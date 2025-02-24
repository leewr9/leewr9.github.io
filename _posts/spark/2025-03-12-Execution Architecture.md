---
title: Execution Architecture
category: Spark
tag: [Spark]
---

> Apache Spark는 대규모 데이터 처리에 특화된 분산 컴퓨팅 시스템입니다. Spark의 핵심은 데이터를 분산하여 처리하는 데 있으며, 효율적인 데이터 처리를 위해 여러 개념들이 유기적으로 작동합니다. 

---

## Execution Flow
[![](\assets\posts\{{ page.name }}\diagram.png)](\assets\posts\{{ page.name }}\diagram.png)

### Driver
Spark 애플리케이션이 실행될 때 가장 먼저 시작되는 것은 `Driver`이며, 애플리케이션의 중앙 제어자로써 전반적인 실행을 관리합니다.

- Job 생성 및 스케줄링: Driver는 사용자가 정의한 `Action`이 실행될 때 `Job`을 생성합니다.
- Stage 분할: `Job`을 여러 개의 `Stage`로 나누고, 각 `Stage`가 여러 개의 `Task`로 나뉘도록 분할합니다.
- Task 할당 및 실행 모니터링: 각 `Task`를 클러스터 내의 `Executor`에게 할당하고, 진행 상황을 모니터링합니다.
- 결과 반환: 작업이 완료되면 `Executor`에서 반환된 결과를 모은 후, 최종적으로 사용자에게 전달합니다.

### Cluster Manager
Spark는 다양한 `Cluster Manager`를 지원합니다. 클러스터 관리자는 클러스터에서 자원을 할당하고, `Executor`를 실행할 적절한 노드를 선택합니다. 
주요 Cluster Manager로는 `Standalone`, `YARN`, `Mesos`가 있습니다.

- 자원 관리: 클러스터의 모든 자원을 관리하고, 필요한 리소스를 Driver와 Executor에 할당합니다.
- 실행 계획 수립: Driver로부터 받은 실행 계획을 바탕으로 Executor를 배정하고, 작업을 분배합니다.

### Worker and Executor
`Worker`는 실제 작업을 수행하는 노드입니다. 각 Worker 노드는 `Executor`를 실행하는 프로세스를 포함하고 있으며, 이 Executor가 실제 데이터를 처리하고 연산을 수행합니다.

- 데이터 처리: Executor는 각 `Task`에 해당하는 데이터를 처리합니다.
- 결과 반환: 처리한 데이터를 `Driver`로 반환하여 최종 결과를 생성합니다.
- 메모리와 CPU 자원 관리: 각 `Executor`는 클러스터 내에서 병렬로 작업을 처리하며, 메모리와 CPU를 효율적으로 사용합니다.

---

## Execution Plan
[![](\assets\posts\{{ page.name }}\dag.png)](\assets\posts\{{ page.name }}\dag.png)

### Job
`Job`은 `Action`이 호출될 때 생성되며, Spark는 **DAG(Directed Acyclic Graph)**를 기반으로 실행 계획을 수립하고 실행합니다. 여러 개의 `Transformation`이 수행되더라도 즉시 실행되지 않으며, 최종적으로 Action이 호출될 때 하나의 Job이 생성됩니다.

- Action
  - `show()`, `count()`, `collect()`와 같은 연산으로, 데이터를 즉시 실행하고 결과를 반환하는 연산입니다. Action이 실행되면 Spark는 DAG를 평가하고, Job을 생성하여 클러스터에서 실행합니다.
- Transformation
  - `select()`, `groupBy()`와 같은 연산으로, 기존 데이터를 변환하는 연산입니다. `Lazy Execution`(지연 실행) 방식으로 동작하며, 즉시 실행되지 않고 DAG에 저장되었다가 Action이 호출될 때 한 번에 처리됩니다.

### Stage
`Stage`는 하나의 `Job`을 여러 개의 논리적 실행 단위로 나눈 것입니다. Stage는 주로 `Shuffling`이 발생하는 지점에서 나뉩니다. 
`Shuffling`은 데이터의 재배치를 필요로 하는 연산이 있을 때 발생하며, 이로 인해 새로운 Stage가 생성됩니다.

- Narrow Dependency
  - `select()`, `filter()`와 같은 연산은 데이터가 한 파티션 내에서 처리되기 때문에 `Shuffling`이 필요하지 않으며, 같은 `Stage` 내에서 실행됩니다.
