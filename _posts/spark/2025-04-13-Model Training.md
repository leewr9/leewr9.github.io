---
title: Model Training
category: Spark
tag: [SparkML, Spark]
---

> SparkML에서 모델 학습은 데이터에서 숨겨진 패턴이나 관계를 학습하고, 이를 기반으로 새로운 데이터에 대한 예측을 수행하는 과정입니다. 이 과정은 데이터를 분석하고, 모델을 구축하여 실제 상황에서 유용한 예측을 할 수 있게 합니다.

---

## Regression
`Regression`은 변수 간의 관계를 모델링하고, 이를 바탕으로 연속적인 값을 예측하는 기법입니다. 주로 예측 문제에서 사용되며, 특정 변수들의 값을 입력받아 연속적인 출력값을 예측하는 데 사용됩니다.

- `LinearRegression`: 연속적인 값을 예측하는 기본적인 선형 회귀 모델
- `DecisionTreeRegressor`: 결정 트리를 사용한 비선형 회귀 모델
- `RandomForestRegressor`: 여러 개의 결정 트리로 예측을 평균화한 앙상블 모델

### LinearRegression
`LinearRegression`는 독립 변수와 종속 변수 간의 관계가 직선으로 표현될 수 있다고 가정하는 기법입니다. 즉, 변수들 간의 관계를 선형 함수로 모델링하여 예측값을 계산합니다. 

```python
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Regression Example").getOrCreate()

data = [(i, (i + 10), (i * 10)) for i in range(1000)]
columns = ["id", "label", "value"]
df = spark.createDataFrame(data, columns)

assembler = VectorAssembler(inputCols=["id", "label"], outputCol="features")
df = assembler.transform(df)

train, test = df.randomSplit([0.7, 0.3])

# 모델 학습
lr = LinearRegression(featuresCol="features", labelCol="value")
lr_model = lr.fit(train)

# 예측 결과 출력
predictions = lr_model.transform(test)
predictions.select("id", "value", "prediction").show(5)
```

```bash
+---+-----+--------------------+
| id|value|          prediction|
+---+-----+--------------------+
|  0|    0|2.870592652470804...|
|  4|   40|  40.000000000002856|
|  6|   60|   60.00000000000284|
|  7|   70|   70.00000000000284|
| 10|  100|  100.00000000000284|
+---+-----+--------------------+
only showing top 5 rows
```

---

## Classification
`Classification`은 주어진 데이터를 여러 카테고리나 클래스로 나누는 기법입니다. 주로 이진 분류 또는 다중 클래스 분류 문제에 사용되며, 데이터가 특정 클래스에 속할 확률을 예측합니다.

- `LogisticRegression`: 이진 분류 문제를 해결하는 로지스틱 회귀 모델
- `DecisionTreeClassifier`: 결정 트리를 이용한 분류 모델
- `RandomForestClassifier`: 앙상블 방법으로 여러 트리 예측을 결합한 분류 모델

### LogisticRegression
`LogisticRegression`은 선형 회귀의 확장으로, 종속 변수의 값이 연속적인 것이 아니라 이진 분류(0 또는 1)인 경우에 사용됩니다. 즉, 어떤 데이터가 특정 클래스에 속할 확률을 예측하는 모델입니다. 

```python
import random
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Classification Example").getOrCreate()

data = [(random.random() * 5, random.random() * 5, 0) for _ in range(1000)] + \
       [(random.random() * 10, random.random() * 10, 1) for _ in range(1000)]
columns = ["id", "label", "value"]
df = spark.createDataFrame(data, columns)

# 특성 벡터화
assembler = VectorAssembler(inputCols=["id", "label"], outputCol="features")
df = assembler.transform(df)

train, test = df.randomSplit([0.7, 0.3])

# 모델 학습
lr = LogisticRegression(featuresCol="features", labelCol="value")
lr_model = lr.fit(train)

# 예측 결과 출력
predictions = lr_model.transform(test)
predictions.select("id", "value", "probability", "prediction").show(5)
```

```bash
+--------------------+-----+--------------------+----------+
|                  id|value|         probability|prediction|
+--------------------+-----+--------------------+----------+
|0.005162264404748873|    0|[0.95288494725835...|       0.0|
| 0.04333524871527106|    0|[0.89117339637285...|       0.0|
| 0.04440304076649193|    0|[0.96235489185143...|       0.0|
|0.046178032361606225|    0|[0.96087295609275...|       0.0|
| 0.06941208209954919|    0|[0.95498469164518...|       0.0|
+--------------------+-----+--------------------+----------+
only showing top 5 rows
```

---

## Clustering
`Clustering`은 주어진 데이터셋을 유사한 특성을 가진 그룹으로 나누는 비지도 학습 기법입니다. 데이터의 레이블이 없을 때, 비슷한 데이터를 묶는 데 사용됩니다. 그룹화는 데이터의 구조나 패턴을 발견하는 데 유용합니다.

- `KMeans`: 데이터를 K개의 군집으로 나누는 군집화 모델
- `BisectingKMeans`: `KMeans`의 변형으로, 이진 분할 방식으로 군집화

### KMeans
`KMeans`는 데이터를 K개의 군집으로 나누는 비지도 학습 기법입니다. `KMeans`는 주어진 데이터를 K개의 군집으로 분할하고, 각 군집의 중심점을 계산하여 데이터를 할당하는 방식으로 작동합니다. 데이터 포인트는 가장 가까운 중심점을 기준으로 군집에 속하게 됩니다.

```python
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Clustering Example").getOrCreate()

data = [(i, i * 10) for i in range(1000)]
columns = ["id", "value"]
df = spark.createDataFrame(data, columns)

# 특성 벡터화
assembler = VectorAssembler(inputCols=["id", "value"], outputCol="features")
df = assembler.transform(df)

train, test = df.randomSplit([0.7, 0.3])

# 모델 학습
kmeans = KMeans(k=3, seed=7, featuresCol="features", predictionCol="prediction")
km_model = kmeans.fit(train)

# 예측 결과 출력
predictions = km_model.transform(test)
predictions.groupBy("prediction").count().show()
```

```bash
+----------+-----+
|prediction|count|
+----------+-----+
|         1|  118|
|         2|  107|
|         0|  108|
+----------+-----+
```

## Persistence
한 번 학습된 모델을 저장하면, 나중에 다시 불러와서 예측에 사용할 수 있습니다. 이를 통해 모델을 재학습하지 않고도 동일한 성능을 유지하면서 빠르게 결과를 도출할 수 있습니다. 

```python
from pyspark.ml.regression import LinearRegressionModel
from pyspark.ml.clustering import KMeansModel

# 모델 저장
lr_model.save("linear_regression_model")
km_model.save("kmeans_model")

# 저장된 모델 로드
loaded_lr_model = LinearRegressionModel.load("linear_regression_model")
loaded_km_model = LinearRegressionModel.load("kmeans_model")
```

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
