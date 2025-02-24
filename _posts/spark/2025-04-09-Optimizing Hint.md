---
title: Optimizing Hint
category: Spark
tag: [Spark]
---

> Apache Spark는 성능 최적화를 위해 다양한 힌트를 제공합니다. 이 힌트들은 쿼리 실행을 최적화하는 데 사용되며, 주로 데이터 파티셔닝과 조인 전략에 활용됩니다. 각 힌트는 특정 시나리오에서 성능을 크게 향상시킬 수 있습니다.

---

## Partitioning

### COALESCE
`COALESCE`는 파티션 수를 줄이는 데 사용됩니다. 많은 파티션을 병합하여 성능 최적화를 도와줍니다.

```python
spark.sql("SELECT /*+ COALESCE(2) */ * FROM my_table").show()
```

```python
df.hint("COALESCE", 2).show()  # 2개의 파티션으로 병합
```

### REPARTITION
`REPARTITION`은 데이터를 지정된 수의 파티션으로 재분배하는 데 사용됩니다. 대규모 데이터셋에서 파티션 수를 늘려 병렬 처리 성능을 향상시킬 수 있습니다.

```python
spark.sql("SELECT /*+ REPARTITION(4) */ * FROM my_table").show()
```

```python
df.hint("REPARTITION", 4).show()  # 4개의 파티션으로 재분배
```

### REPARTITION_BY_RANGE
`REPARTITION_BY_RANGE`는 특정 컬럼을 기준으로 데이터를 범위별로 파티셔닝합니다. 이를 통해 쿼리 성능을 향상시킬 수 있습니다.

```python
spark.sql("""
  SELECT /*+ REPARTITION_BY_RANGE(3, column) */ * 
  FROM my_table
""").show()
```

### REBALANCE
`REBALANCE`는 데이터를 균등하게 분배하여 성능을 최적화하는 데 사용됩니다. 파티션 간 데이터 불균형이 있을 때 유용합니다.

```python
spark.sql("SELECT /*+ REBALANCE */ * FROM my_table").show()
```

```python
df.hint("REBALANCE").show()  # 데이터를 균등하게 재분배
```

---

## Join

### BROADCAST
`BROADCAST`는 작은 테이블을 각 노드에 복제하여 조인 성능을 최적화합니다.

```sql
spark.sql("""
  SELECT /*+ BROADCAST(small_table) */ * 
  FROM large_table JOIN small_table 
  ON large_table.id = small_table.id
""").show()
```

```python
df1.join(df2.hint("BROADCAST"), "id").show()  # df2를 broadcast하여 조인
```

### MERGE
`MERGE`는 정렬된 데이터를 기준으로 효율적인 조인을 수행하도록 돕습니다.

```python
spark.sql("""
  SELECT /*+ MERGE(small_table) */ * 
  FROM large_table JOIN small_table 
  ON large_table.id = small_table.id
""").show()
```

```python
df1.join(df2.hint("MERGE"), "id").show()  # 정렬된 상태로 병합
```

### SHUFFLE_HASH
`SHUFFLE_HASH`는 해시 기반으로 조인을 수행하도록 합니다. 대규모 데이터를 처리할 때 유리합니다.

```python
spark.sql("""
  SELECT /*+ SHUFFLE_HASH(small_table) */ * 
  FROM large_table JOIN small_table 
  ON large_table.id = small_table.id
""").show()
```

```python
df1.join(df2.hint("SHUFFLE_HASH"), "id").show()  # 해시 기반 조인 사용
```

### SHUFFLE_REPLICATE_NL
`SHUFFLE_REPLICATE_NL`은 중첩 루프 조인에서 작은 테이블을 복제하여 큰 테이블과 조인합니다. 복잡한 조인 연산에서 성능을 높입니다.

```python
spark.sql("""
  SELECT /*+ SHUFFLE_REPLICATE_NL(small_table) */ * 
  FROM large_table JOIN small_table 
  ON large_table.id = small_table.id
""").show()
```

```python
df1.join(df2.hint("SHUFFLE_REPLICATE_NL"), "id").show()  # 중복 데이터 처리 조인
```

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
