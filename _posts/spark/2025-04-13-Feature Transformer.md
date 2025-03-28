---
title: Feature Transformer
category: Spark
tag: [SparkML, Spark]
---

> SparkML에서 Feature Transformer는 데이터를 모델이 처리할 수 있는 형태로 변환하는 중요한 역할을 합니다. 대부분의 머신러닝 알고리즘은 숫자형 데이터만을 처리할 수 있기 때문에, 다양한 변환 작업을 통해 데이터를 모델에 맞게 준비하는 것이 필요합니다. 

---

## Imputer
`Imputer`는 비어있는 값을 처리하는 데 사용되는 변환기입니다. 주로 데이터셋에서 비어있는 값(NaN)을 평균, 중간 또는 자주 나오는 값으로 대체할 때 사용됩니다. 이 방법은 데이터를 분석할 수 있도록 완전하게 만들어주는 중요한 기법입니다.

- `mean`: 평균값으로 비어있는 값 대체 (기본값)
- `median`: 중간값으로 비어있는 값 대체
- `mode`: 가장 자주 나오는 값으로 비어있는 값 대체

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import Imputer

spark = SparkSession.builder.appName("Imputer Example").getOrCreate()

# 데이터 준비
data = spark.createDataFrame([
    (1.0, 2.0),
    (2.0, None),
    (3.0, 3.0),
    (None, 4.0),
    (5.0, 5.0),
], ["col1", "col2"])

# Imputer 설정 (비어있는 값을 각 컬럼의 평균값으로 대체)
imputer = Imputer(inputCols=["col1", "col2"], outputCols=["col1_imputed", "col2_imputed"], 
                  strategy="mean")

# 변환 실행
imputer_model = imputer.fit(data)
imputed_data = imputer_model.transform(data)
imputed_data.show()
```

```bash
+----+----+------------+------------+
|col1|col2|col1_imputed|col2_imputed|
+----+----+------------+------------+
| 1.0| 2.0|         1.0|         2.0|
| 2.0|NULL|         2.0|         3.5|
| 3.0| 3.0|         3.0|         3.0|
|NULL| 4.0|        2.75|         4.0|
| 5.0| 5.0|         5.0|         5.0|
+----+----+------------+------------+
```

---

## Feature 

### VectorAssembler
`VectorAssembler`는 여러 개의 개별 컬럼을 하나의 벡터로 결합하는 데 사용됩니다. 이 벡터는 머신러닝 알고리즘에서 입력으로 사용될 수 있습니다.

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.appName("VectorAssembler Example").getOrCreate()

# 데이터 준비
data = spark.createDataFrame([(1, 2), (3, 4)], ["feature1", "feature2"])

# VectorAssembler 설정
assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")

# 변환 실행
data_transformed = assembler.transform(data)
data_transformed.show()
```

```bash
+--------+--------+---------+
|feature1|feature2| features|
+--------+--------+---------+
|       1|       2|[1.0,2.0]|
|       3|       4|[3.0,4.0]|
+--------+--------+---------+
```

### StringIndexer
`StringIndexer`는 범주형 데이터를 숫자형으로 변환하는 데 사용됩니다. 이 변환을 통해 범주형 데이터를 머신러닝 알고리즘이 처리할 수 있는 숫자형 데이터로 변환할 수 있습니다.

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer

spark = SparkSession.builder.appName("StringIndexer Example").getOrCreate()

# 데이터 준비
data = spark.createDataFrame([("Male",), ("Female",), ("Female",)], ["gender"])

# StringIndexer 설정
indexer = StringIndexer(inputCol="gender", outputCol="gender_index")

# 변환 실행
data_transformed = indexer.fit(data).transform(data)
data_transformed.show()
```

```bash
+------+------------+
|gender|gender_index|
+------+------------+
|  Male|         1.0|
|Female|         0.0|
|Female|         0.0|
+------+------------+
```

### OneHotEncoder
`OneHotEncoder`는 범주형 데이터를 원-핫 인코딩 방식으로 변환하는 데 사용됩니다. 원-핫 인코딩은 각 범주형 변수의 고유 값마다 새로운 컬럼을 생성하고, 해당 값에 대해서만 1을 할당하며 나머지는 0으로 채웁니다. 

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, OneHotEncoder

spark = SparkSession.builder.appName("OneHotEncoder Example").getOrCreate()

# 데이터 준비
data = spark.createDataFrame([("Male",), ("Female",), ("Other",), ("Female",), ("Other",)], ["gender"])

# StringIndexer 설정 
indexer = StringIndexer(inputCol="gender", outputCol="gender_index")

# OneHotEncoder 설정
encoder = OneHotEncoder(inputCol="gender_index", outputCol="gender_onehot")

# 변환 실행
indexed_data = indexer.fit(data).transform(data)
encoded_data = encoder.fit(indexed_data).transform(indexed_data)
encoded_data.show()
```

```bash
+------+------------+-------------+
|gender|gender_index|gender_onehot|
+------+------------+-------------+
|  Male|         2.0|    (2,[],[])|
|Female|         0.0|(2,[0],[1.0])|
| Other|         1.0|(2,[1],[1.0])|
|Female|         0.0|(2,[0],[1.0])|
| Other|         1.0|(2,[1],[1.0])|
+------+------------+-------------+
```

---

## Scaling 

### StandardScaler
`StandardScaler`는 데이터를 평균 0, 표준편차 1로 변환하는 방법입니다. 이 변환은 데이터의 분포가 평균적으로 0에 가까워지고, 표준편차는 1로 맞춰집니다. 이를 통해 다양한 스케일을 가진 특성들이 동일한 기준으로 비교할 수 있습니다.

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import StandardScaler
from pyspark.ml.linalg import Vectors

