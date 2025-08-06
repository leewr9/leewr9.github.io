---
title: Distributed Variable
category: Spark
tag: [Spark]
---

> Apache Spark는 대규모 분산 처리 환경에서 각 작업 노드 간 데이터와 변수를 효율적으로 공유하고 처리 성능을 최적화하기 위해 다양한 변수를 제공합니다. 이러한 변수는 네트워크 오버헤드를 줄이고 안전한 데이터 집계를 지원하여 대규모 작업에서도 일관된 결과를 보장합니다.

---

## Closures

`Closures`는 드라이버에서 정의된 변수나 함수가 클러스터 내 `Task` 단위 작업에서 참조될 때 발생하는 개념입니다. 각 태스크는 독립적으로 실행되며, 드라이버에서 정의된 변수가 워커 노드의 태스크에서 사용될 수 있도록 전송됩니다.

- 드라이버에서 정의된 변수를 클러스터 내 작업에서 사용
- 불필요한 데이터 캡처는 성능 저하를 초래할 수 있음
- 각 태스크는 독립적으로 실행됨

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.master("local").appName("Closure Example with UDF").getOrCreate()

# Closures
multiplier = 10

def multiply(x):
    return x * multiplier

multiply_udf = udf(multiply, IntegerType())

df = spark.createDataFrame([(1,), (2,), (3,), (4,)], ["value"])

result_df = df.withColumn("result", multiply_udf(df["value"]))
result_df.show()
```

```bash
+-----+------+
|value|result|
+-----+------+
|    1|    10|
|    2|    20|
|    3|    30|
|    4|    40|
+-----+------+
```

---

## Broadcast Variables

`Broadcast Variables`는 데이터를 클러스터의 모든 `Worker`에 한 번만 전송하여 여러 작업에서 반복적으로 사용할 수 있게 해주는 변수입니다. 이를 통해 네트워크 비용을 절감하고 성능을 최적화할 수 있습니다.

- 데이터를 한 번만 전송하여 여러 작업에서 사용
- 네트워크 비용 절감
- 대규모 데이터셋을 처리할 때 성능 최적화

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.master("local").appName("Broadcast Example with UDF").getOrCreate()

# Broadcast Variables
broadcast_var = spark.sparkContext.broadcast([1, 2, 3, 4, 5])

def add_broadcast_sum(x):
    return x + sum(broadcast_var.value)

add_broadcast_sum_udf = udf(add_broadcast_sum, IntegerType())

df = spark.createDataFrame([(10,), (20,), (30,), (40,)], ["value"])

result_df = df.withColumn("result", add_broadcast_sum_udf(df["value"]))
result_df.show()
```

```bash
+-----+------+
|value|result|
+-----+------+
|   10|    25|
|   20|    35|
|   30|    45|
|   40|    55|
+-----+------+
```

---

## Accumulators

`Accumulators`는 값을 안전하게 누적할 수 있는 변수로, 주로 디버깅과 성능 분석에 사용됩니다. 값은 한 번에 하나의 작업에서만 수정되며, 작업 완료 후 드라이버에서 최종 값을 읽을 수 있습니다.

- 값 안전하게 누적
- 한 번에 하나의 작업만 수정
- 최종 값은 드라이버에서 읽음
- 작업 실패 시 재시도 시 누적값 중복 가능

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.master("local").appName("Accumulator Example with Global").getOrCreate()

# Accumulators
accum_even = spark.sparkContext.accumulator(0)
accum_sum = spark.sparkContext.accumulator(0)

def accumulate(x):
    if x % 2 == 0:
      accum_even.add(1)
    return x * 2

def accumulate_sum(x):
    global accum_sum
    accum_sum += x["value"]

accumulate_udf = udf(accumulate, IntegerType())

df = spark.createDataFrame([(1,), (2,), (3,), (4,)], ["value"])

df.withColumn("accumulated", accumulate_udf(df["value"])).show()
print("Accumulator even after processing:", accum_even.value)

df.foreach(accumulate_sum)
print("Accumulator sum after processing:", accum_sum.value)
```

```bash
+-----+-----------+
|value|accumulated|
+-----+-----------+
|    1|          2|
|    2|          4|
|    3|          6|
|    4|          8|
+-----+-----------+

Accumulator even after processing: 2
Accumulator sum after processing: 10
```

---

## References

- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
