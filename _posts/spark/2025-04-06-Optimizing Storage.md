---
title: Optimizing Storage
category: Spark
tag: [Spark SQL, Spark]
---

> Apache Spark는 대규모 데이터 처리 성능을 극대화하기 위해 데이터를 메모리나 디스크에 캐싱하고 퍼시스팅하는 기능을 제공하는 분산 처리 시스템으로, 반복적인 계산을 최적화하고 시스템 자원을 효율적으로 사용하여 빠르고 확장 가능한 데이터 분석을 가능하게 합니다.

---

## RDD and DataFrame
Spark에서 `RDD`나 `DataFrame`을 캐시하거나 퍼시스트하는 방법은 데이터 처리 속도를 최적화하는 데 중요한 역할을 합니다. 자주 사용되는 RDD나 DataFrame을 캐시하거나 퍼시스트하면, 반복 작업 시 데이터를 재계산하지 않고 빠르게 액세스할 수 있습니다.

```python
from pyspark.sql import SparkSession
from pyspark.storagelevel import StorageLevel

spark = SparkSession.builder.master("local").appName("Persist Example").getOrCreate()

# RDD persist
rdd = spark.sparkContext.range(0, 100, 1, 5).setName("rdd")
rdd.persist(StorageLevel.MEMORY_ONLY)
rdd.count()

data = [(1, "andy"), (2, "bob"), (2, "andy")]
df = spark.createDataFrame(data, ["count", "name"])

# DataFrame persist
df.persist(StorageLevel.DISK_ONLY)
df.count()
```

[![](\assets\posts\2025-04-06-Optimizing Storage.md\storage.png)](\assets\posts\2025-04-06-Optimizing Storage.md\storage.png)

### cache()
`cache()`는 RDD나 DataFrame을 메모리에 캐시하여, 반복적인 작업에서 빠른 접근을 가능하며, 액션이 실행될 때 캐시가 실제로 이루어집니다.

```python
df.cache()
```

### persist()
`persist()`는 RDD나 DataFrame을 메모리와 디스크에 저장할 수 있도록 설정합니다. `StorageLevel`을 사용해 저장 방식을 세부적으로 조정할 수 있습니다.

```python
from pyspark import StorageLevel

df.persist(StorageLevel.MEMORY_AND_DISK)
```

### unpersist()
`unpersist()`는 이미 캐시된 RDD나 DataFrame의 데이터를 메모리와 디스크에서 제거하는 방법입니다. 이는 더 이상 해당 데이터가 필요 없을 때 사용하여 자원을 해제하고, 메모리 및 디스크 공간을 반환합니다.

```python
df.unpersist()
```

---

## Table
Spark의 `Catalog`를 사용하면 테이블을 관리하고, 캐시 작업을 수행할 수 있습니다. 테이블을 캐시하면 이후 쿼리에서 성능이 최적화됩니다. 또한, `Spark SQL`을 사용하여 동일한 작업을 SQL로 실행할 수도 있습니다.

### cacheTable()
`cacheTable()`은 지정된 테이블을 메모리에 캐시하는 메서드입니다. 이 작업을 통해 이후 해당 테이블에 대한 쿼리 성능을 최적화할 수 있습니다. 

```python
from pyspark import StorageLevel

spark.catalog.cacheTable("my_table", StorageLevel.MEMORY_AND_DISK)

spark.sql("CACHE TABLE my_table OPTIONS('storageLevel' 'MEMORY_AND_DISK')") # Spark SQL
spark.sql("CACHE LAZY TABLE my_table") # Spark SQL Lazy Execution
```

### uncacheTable()
`uncacheTable()`은 캐시된 테이블을 메모리에서 제거하는 메서드입니다. 이를 사용하면 더 이상 캐시된 데이터를 사용하지 않도록 할 수 있습니다.

```python
spark.catalog.uncacheTable("my_table")

spark.sql("UNCACHE TABLE my_table") # Spark SQL
```

### isCached()
`isCached()`는 지정된 테이블이 현재 캐시되어 있는지를 확인하는 메서드입니다. 이 메서드는 테이블이 캐시되어 있는지 여부를 `Boolean` 값으로 반환합니다.

```python
spark.catalog.isCached("my_table")
```

---

## StorageLevel
`StorageLevel`은 데이터를 메모리와 디스크에 저장하는 방식을 세밀하게 제어할 수 있는 옵션을 제공합니다. 기본적으로 제공되는 여러 StorageLevel 외에도 사용자가 필요에 맞게 커스터마이징할 수 있습니다.

- `MEMORY_ONLY`: 메모리에만 데이터를 저장합니다. 메모리가 부족할 경우 해당 데이터는 저장되지 않거나 재계산됩니다.
- `MEMORY_AND_DISK`: 데이터를 메모리에 저장하고, 메모리가 부족하면 디스크에 저장합니다.
- `DISK_ONLY`: 데이터를 디스크에만 저장합니다. 메모리에는 저장되지 않습니다.

### Custom
```python
from pyspark import StorageLevel

# 메모리와 디스크에 직렬화된 방식으로 저장
custom_storage_level = StorageLevel(useDisk=True, 
                                    useMemory=True, 
                                    useOffHeap=False, 
                                    deserialized=False, 
                                    replication=1)
df.persist(custom_storage_level)
```
- `useDisk`: 데이터를 디스크에 저장할지 여부
- `useMemory`: 데이터를 메모리에 저장할지 여부
- `useOffHeap`: 오프힙(Off-Heap) 메모리에 저장할지 여부
- `deserialized`: 데이터를 비직렬화된 형식으로 저장할지 여부
- `replication`: 데이터 복제 수 

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