- Wide Dependency
  - `groupBy()`, `join()`와 같은 연산은 데이터가 여러 파티션으로 이동해야 하므로 `Shuffling`이 발생하여 새로운 Stage가 생성되며, 데이터 이동이 필요할 때마다 `Stage`가 나뉘어 실행됩니다.

### Task
`Task`는 `Stage`를 구성하는 가장 작은 실행 단위로, 데이터의 파티션 단위로 실행되며, 각 Task는 하나의 데이터 파티션을 처리하고, 
`Executor`는 여러 Task를 병렬로 실행하여 빠른 연산을 수행합니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ExecutionPlanExample").getOrCreate()

data = [("Alice", "HR", 5000), 
        ("Bob", "IT", 7000), 
        ("Charlie", "HR", 5500),
        ("David", "IT", 7200),
        ("Eve", "Finance", 6500)]

columns = ["name", "department", "salary"]

df = spark.createDataFrame(data, columns)

# Stage 1
selected_df = df.select("department", "salary")  # Narrow Dependency → Shuffling X
grouped_df = selected_df.groupBy("department").avg("salary")  # Wide Dependency → Shuffling O, Stage 2

# Action -> Job
result = grouped_df.show()
```

```bash
+----------+-----------+
|department|avg(salary)|
+----------+-----------+
|        HR|     5250.0|
|        IT|     7100.0|
|   Finance|     6500.0|
+----------+-----------+
```

- Job 생성: `show()`가 호출되면서 Job이 생성됩니다.
- Stage 1: `select()`는 `Narrow Dependency`이므로 같은 Stage에서 실행됩니다.
- Stage 2: `groupBy()`는 `Wide Dependency`이므로 `Shuffling`이 발생하고 새로운 Stage가 생성됩니다.
- Task 실행: 각 Stage는 데이터의 파티션 개수만큼 Task로 나뉘어 병렬 실행됩니다.

---

## Partition and Shuffling
`Partition`은 데이터를 작은 단위로 나누어 병렬 처리의 기본 단위가 되며, 각 `Partition`은 하나의 `Task`에 해당하고, `Shuffling`은 데이터를 파티션 간에 재배치하는 작업으로 주로 `Wide Dependency` 연산에서 발생하며 성능에 영향을 미쳐 이를 최소화하는 것이 중요합니다.

- `spark.sql.shuffle.partitions`: 이 설정은 Shuffling 발생 시 생성되는 기본 파티션 수를 결정합니다.
- `spark.default.parallelism`: 기본적으로 RDD에서 연산을 수행할 때 사용하는 파티션 수를 설정합니다.
```python
spark = SparkSession.builder \
    .appName("MySparkSession") \
    .config("spark.sql.shuffle.partitions", "200") \
    .config("spark.default.parallelism", "100") \
    .getOrCreate()
```

### Repartitioning
- `repartition()`: 데이터를 특정 파티션 수로 다시 나누는 작업입니다. 전체 데이터를 셔플하여 새로운 파티션 수로 재분배합니다.
- `coalesce()`: 셔플 없이 데이터를 병합하여 파티션 수를 줄입니다. 주로 작업을 줄이거나 파티션을 축소할 때 사용됩니다.
```python
df = df.repartition(10)  # 10개의 파티션으로 재분배
df = df.coalesce(3)      # 3개의 파티션으로 합침
```

### Optimization
- `Broadcast Join`: 작은 데이터셋을 모든 Executor에 배포하여 Shuffling을 줄이는 방법입니다.
  ```python
  small_df = spark.read.csv("small_data.csv", header=True, inferSchema=True)
  large_df = spark.read.csv("large_data.csv", header=True, inferSchema=True)

  result = large_df.join(broadcast(small_df), "key").show()
  ```
- `SparkSQL`:복잡한 연산은 SQL을 사용하여 더 효율적으로 처리할 수 있으며, groupBy, join 같은 연산도 최적화된 실행 계획을 통해 처리됩니다.
  ```python
  small_df = spark.read.csv("small_data.csv", header=True, inferSchema=True)
  large_df = spark.read.csv("large_data.csv", header=True, inferSchema=True)
  
  # DataFrame을 임시 테이블로 등록
  small_df.createOrReplaceTempView("small_data")
  large_df.createOrReplaceTempView("large_data")
  
  result = spark.sql("""
      SELECT *
      FROM large_data AS l
      LEFT JOIN small_data AS s
      ON l.key = s.key
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
