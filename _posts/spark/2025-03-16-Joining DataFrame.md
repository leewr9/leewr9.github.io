---
title: Joining DataFrame
category: Spark
tag: [DataFrame, Spark SQL, Spark]
---

> Spark에서는 DataFrame과 Spark SQL을 사용하여 데이터를 결합할 수 있습니다. 이 때 데이터셋의 크기가 매우 다를 경우, Broadcast를 사용하여 작은 데이터셋을 모든 노드에 분배함으로써 조인의 성능을 크게 향상시킬 수 있습니다.

---

## DataFrame
DataFrame에서는 `join()` 함수를 사용하여 두 개의 DataFrame을 결합할 수 있습니다. 이때 broadcast()를 사용하면 작은 테이블을 클러스터의 모든 작업자 노드에 복제하여 셔플링을 줄일 수 있습니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark DataFrame Join").getOrCreate()

data1 = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
data2 = [(1, "HR"), (2, "Engineering"), (3, "Marketing")]

df1 = spark.createDataFrame(data1, ["Name", "DeptID"])
df2 = spark.createDataFrame(data2, ["DeptID", "DeptName"])

# Join Expression
join_expr = df1["DeptID"] == df2["DeptID"]

result = df1.join(df2, join_expr, "inner")
result.collect()
```

### Broadcast
DataFrame API에서는 broadcast()를 사용하여 작은 테이블을 브로드캐스트하여 성능을 향상시킬 수 있습니다.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

spark = SparkSession.builder.appName("Spark DataFrame Join with Broadcast").getOrCreate()

data1 = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
data2 = [(1, "HR"), (2, "Engineering"), (3, "Marketing")]

df1 = spark.createDataFrame(data1, ["Name", "DeptID"])
df2 = spark.createDataFrame(data2, ["DeptID", "DeptName"])

# Join Expression
join_expr = df1["DeptID"] == df2["DeptID"]

# Broadcast Join
result = df1.join(broadcast(df2), join_expr, "inner")
result.show()
```

```bash
+-----+-------+-----------+
| Name| DeptID|   DeptName|
+-----+-------+-----------+
|Alice|      1|         HR|
|  Bob|      2|Engineering|
|Cathy|      3|  Marketing|
+-----+-------+-----------+
```

---

## Spark SQL
Spark SQL에서는 `JOIN`을 `SQL` 쿼리로 처리할 수 있습니다. 기본적인 조인 방식으로 테이블을 결합할 수 있습니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark SQL Join").getOrCreate()

data1 = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
data2 = [(1, "HR"), (2, "Engineering"), (3, "Marketing")]

df1 = spark.createDataFrame(data1, ["Name", "DeptID"])
df2 = spark.createDataFrame(data2, ["DeptID", "DeptName"])

df1.createOrReplaceTempView("employees")
df2.createOrReplaceTempView("departments")

result = spark.sql("SELECT e.Name, e.DeptID, d.DeptName "
                   "FROM employees e JOIN departments d ON e.DeptID = d.DeptID")
result.collect()
```

### Broadcast
SQL 쿼리에서도 `BROADCAST` 힌트를 사용하여 작은 테이블을 브로드캐스트할 수 있습니다. 이 방법을 사용하면 셔플링을 줄이고 성능을 개선할 수 있습니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark SQL Join with Broadcast").getOrCreate()

data1 = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
data2 = [(1, "HR"), (2, "Engineering"), (3, "Marketing")]

df1 = spark.createDataFrame(data1, ["Name", "DeptID"])
df2 = spark.createDataFrame(data2, ["DeptID", "DeptName"])

df1.createOrReplaceTempView("employees")
df2.createOrReplaceTempView("departments")

# Broadcast Join
result = spark.sql("SELECT /*+ BROADCAST(d) */ e.Name, e.DeptID, d.DeptName "
                   "FROM employees e JOIN departments d ON e.DeptID = d.DeptID")
result.show()
```

```bash
+-----+-------+-----------+
| Name| DeptID|   DeptName|
+-----+-------+-----------+
|Alice|      1|         HR|
|  Bob|      2|Engineering|
|Cathy|      3|  Marketing|
+-----+-------+-----------+
```

---

## Broadcast Join
`broadcast()` 조인은 작은 데이터셋을 클러스터의 모든 Executor에 복제하여, 셔플링을 최소화하고 성능을 크게 향상시킬 수 있습니다. 이 방식은 특히 데이터셋의 크기가 매우 다를 때 유용하며, 큰 데이터셋에서 셔플링이 발생하지 않도록 하여 처리 속도를 크게 개선할 수 있습니다.

- 셔플링 감소: 작은 데이터셋을 브로드캐스트하여 셔플링을 줄입니다.
- 작은 테이블의 빠른 처리: 작은 테이블을 각 작업자 노드에서 로컬로 처리할 수 있습니다.
- 메모리 최적화: 작은 데이터셋을 메모리에 올려놓고 계산하여 디스크 I/O를 줄입니다.

Spark는 기본적으로 `spark.sql.autoBroadcastJoinThreshold` 설정을 통해 자동으로 broadcast 조인을 적용합니다. 이를 변경하려면 설정값을 조정할 수 있습니다.
```python
# 기본값 10485760 (10 MB)
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "-1") # 해제
```

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
