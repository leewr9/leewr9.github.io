---
title: Data Retrieval
category: Spark
tag: [Spark SQL, Spark]
---

> Spark SQL에서는 데이터를 다룰 때 정렬이나 파티셔닝 전략을 선택할 수 있는 여러 키워드를 제공합니다. 이러한 키워드들은 결과 데이터의 정렬 순서, 병렬 처리 방식, 그리고 전체 쿼리 성능에 직접적인 영향을 미치기 때문에, 각 키워드의 특성과 동작 방식을 정확하게 이해하고 적절히 활용하는 것이 매우 중요합니다.

---

## Sorting

### ORDER BY

`ORDER BY`는 전체 데이터를 하나의 파티션으로 모은 뒤 정렬하는 방식입니다. 이는 전역 정렬을 의미하며, 가장 직관적이지만 병렬 처리를 하지 못하기 때문에 성능상 제약이 가장 큽니다. 데이터 양이 많을 경우 `OOM`이 발생할 수 있습니다. 그럼에도 불구하고 결과 전체의 순서를 명확히 보장해야 할 때 사용합니다.

```python
spark.sql("SELECT * FROM my_table ORDER BY col DESC").show()
```

```python
df.orderBy("col", ascending=False)
```

### SORT BY

`SORT BY`는 각 파티션 내부에서만 정렬을 수행합니다. 전체 정렬 순서를 보장하지 않지만, 파티션 단위로 데이터를 병렬로 정렬할 수 있어 `ORDER BY`보다 훨씬 효율적입니다.

```python
spark.sql("SELECT * FROM my_table SORT BY col").show()
```

```python
df.sortWithinPartitions("col").show()
```

---

## Partitioning

### DISTRIBUTE BY

`DISTRIBUTE BY`는 지정한 컬럼 값을 기준으로 데이터를 다양한 파티션에 나누는 작업을 수행합니다. 이때 같은 키를 가진 데이터는 반드시 같은 파티션으로 이동하게 됩니다. 하지만 정렬은 하지 않기 때문에, 그 안에서의 순서는 보장되지 않습니다.

```python
spark.sql("SELECT * FROM my_table DISTRIBUTE BY col").show()
```

```python
df.repartition("col").show()
```

### CLUSTER BY

`CLUSTER BY`는 `DISTRIBUTE BY`와 `SORT BY`를 하나의 구문으로 결합한 키워드입니다. 지정한 컬럼을 기준으로 데이터를 파티셔닝하고, 각 파티션 내부에서는 해당 컬럼 기준으로 정렬까지 수행합니다. 내부적으로는 `DISTRIBUTE BY col SORT BY col`과 동일하게 작동합니다.

```python
spark.sql("SELECT * FROM my_table CLUSTER BY col").show()
spark.sql("SELECT * FROM my_table DISTRIBUTE BY col SORT BY col").show()
```

```python
df.repartition("col").sortWithinPartitions("col").show()
```

---

## References

- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
