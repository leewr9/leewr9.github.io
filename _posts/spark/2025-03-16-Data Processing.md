---
title: Data Processing
category: Spark
tag: [RDD, DataFrame, Spark SQL, Spark]
---

> Apache Spark는 대규모 데이터를 분산 처리할 수 있는 강력한 엔진으로, 다양한 방식으로 데이터를 처리할 수 있습니다. 가장 대표적인 데이터 처리 방법은 RDD(Resilient Distributed Dataset), DataFrame, Spark SQL입니다. 각 방식은 사용자가 데이터에 접근하고 변형하는 방식에서 차이를 보이지만, 모두 Spark의 강력한 분산 처리 기능을 활용합니다.

---

## Spark Core
`Spark Core`는 Spark의 핵심 엔진으로, 분산 데이터 처리를 위한 기반을 제공하며, 작업 스케줄링, 자원 관리, 장애 복구 등의 기본 기능을 담당합니다. `RDD`, `DataFrame`, `Spark SQL`을 포함한 다양한 기능들은 Spark Core의 분산 처리 및 최적화된 실행 환경을 활용하여 동작합니다.

[![](\assets\posts\2025-03-16-Data Processing.md\core.png)](\assets\posts\2025-03-16-Data Processing.md\core.png)

### RDD 
**RDD(Resilient Distributed Dataset)**는 Spark의 기본 데이터 구조로, 불변의 분산 객체입니다. `RDD`는 고급 연산을 지원하며, 데이터에 대한 상세한 제어가 필요할 때 유용합니다. 예를 들어, 복잡한 변환을 직접 구현하고자 할 때 사용합니다.

```python
from pyspark import SparkContext

sc = SparkContext("local", "RDD Example")

# RDD 생성
data = [("Alice", 34), ("Bob", 45), ("Cathy", 23)]
rdd = sc.parallelize(data)

# RDD 변환
rdd_filtered = rdd.filter(lambda x: x[1] > 30)
rdd_collect = rdd_filtered.collect()

for rdd_data in rdd_collect:
    print(rdd_data)
```

```bash
('Alice', 34)
('Bob', 45)
```

RDD는 데이터 변환 시 좀 더 세밀한 제어를 할 수 있지만, 그만큼 코드가 길어지고 복잡해질 수 있습니다. 
또한, `DataFrame`이나 `Spark SQL`을 사용한 방법에 비해 성능 최적화가 부족할 수 있습니다.

### DataFrame
`DataFrame`은 `RDD`를 추상화한 구조로, 행과 열로 구성된 데이터 테이블입니다. SQL 쿼리를 사용하듯 데이터에 접근할 수 있어 더 직관적이고, 
성능 최적화가 내장되어 있어 대용량 데이터 처리에 유리합니다. 

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataFrame Example").getOrCreate()

# DataFrame 생성
data = [("Alice", 34), ("Bob", 45), ("Cathy", 23)]
df = spark.createDataFrame(data, ["Name", "Age"])

# DataFrame 변환
df_filtered = df.where(df.Age > 30)
df_filtered.show()
```

```bash
+-----+---+
| Name|Age|
+-----+---+
|Alice| 34|
|  Bob| 45|
+-----+---+
```

`DataFrame`은 `RDD`보다 더 간단하고 직관적이며, 성능 최적화가 내장되어 있기 때문에 많은 Spark 사용자에게 선호됩니다. 
SQL 쿼리처럼 테이블을 다루는 방식은 데이터 처리 과정을 단순화시켜 줍니다.

### Spark SQL
`Spark SQL`은 SQL 쿼리를 사용하여 데이터를 처리할 수 있는 방법입니다. `DataFrame`을 기반으로 하며, SQL을 사용하여 다양한 데이터 변환을 수행할 수 있습니다. 
SQL을 사용할 경우, `RDBMS`에 익숙한 사용자가 쉽게 적응할 수 있습니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark SQL Example").getOrCreate()

data = [("Alice", 34), ("Bob", 45), ("Cathy", 23)]
df = spark.createDataFrame(data, ["Name", "Age"])

# 임시 뷰 등록
df.createOrReplaceTempView("people")

# SQL 쿼리 실행
result = spark.sql("SELECT * FROM people WHERE Age > 30")
result.show()
```

```bash
+-----+---+
| Name|Age|
+-----+---+
|Alice| 34|
|  Bob| 45|
+-----+---+
```

`Spark SQL`은 `SQL`을 선호하는 사용자에게 익숙한 인터페이스를 제공하며, 복잡한 데이터 변환을 더 간단한 쿼리로 처리할 수 있습니다. 
SQL을 사용하면 데이터에 대한 직관적인 접근이 가능하며, `DataFrame`과 동일한 최적화 기능을 활용할 수 있습니다.

---

## Comparison 

| 특성 | RDD | DataFrame | Spark SQL |
|-|-|-|-|
| **표현력** | 저수준 API, 복잡한 처리 가능 | 고수준 API, 직관적인 사용 가능| SQL 쿼리로 직관적이고 쉽게 사용 가능  |
| **최적화** | 수동으로 최적화 필요 | Catalyst Optimizer 자동 최적화| Catalyst Optimizer 자동 최적화 |
| **성능** | 성능 최적화 어려움 | 자동 최적화로 성능 향상 가능 | 자동 최적화, 셔플링 최적화 가능 |
| **셔플링** | 많은 셔플링 발생 가능 | 셔플링을 최소화하도록 최적화 | 셔플링을 최소화하도록 최적화 |
| **데이터 처리** | 복잡한 데이터 처리 가능 | DataFrame 기반으로 처리 가능 | SQL 쿼리로 간편하게 처리 가능 |

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
