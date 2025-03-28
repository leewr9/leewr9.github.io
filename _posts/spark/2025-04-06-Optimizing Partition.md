---
title: Optimizing Partition
category: Spark
tag: [Spark]
---

> Apache Spark에서 파티셔닝은 데이터 분산 및 작업 성능에 중요한 영향을 미칩니다. 적절한 파티셔닝 전략을 사용하면 데이터 처리 속도를 크게 향상시킬 수 있습니다. 데이터셋의 크기와 파티션 수를 최적화하면 병렬 처리 효율성을 높이고 리소스를 절약할 수 있습니다.

---

## Partitioning
Spark는 데이터를 여러 파티션으로 분배하거나 기존 파티션을 변경하는 함수들을 제공합니다. 이를 통해 데이터 분산 처리 성능을 최적화할 수 있습니다.

### repartition
`repartition`은 데이터를 지정한 수의 파티션으로 완전히 재분배하는 함수입니다. 주로 데이터가 너무 작거나 분포가 불균형할 때, 또는 병렬 처리 성능을 최적화하려고 할 때 사용됩니다. 

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Repartition Example").getOrCreate()

data = [(1, "A"), (2, "B"), (3, "C"), (4, "D")]
columns = ["id", "value"]
df = spark.createDataFrame(data, columns)

# 데이터를 4개의 파티션으로 재분배
df_repartitioned = df.repartition(4)
df_repartitioned.show()
```

- 완전한 셔플링을 통해 데이터의 균등 분배를 보장합니다.
- 데이터가 클 경우 성능 저하가 발생할 수 있습니다.
- 적절한 파티션 수는 클러스터 리소스에 따라 다릅니다.

### coalesce
coalesce는 기존의 파티션을 병합하여 파티션 수를 줄이는 방법입니다. repartition은 파티션을 늘리거나 재배치하는 데 사용되지만, coalesce는 파티션을 줄이는 데 적합합니다. 

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Coalesce Example").getOrCreate()

data = [(1, "A"), (2, "B"), (3, "C"), (4, "D")]
columns = ["id", "value"]
df = spark.createDataFrame(data, columns)

# 데이터를 2개의 파티션으로 병합
df_coalesced = df_repartitioned.coalesce(2)
df_coalesced.show()
```

- 파티션 수를 줄이는 데 적합합니다.
- 작은 데이터셋에서 성능을 최적화할 때 유용합니다.
- 파티션 수를 줄일 때만 사용해야 하며, 늘리는 데는 `repartition`이 더 적합합니다.

### repartitionByRange
`repartitionByRange`는 데이터를 지정된 컬럼 값에 따라 정렬하면서 파티션을 재분배하는 방법입니다. 이 방법은 특정 범위에 따라 데이터를 파티션하는데 유용하며, 범위 기반 조인이나 정렬된 데이터를 필요로 하는 연산에 최적화된 방법입니다. 

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RepartitionByRange Example").getOrCreate()

data = [(1, "A"), (2, "B"), (3, "C"), (4, "D")]
columns = ["id", "value"]
df = spark.createDataFrame(data, columns)

# 컬럼 'id' 값에 따라 4개의 파티션으로 재분배
df_repartitioned_range = df.repartitionByRange(4, "id")
df_repartitioned_range.show()
```

- 데이터를 특정 컬럼 값의 범위에 따라 분배하여, 해당 컬럼을 기준으로 작업을 병렬화합니다.
- 범위 기반 조인, 정렬된 데이터를 다룰 때 효율적입니다.
- 셔플링이 발생하지만, 정렬된 데이터가 필요한 작업에서 유리합니다.

---

## Dynamic Partition Pruning
`Dynamic Partition Pruning`은 조인 연산을 최적화하는 데 유용한 기법으로, 실행 시간에 파티션을 동적으로 필터링하여 성능을 향상시킵니다. 주로 조인 작업에서 큰 성능 향상을 제공하는데, 이는 불필요한 파티션을 읽지 않고 필요한 데이터만 효율적으로 처리할 수 있게 해줍니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Dynamic Partition Example").getOrCreate()

df1 = spark.read.parquet("/path/to/parquet1")
df2 = spark.read.parquet("/path/to/parquet2")

# 데이터에서 특정 value > 1000 조건을 걸어 필터링
df2_filtered = df2.filter(df2.value > 1000)

# df2_filtered의 id 값에 해당하는 df1의 파티션만 읽게 됨
# 예를 들어, df2_filtered에서 id가 1, 2, 3이라면
# df1에서 id=1, id=2, id=3이 포함된 파티션만 읽게 되며
# 이때 `df1`에서 `id` 값을 기준으로만 필터링이 적용됨
result = df1.join(df2, df1.id == df2.id)
result.show()
```

- `spark.sql.dynamicPartitionPruning.enabled` : 동적 파티션 프루닝 활성화 (기본값: `true`)
- 필요한 파티션만 읽어 성능을 향상시킵니다.
- 실행 중에 동적으로 파티션을 선택하여 불필요한 파티션 필터링을 자동으로 수행합니다.
- 필터링 조건에 따라 효율적으로 작업을 분배할 수 있습니다.

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
