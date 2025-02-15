---
title:  User Defined Functions
category: Spark
tag: [UDAF, UDF, Spark]
---

> PySpark는 데이터 처리와 분석을 위해 다양한 방식으로 사용자 정의 함수를 활용할 수 있습니다. 그 중 UDF(User Defined Function)와 Pandas UDF는 데이터 변환 및 집계 작업을 위해 자주 사용됩니다.

---

## UDF 
**UDF(User Defined Function)**는 PySpark에서 사용자 정의 함수를 사용할 수 있도록 하는 기능입니다. Spark에서 기본 제공하는 함수 외에, 복잡한 로직이나 비즈니스 요구사항에 맞는 커스텀 함수를 작성할 수 있습니다.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import pandas as pd

spark = SparkSession.builder.appName("UDF Example").getOrCreate()

data = [("Alice", 34), ("Bob", 45), ("Cathy", 23)]
df = spark.createDataFrame(data, ["Name", "Age"])

# UDF 작성
def categorize_age(age):
    if age >= 30:
        return "Senior"
    else:
        return "Junior"

# UDF 등록
age_category_udf = udf(categorize_age, StringType())

# DataFrame에 적용
df = df.withColumn("Category", age_category_udf(df["Age"]))
df.show()
```

```bash
+-----+---+--------+
| Name|Age|Category|
+-----+---+--------+
|Alice| 34|  Senior|
|  Bob| 45|  Senior|
|Cathy| 23|  Junior|
+-----+---+--------+
```

- 단일 값 처리: UDF는 각 행마다 처리할 수 있는 단일 값을 입력으로 받습니다.
- 성능 문제: UDF는 Spark의 내부 최적화를 사용하지 않기 때문에 성능상 비효율적일 수 있습니다.

---

## Pandas UDF
`pandas_udf`는 Pandas 라이브러리를 활용한 UDF입니다.벡터화된 방식으로 데이터 처리 속도가 더 빠르며, 대용량 데이터를 처리하는 데 적합합니다. Pandas UDF는 `pandas.Series`를 입력으로 받고 `pandas.Series`를 반환합니다.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import StringType
import pandas as pd

spark = SparkSession.builder.appName("Pandas UDF Example").getOrCreate()

data = [("Alice", 34), ("Bob", 45), ("Cathy", 23)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Pandas UDF 정의
@pandas_udf(StringType())
def categorize_age_pandas(s: pd.Series) -> pd.Series:
    return s.apply(lambda age: "Senior" if age >= 30 else "Junior")

# DataFrame에 적용
df = df.withColumn("Category", categorize_age_pandas(df["Age"]))
df.show()
```

```bash
+-----+---+--------+
| Name|Age|Category|
+-----+---+--------+
|Alice| 34|  Senior|
|  Bob| 45|  Senior|
|Cathy| 23|  Junior|
+-----+---+--------+
```

- 벡터화된 처리: Pandas UDF는 `pandas.Series`를 입력으로 받고 `pandas.Series`를 반환하므로, 벡터화된 방식으로 데이터를 처리할 수 있습니다.
- 성능 향상: Pandas UDF는 Spark의 분산 처리와 Pandas의 벡터화된 연산을 결합하여 성능이 향상됩니다.
- 집계 작업에 적합: Pandas UDF는 집계 작업에서 매우 효과적입니다.

### Aggregate
`pandas_udf`는 집계 함수에서도 유용하게 사용할 수 있습니다. 특히, `groupBy`와 결합할 때 효율적으로 대규모 데이터를 처리할 수 있습니다.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import LongType
import pandas as pd

spark = SparkSession.builder.appName("Aggregate pandas UDF").getOrCreate()

data = [(1, "Alice", 10), (2, "Bob", 15), (1, "Alice", 30), (2, "Bob", 25)]
columns = ["ID", "Name", "Amount"]
df = spark.createDataFrame(data, columns)

# pandas_udf 정의: 집계 함수 (Sum)
@pandas_udf(LongType())
def sum_amount(s: pd.Series) -> int:
    return s.sum()

# GroupBy와 pandas_udf 사용하여 집계
result = df.groupBy("ID").agg(sum_amount(df["Amount"]).alias("Total_Amount"))

result.show()
```

```bash
+---+------------+
| ID|Total_Amount|
+---+------------+
|  1|          40|
|  2|          40|
+---+------------+
```

---

## Spark SQL UDF
UDF와 Pandas UDF는 `Spark SQL`에서 직접 사용할 수 있도록 등록할 수 있습니다. 이를 통해 SQL 쿼리 내에서도 정의한 사용자 함수들을 사용할 수 있습니다.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import pandas as pd

spark = SparkSession.builder.appName("UDF Spark SQL Example").getOrCreate()

data = [("Alice", 34), ("Bob", 45), ("Cathy", 23)]
df = spark.createDataFrame(data, ["Name", "Age"])

# UDF 작성
def categorize_age(age):
    if age >= 30:
        return "Senior"
    else:
        return "Junior"

# UDF 등록
spark.udf.register("categorize_age", categorize_age, StringType())

# SQL 쿼리 사용
df.createOrReplaceTempView("people")
spark.sql("SELECT Age, categorize_age(Age) FROM people").show()
```

```bash
+---+-------------------+
|Age|categorize_age(Age)|
+---+-------------------+
| 25|             Junior|
| 35|             Senior|
+---+-------------------+
```

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