spark = SparkSession.builder.appName("StandardScaler Example").getOrCreate()

# 데이터 준비
data = spark.createDataFrame([
    (Vectors.dense([88.0, 95.0]),),
    (Vectors.dense([78.0, 85.0]),),
    (Vectors.dense([92.0, 80.0]),),
    (Vectors.dense([70.0, 90.0]),),
    (Vectors.dense([85.0, 65.0]),),
], ["features"])

# StandardScaler 설정
scaler = StandardScaler(inputCol="features", outputCol="scaled_features", 
                        withMean=True, withStd=True)

# 변환 실행
scaler_model = scaler.fit(data)
scaled_data = scaler_model.transform(data)
scaled_data.show(truncate=False)
```

[![](\assets\posts\2025-04-13-Feature Transformer.md\standard.png)](\assets\posts\2025-04-13-Feature Transformer.md\standard.png)

```bash
+-----------+-----------------------------------------+
|features   |scaled_features                          |
+-----------+-----------------------------------------+
|[88.0,95.0]|[0.6202391231781861,1.0424933826313665]  |
|[78.0,85.0]|[-0.5283518456703055,0.17374889710522776]|
|[92.0,80.0]|[1.0796755107175826,-0.2606233456578416] |
|[70.0,90.0]|[-1.4472246207490986,0.6081211398682972] |
|[85.0,65.0]|[0.27566183252363863,-1.5637400739470497]|
+-----------+-----------------------------------------+
```

### MinMaxScaler
`MinMaxScaler`는 데이터를 0과 1 사이로 변환하는 방법입니다. 모든 특성(feature)의 값을 최소값과 최대값을 기준으로 0과 1 사이로 스케일링합니다. 이 변환은 각 특성의 범위를 고정된 구간으로 바꾸므로, 정규화와는 다른 방식으로 데이터를 처리합니다. 

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import MinMaxScaler
from pyspark.ml.linalg import Vectors

spark = SparkSession.builder.appName("MinMaxScaler Example").getOrCreate()

# 데이터 준비
data = spark.createDataFrame([
    (Vectors.dense([88.0, 95.0]),),
    (Vectors.dense([78.0, 85.0]),),
    (Vectors.dense([92.0, 80.0]),),
    (Vectors.dense([70.0, 90.0]),),
    (Vectors.dense([85.0, 65.0]),),
], ["features"])

# MinMaxScaler 설정
scaler = MinMaxScaler(inputCol="features", outputCol="scaled_features")

# 변환 실행
scaler_model = scaler.fit(data)
scaled_data = scaler_model.transform(data)
scaled_data.show(truncate=False)
```

[![](\assets\posts\2025-04-13-Feature Transformer.md\minmax.png)](\assets\posts\2025-04-13-Feature Transformer.md\minmax.png)

```bash
+-----------+----------------------------------------+
|features   |scaled_features                         |
+-----------+----------------------------------------+
|[88.0,95.0]|[0.8181818181818182,1.0]                |
|[78.0,85.0]|[0.36363636363636365,0.6666666666666666]|
|[92.0,80.0]|[1.0,0.5]                               |
|[70.0,90.0]|[0.0,0.8333333333333334]                |
|[85.0,65.0]|[0.6818181818181819,0.0]                |
+-----------+----------------------------------------+
```


### PCA 
**PCA(Principal Component Analysis)**는 고차원 데이터를 저차원으로 변환하여 데이터 분석의 효율성을 높이는 차원 축소 기법입니다. 이 방법은 데이터의 주요 특성을 유지하면서 불필요한 차원을 제거하는 데 사용됩니다.

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import StandardScaler, PCA
from pyspark.ml.linalg import Vectors

spark = SparkSession.builder.appName("PCA Example").getOrCreate()

# 데이터 준비
data = spark.createDataFrame([
    (Vectors.dense([88.0, 95.0, 100.0]),),
    (Vectors.dense([78.0, 85.0, 92.0]),),
    (Vectors.dense([92.0, 80.0, 85.0]),),
    (Vectors.dense([70.0, 90.0, 88.0]),),
    (Vectors.dense([85.0, 65.0, 78.0]),),
], ["features"])

# StandardScaler 설정
scaler = StandardScaler(inputCol="features", outputCol="scaled_features")

# PCA 설정 (데이터를 2개의 주요 특성으로 축소)
pca = PCA(k=2, inputCol="features", outputCol="pca_features")

# 변환 실행
scaled_data = scaler.fit(data).transform(data)
pca_result = pca.fit(scaled_data).transform(scaled_data)
pca_result.show(truncate=False)
```

```bash
+-----------------+----------------------------------------------------------+----------------------------------------+
|features         |scaled_features                                           |pca_features                            |
+-----------------+----------------------------------------------------------+----------------------------------------+
|[88.0,95.0,100.0]|[10.107600525866724,8.253072612498318,12.235219605809911] |[115.94312569668075,-115.18310280536284]|
|[78.0,85.0,92.0] |[8.959009557018234,7.384328126972179,11.256402037345119]  |[105.2517184717962,-103.02219229284357] |
|[92.0,80.0,85.0] |[10.567036913406122,6.9499558842091105,10.399936664938425]|[94.76135687876607,-114.43956268969211] |
|[70.0,90.0,88.0] |[8.04013678193944,7.818700369735249,10.766993253112723]   |[108.63800952870585,-94.4516122589839]  |
|[85.0,65.0,78.0] |[9.763023235212177,5.646839155919902,9.54347129253173]    |[79.97196725656475,-105.2347172029608]  |
+-----------------+----------------------------------------------------------+----------------------------------------+
```

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
