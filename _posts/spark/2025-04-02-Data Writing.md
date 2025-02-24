---
title: Data Writing
category: Spark
tag: [Spark SQL, Spark]
---

> Apache Spark는 데이터를 다양한 형식과 방법으로 저장할 수 있는 유연성을 제공합니다. Spark에서 데이터를 저장하는 주요 방식은 DataFrame API를 통해 이루어지며, 다양한 파일 포맷뿐만 아니라, 파티셔닝, 압축, 조인 최적화 등 다양한 옵션을 설정할 수 있습니다.

---

## Write Option
### format
`format`은 데이터 저장 시 파일 형식을 지정할 수 있는 옵션입니다. `parquet`, `csv`, `json` 등을 지정할 수 있습니다.

```python
df.write.format("parquet").save("/path/to/output")
df.write.format("csv").save("/path/to/output")
df.write.format("json").save("/path/to/output")
```

### mode
`mode`는 데이터를 저장할 때 기존 데이터를 어떻게 처리할지 지정할 수 있는 옵션입니다.
- `append`: 기존 데이터를 덮어쓰지 않고 추가
- `overwrite`: 기존 데이터를 덮어쓰고 새 데이터 저장
- `ignore`: 기존 데이터가 있을 경우 아무 작업도 하지 않음
- `error`: 파일이 이미 존재하면 오류 발생 (기본값)

```python
df.write.mode("overwrite").parquet("/path/to/output")
df.write.mode("append").json("/path/to/output")
```

### compression
`compression`은 데이터를 저장할 때 압축 방식을 지정할 수 있습니다. 지원되는 압축 방식에는 `gzip`, `snappy`, `bzip2`, `lz4`, `deflate`, `zstd` 등이 있습니다.

```python
df.write.option("compression", "bzip2").json("/path/to/output")
```

```plaintext
/path/to/output/part-00000-file_00000.json.bz2
```

### saveAsTable
`saveAsTable`은 DataFrame을 `Hive` 테이블로 저장하는 메소드입니다. 이를 통해 Spark SQL에서 사용할 수 있는 Hive 테이블을 생성하거나 업데이트할 수 있습니다.

```python
df.write.saveAsTable("my_hive_table")
```

```plaintext
/spark-warehouse/my_hive_table/part-00000-file_00000.snappy.parquet
```

---

## Optimization
### partitionBy
`partitionBy`는 특정 컬럼을 기준으로 데이터를 파티셔닝하여 저장합니다. 이렇게 저장된 데이터는 해당 컬럼에 따라 디렉터리가 나뉘어 저장됩니다. 이 방식은 쿼리 성능을 최적화하는 데 유용하며, 특정 컬럼을 기준으로 데이터를 나누어 효율적인 읽기 작업을 할 수 있습니다.

```python
df.write.partitionBy("year", "month").parquet("/path/to/output")
```

```plaintext
/path/to/output/year=2025/month=01/
/path/to/output/year=2025/month=02/
/path/to/output/year=2025/month=03/
/path/to/output/year=2025/month=04/
```

### bucketBy
`bucketBy`는 데이터를 해시 기반으로 버킷으로 나누어 테이블을 생성합니다. 이는 조인 성능 최적화에 유용합니다. 동일한 값을 가진 데이터가 같은 버킷에 배치되므로, 조인 시 같은 버킷끼리만 비교하게 되어 성능이 향상됩니다. 

```python
df.repartition(3).write.bucketBy(2, "id").saveAsTable("bucketed_table")
```

```plaintext
/spark-warehouse/bucketed_table/part-00000-file_00000.snappy.parquet
/spark-warehouse/bucketed_table/part-00000-file_00001.snappy.parquet
/spark-warehouse/bucketed_table/part-00001-file_00000.snappy.parquet
/spark-warehouse/bucketed_table/part-00001-file_00001.snappy.parquet
/spark-warehouse/bucketed_table/part-00002-file_00000.snappy.parquet
/spark-warehouse/bucketed_table/part-00002-file_00001.snappy.parquet
```

#### sortBy
`sortBy`는 `bucketBy`와 함께 사용하여 각 버킷 내 데이터를 지정한 컬럼 기준으로 정렬합니다. 이렇게 저장하면 조인 성능과 쿼리 최적화에 도움이 됩니다.

```python
df.write.sortBy("age").bucketBy(2, "id").saveAsTable("bucket_sorted_table")
```

---

## Spark SQL
`Spark SQL`에서 `df.write`와 유사한 방식으로 SQL 쿼리를 통해 데이터를 저장할 수 있습니다. 이를 통해 테이블 생성, 데이터 삽입, 파티셔닝 및 클러스터링 등을 수행할 수 있습니다.

### PARTITIONED BY
PARTITIONED BY는 SQL 쿼리에서 데이터를 파티셔닝하여 저장하는 방법입니다. 이를 사용하면 특정 컬럼을 기준으로 데이터를 나누어 저장할 수 있으며, 이는 `df.write.partitionBy`와 유사한 방식으로 동작합니다.

```python
spark.sql("""
    CREATE TABLE my_table (
        id INT,
        name STRING,
        year INT
    )
    USING PARQUET
    PARTITIONED BY (year)
""")
```

### CLUSTERED BY 
`CLUSTERED BY`는 데이터를 해시 기반으로 버킷으로 나누어 저장하는 방법입니다. 이는 데이터를 버킷 단위로 분할하여 저장하며, 이는 `df.write.bucketBy`와 유사한 방식으로 동작합니다.

```python
spark.sql("""
    CREATE TABLE clustered_table (
        id INT,
        name STRING
    )
    USING PARQUET
    CLUSTERED BY (id) INTO 2 BUCKETS
""")
```

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
