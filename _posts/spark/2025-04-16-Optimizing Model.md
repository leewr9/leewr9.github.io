---
title: Optimizing Model
category: Spark
tag: [SparkML, Spark]
---

> SparkML은 대규모 데이터 처리를 위한 강력한 머신러닝 라이브러리로, 모델을 학습하고 최적화하는 데 필요한 다양한 기능을 제공합니다. 모델 튜닝은 하이퍼파라미터를 최적화하여 성능을 극대화하는 과정이며, 파이프라인은 여러 머신러닝 단계를 연결하여 효율적으로 데이터를 처리하고 모델을 학습할 수 있게 합니다.

---

## Tuning

모델을 최적화하기 위한 방법 중 하나는 하이퍼파라미터 튜닝입니다. 모델 성능을 최적화하기 위해서는 여러 하이퍼파라미터를 테스트하고 가장 적합한 값을 찾아야 합니다.

### CrossValidator

`CrossValidator`는 데이터셋을 여러 개로 나누어 모델을 학습하고 평가하는 방법입니다. 각 폴드에서 모델을 학습하고, 나머지 데이터를 사용하여 성능을 평가합니다. 이렇게 여러 번 학습과 평가를 반복함으로써 모델의 일반화 성능을 더 정확히 평가할 수 있습니다.

```python
from pyspark.ml.regression import LinearRegression
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Regression Example").getOrCreate()

data = [(i, (i + 10), (i * 10)) for i in range(1000)]
columns = ["id", "label", "value"]
df = spark.createDataFrame(data, columns)

assembler = VectorAssembler(inputCols=["id", "label"], outputCol="features")
df = assembler.transform(df)

train, test = df.randomSplit([0.7, 0.3])

lr = LinearRegression(featuresCol="features", labelCol="value")

# CrossValidator 설정
paramGrid = ParamGridBuilder() \
    .addGrid(lr.regParam, [0.1, 0.5, 1.0]) \
    .addGrid(lr.elasticNetParam, [0.0, 0.5, 1.0]) \
    .build()

evaluator = RegressionEvaluator(labelCol="value", predictionCol="prediction",
                                metricName="rmse")
crossval = CrossValidator(
  estimator=lr,
  estimatorParamMaps=paramGrid,
  evaluator=evaluator,
  numFolds=5
)

# 모델 학습
cv_model = crossval.fit(train)
for i, (metric, model) in enumerate(zip(cv_model.avgMetrics, cv_model.getEstimatorParamMaps())):
    param = [f"{k.name}: {v}" for k, v in model.items()]
    print(f"Model {i + 1} RMSE: {metric} {' '.join(param)}")

# 최적 모델 평가
cv_predictions = cv_model.transform(test)
rmse = evaluator.evaluate(cv_predictions)
print(f"RMSE: {rmse}")
```

```bash
Model 1 RMSE: 0.050064284686751725 regParam: 0.1 elasticNetParam: 0.0 # 최적 모델
Model 2 RMSE: 0.07509708016663194 regParam: 0.1 elasticNetParam: 0.5
Model 3 RMSE: 0.10013031108426895 regParam: 0.1 elasticNetParam: 1.0
Model 4 RMSE: 0.2503040078358246 regParam: 0.5 elasticNetParam: 0.0
Model 5 RMSE: 0.3754723384486245 regParam: 0.5 elasticNetParam: 0.5
Model 6 RMSE: 0.5006515554203652 regParam: 0.5 elasticNetParam: 1.0
Model 7 RMSE: 0.5005644834945263 regParam: 1.0 elasticNetParam: 0.0
Model 8 RMSE: 0.7509120235063709 regParam: 1.0 elasticNetParam: 0.5
Model 9 RMSE: 1.001303110840908 regParam: 1.0 elasticNetParam: 1.0
RMSE: 0.05070547812607801
```

- `regParam`: 모델의 복잡도 제어 파라미터
  - 값이 클 때: 모델이 더 간단해짐 (과적합 방지)
  - 값이 작을 때: 모델이 더 복잡해짐 (과적합 가능성 증가)
- `elasticNetParam`: **L1 (Lasso)**과 **L2 (Ridge)** 정규화 비율 설정 파라미터
  - 0: L2만 사용 (모든 특성의 영향을 균등하게 조정)
  - 1: L1만 사용 (불필요한 특성 제거)
  - 0과 1 사이: L1과 L2를 섞어서 사용

### TrainValidationSplit

`TrainValidationSplit`은 데이터를 훈련 세트와 검증 세트로 나누어 모델을 평가하는 방법입니다. `CrossValidator`와 달리, 여러 번의 폴드 분할을 하지 않고 한 번의 훈련/검증을 통해 모델을 최적화합니다.

```python
import random
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TrainValidationSplit Example").getOrCreate()

data = [(random.random() * 5, random.random() * 5, 0) for _ in range(1000)] + \
       [(random.random() * 10, random.random() * 10, 1) for _ in range(1000)]
columns = ["id", "label", "value"]
df = spark.createDataFrame(data, columns)

assembler = VectorAssembler(inputCols=["id", "label"], outputCol="features")
df = assembler.transform(df)

train, test = df.randomSplit([0.7, 0.3])

lr = LogisticRegression(featuresCol="features", labelCol="value")

# TrainValidationSplit 설정
paramGrid = ParamGridBuilder() \
    .addGrid(lr.maxIter, [1, 5, 10]) \
    .addGrid(lr.regParam, [0.1, 0.5, 1.0]) \
    .build()

evaluator = BinaryClassificationEvaluator(labelCol="value", rawPredictionCol="prediction",
                                          metricName="areaUnderROC")
tvs = TrainValidationSplit(
  estimator=lr,
  estimatorParamMaps=paramGrid,
  evaluator=evaluator,
  trainRatio=0.5)

# 모델 학습
tvs_model = tvs.fit(train)
for i, (metric, model) in enumerate(zip(tvs_model.validationMetrics, tvs_model.getEstimatorParamMaps())):
    param = [f"{k.name}: {v}" for k, v in model.items()]
    print(f"Model {i + 1} AUC: {metric} {' '.join(param)}")

# 최적 모델 평가
tvs_predictions = tvs_model.transform(test)
auc = evaluator.evaluate(tvs_predictions)
print(f"AUC: {auc}")
```

