---
title: Adaptive Query
category: Spark
tag: [Spark]
---

> Apache Spark는 쿼리 성능을 최적화하는 데 있어 다양한 기술을 활용합니다. Adaptive Query Execution(AQE)는 쿼리 실행 중에 실제 데이터를 바탕으로 최적화를 동적으로 수행하여 성능을 개선하는 기능입니다. 이를 통해 Spark는 쿼리가 실행되는 동안 실행 계획을 동적으로 조정하여 더 나은 성능을 얻을 수 있습니다.

---

## Adaptive Query Execution
**Adaptive Query Execution (AQE)**는 쿼리 실행 중 각 스테이지가 완료될 때마다 실제 실행 통계 정보를 분석하여 더 나은 전략이 있는지 확인하고 동적으로 실행 계획을 조정합니다. 즉, 초기 실행 계획만 따르는 것이 아니라, 데이터의 분포와 크기 같은 실제 실행 정보를 기반으로 최적의 전략을 선택합니다.

[![](\assets\posts\2025-04-13-Adaptive Query.md\aqe.png)](\assets\posts\2025-04-13-Adaptive Query.md\aqe.png)

```python
spark.conf.set("spark.sql.adaptive.enabled", "true")
```

### Coalescing Partitions
`Coalescing Partitions`는 Spark에서 shuffle 이후 생성되는 많은 작은 파티션들을 병합하여 성능을 최적화하는 기능입니다. 

[![](\assets\posts\2025-04-13-Adaptive Query.md\coalescing_before.png)](\assets\posts\2025-04-13-Adaptive Query.md\coalescing_before.png)

많은 작은 파티션들은 Spark의 리소스를 비효율적으로 사용할 수 있습니다. 예를 들어, 너무 많은 파티션이 존재하면 각 파티션을 처리하는 데 드는 시간과 자원 소모가 늘어나 성능 저하를 초래할 수 있습니다.

[![](\assets\posts\2025-04-13-Adaptive Query.md\coalescing.png)](\assets\posts\2025-04-13-Adaptive Query.md\coalescing.png)

`Coalescing Partitions`는 shuffle 과정에서 너무 작은 파티션들을 병합하여 적정 크기의 파티션으로 만들어 성능을 최적화합니다. AQE에서는 이 기능을 활성화하여 불필요한 작은 파티션들을 자동으로 합칠 수 있습니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Coalescing Partitions Example").getOrCreate()

# Coalesce Partitions 활성화
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")

df = spark.read.parquet("data1")

df.groupBy("id").count().show()
```

### Switching Join
`Switching Join`은 Spark에서 실행되는 쿼리의 조인 전략을 상황에 맞게 동적으로 변경하는 기능입니다.

[![](\assets\posts\2025-04-13-Adaptive Query.md\join.png)](\assets\posts\2025-04-13-Adaptive Query.md\join.png)

AQE는 실행 중에 실제 데이터를 기반으로 최적의 조인 전략을 선택합니다. 예를 들어, 작은 테이블을 큰 테이블에 브로드캐스트하여 처리하는 `Broadcast Join`을 선택하거나, 두 테이블이 이미 정렬되어 있을 경우 `Sort-Merge Join`을 선택할 수 있습니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Switching Join Example").getOrCreate()

# Join 전략을 Sort-Merge Join으로 선호하도록 설정
spark.conf.set("spark.sql.join.preferSortMergeJoin", "true")
# Broadcast Join 임계값 설정
spark.conf.set("spark.sql.adaptive.autoBroadcastJoinThreshold", "10MB")

df1 = spark.read.parquet("data1")
df2 = spark.read.parquet("data2")
df1.join(df2, "id").show()
```

### Skew Join
`Skew Join`은 데이터의 분포가 불균형한 경우, 특히 한쪽 테이블의 특정 파티션에 많은 데이터가 몰려 있을 때 성능 저하를 방지하는 최적화 기능입니다. 

[![](\assets\posts\2025-04-13-Adaptive Query.md\skewjoin_before.png)](\assets\posts\2025-04-13-Adaptive Query.md\skewjoin_before.png)

데이터 분포가 불균형한 경우, 특정 파티션에 많은 데이터가 몰리게 되어 해당 파티션을 처리하는 데 많은 시간과 리소스가 소모됩니다. 이러한 불균형은 조인 연산에 큰 성능 저하를 초래할 수 있습니다.

[![](\assets\posts\2025-04-13-Adaptive Query.md\skewjoin.png)](\assets\posts\2025-04-13-Adaptive Query.md\skewjoin.png)

AQE는 스큐가 발생하는 파티션을 동적으로 감지하고, 해당 파티션을 분할하여 처리할 수 있습니다. 이를 통해 성능을 최적화하고, 불균형적인 데이터 분포로 인한 문제를 해결합니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Skew Join Example").getOrCreate()

# Skew Join 최적화 활성화
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

df1 = spark.read.parquet("data1")
df2 = spark.read.parquet("data2")
df1.join(df2, "id").show()
```

## Skew Sorting
AQE 이전에는 데이터가 특정 키에 치우쳐 파티션이 불균형하게 분배될 때, 이를 해결하기 위한 방법으로 랜덤 키 추가 기법이 사용되었습니다. 이 기법은 파티션 균형을 맞추기 위해 별도의 임시 키(예: 파티션 번호)를 추가하여 데이터를 분산시키고, **그룹화(GroupBy)**나 조인 시 해당 키를 활용하여 파티션 간 **로드 밸런싱(load balancing)**을 유도합니다.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, floor, col

spark = SparkSession.builder.appName("Sorting Example").getOrCreate()

df = spark.read.parquet("data1")

# 파티션 균형 유지를 위해 랜덤 키 생성
df_with_salt = df.withColumn("salt", floor(rand() * 10))

# salt 키를 포함하여 그룹화하여 파티션 분산 처리
grouped_df = df_with_salt.groupBy("id", "salt").count()

final_result = grouped_df.groupBy("id").sum("count")
final_result.show()
```

---

## References
- [Databricks 공식 블로그](https://www.databricks.com/blog)
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