```bash
Model 1 AUC: 0.8001051707575607 maxIter: 1 regParam: 0.1 # 최적 모델
Model 2 AUC: 0.7856628242074928 maxIter: 1 regParam: 0.5
Model 3 AUC: 0.7798535890556163 maxIter: 1 regParam: 1.0
Model 4 AUC: 0.7871120275597071 maxIter: 5 regParam: 0.1
Model 5 AUC: 0.782764417503064 maxIter: 5 regParam: 0.5
Model 6 AUC: 0.7784043857034019 maxIter: 5 regParam: 1.0
Model 7 AUC: 0.7871120275597071 maxIter: 10 regParam: 0.1
Model 8 AUC: 0.782764417503064 maxIter: 10 regParam: 0.5
Model 9 AUC: 0.7784043857034019 maxIter: 10 regParam: 1.0
AUC: 0.8015578223749862
```

- `maxIter`: 모델 학습의 최대 반복 횟수 설정 파라미터
  - 값이 클 때: 불필요한 학습이 발생할 수 있음 (과적합, 계산 비용 증가)
  - 값이 작을 때: 학습이 부족할 수 있음 (성능 저하)

---

## Pipeline

`Pipeline`은 데이터 전처리, 모델 학습, 예측 과정 등을 체계적으로 관리할 수 있게 해주는 중요한 도구입니다. 파이프라인을 사용하면 데이터 변환과 모델 학습을 한 번에 처리할 수 있어 코드가 간결해지고 효율적입니다.

[![](\assets\posts\2025-04-16-Optimizing Model.md\pipeline.png)](\assets\posts\2025-04-16-Optimizing Model.md\pipeline.png)

```python
import random
from pyspark.ml import Pipeline
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import Imputer, StringIndexer, VectorAssembler

spark = SparkSession.builder.appName("Pipeline Example").getOrCreate()

def get_data():
  data = [(i, random.choice([None, i * 10]), i, random.choice(["Male", "Female", "Other"]))
          for i in range(1000)]
  columns = ["id", "label", "value", "gender"]
  df = spark.createDataFrame(data, columns)

  return df.randomSplit([0.7, 0.3])

def get_stages():
  imputer = Imputer(inputCols=["id", "label"], outputCols=["id_imputed", "label_imputed"],
                    strategy="mean")
  indexer = StringIndexer(inputCol="gender", outputCol="gender_index")

  assembler = VectorAssembler(inputCols=["id_imputed", "label_imputed", "gender_index"],
                              outputCol="features")
  lr = LinearRegression(featuresCol="features", labelCol="value")

  return [imputer, indexer, assembler, lr]

# Pipeline 구성
pipeline = Pipeline(stages=get_stages())

# 모델 학습
train, test = get_data()
lr_model = pipeline.fit(train)

# 예측 결과 출력
predictions = lr_model.transform(test)
predictions.show(5)

# 두 번째 모델 학습
sec_train, sec_test = get_data()
lr_sec_model = pipeline.fit(sec_train)

# 두 번째 예측 결과 출력
sec_predictions = lr_sec_model.transform(sec_test)
sec_predictions.show(5)
```

```bash
+---+-----+-----+------+----------+-------------+------------+-----------------+--------------------+
| id|label|value|gender|id_imputed|label_imputed|gender_index|         features|          prediction|
+---+-----+-----+------+----------+-------------+------------+-----------------+--------------------+
|  0| NULL|    0|  Male|         0|         4848|         1.0| [0.0,4848.0,1.0]|6.769261421301903...|
|  8| NULL|    8|Female|         8|         4848|         2.0| [8.0,4848.0,2.0]|   7.999999999999972|
| 12|  120|   12|  Male|        12|          120|         1.0| [12.0,120.0,1.0]|  12.000000000000421|
| 13| NULL|   13|Female|        13|         4848|         2.0|[13.0,4848.0,2.0]|   12.99999999999997|
| 16| NULL|   16| Other|        16|         4848|         0.0|[16.0,4848.0,0.0]|  16.000000000000163|
+---+-----+-----+------+----------+-------------+------------+-----------------+--------------------+
only showing top 5 rows

+---+-----+-----+------+----------+-------------+------------+-----------------+----------+
| id|label|value|gender|id_imputed|label_imputed|gender_index|         features|prediction|
+---+-----+-----+------+----------+-------------+------------+-----------------+----------+
|  1| NULL|    1|  Male|         1|         5041|         2.0| [1.0,5041.0,2.0]|       1.0|
|  6|   60|    6| Other|         6|           60|         0.0|   [6.0,60.0,0.0]|       6.0|
|  8|   80|    8|Female|         8|           80|         1.0|   [8.0,80.0,1.0]|       8.0|
| 10| NULL|   10|  Male|        10|         5041|         2.0|[10.0,5041.0,2.0]|      10.0|
| 12|  120|   12|Female|        12|          120|         1.0| [12.0,120.0,1.0]|      12.0|
+---+-----+-----+------+----------+-------------+------------+-----------------+----------+
only showing top 5 rows
```

---

## References

- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
