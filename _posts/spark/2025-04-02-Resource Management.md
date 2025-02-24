---
title: Resource Management
category: Spark
tag: [Spark]
---

> Apache Spark에서는 클러스터 내 리소스를 효율적으로 관리하여 작업에 필요한 자원을 동적으로 또는 고정적으로 할당하고, 여러 작업이 동시에 실행될 때 리소스를 공평하게 분배합니다. 이를 통해 Spark는 작업 간 리소스 충돌을 최소화하고, 시스템의 성능을 최적화하며, 작업이 원활하게 실행될 수 있도록 합니다

---

## Resource Allocation
`Resource Allocation`은 Spark 클러스터에서 작업을 실행하기 위해 필요한 `CPU`, `Memory` 등의 리소스를 분배하는 과정을 의미합니다.

### Static
`Static Allocation`은 클러스터에 할당된 리소스를 고정적으로 설정하는 방식입니다. 작업을 시작할 때 필요한 리소스 양을 미리 정하고, 이 리소스를 고정적으로 사용합니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Static Allocation Example") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.cores", "2") \
    .getOrCreate()

df = spark.read.csv("your_dataset.csv", header=True, inferSchema=True)
df.show()
```

- `spark.executor.memory`: 각 Executor가 사용할 메모리 크기
- `spark.executor.cores`: 각 Executor가 사용할 CPU 코어 수

### Dynamic
`Dynamic Allocation`은 작업의 실행 중에 필요한 리소스를 실시간으로 할당하는 방식입니다. 이 방식은 클러스터 리소스를 보다 유연하게 관리할 수 있도록 도와주며, 작업의 부하에 따라 자동으로 리소스를 조정합니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Dynamic Allocation Example") \
    .config("spark.dynamicAllocation.enabled", "true") \
    .config("spark.dynamicAllocation.minExecutors", "1") \
    .config("spark.dynamicAllocation.maxExecutors", "10") \
    .getOrCreate()

df = spark.read.csv("your_dataset.csv", header=True, inferSchema=True)
df.show()
```

- `spark.dynamicAllocation.enabled`: 동적 할당 활성화 여부
- `spark.dynamicAllocation.minExecutors`: 최소 Executor 수
- `spark.dynamicAllocation.maxExecutors`: 최대 Executor 수

### Option
Spark에서는 자원 할당에 다양한 옵션을 지원하여, 작업의 요구사항에 맞게 리소스를 최적화할 수 있습니다.

```python
spark.conf.set("spark.executor.memory", "4g")
```

| 옵션 | 설명 | 기본값 |
|-|-|-|
| spark.executor.memory | 각 실행자가 사용할 메모리 크기 | 1g |
| spark.executor.cores | 각 실행자가 사용할 CPU 코어 수 | 1 |
| spark.executor.heartbeatInterval | 실행자 상태를 확인하는 간격 | 10s |
| spark.driver.memory | 드라이버가 사용할 메모리 크기 | 1g |
| spark.driver.cores | 드라이버가 사용할 CPU 코어 수 | 1 |
| spark.dynamicAllocation.enabled | 동적 할당 활성화 여부 | false |
| spark.dynamicAllocation.minExecutors | 동적 할당에서 최소 실행자 수 | 0 |
| spark.dynamicAllocation.maxExecutors | 동적 할당에서 최대 실행자 수 | infinity |
| spark.dynamicAllocation.initialExecutors | 동적 할당 시작 시 초기 실행자 수 | minExecutors |
| spark.scheduler.mode | 스케줄러 모드 설정 (FIFO, FAIR) | FIFO |
| spark.memory.fraction | Spark에서 메모리를 사용하는 비율 | 0.6 |
| spark.memory.storageFraction | 스토리지에 사용하는 메모리 비율 | 0.5 |
| spark.memory.offHeap.enabled | off-heap 메모리 할당 활성화 여부 | false |
| spark.memory.offHeap.size | 할당할 off-heap 메모리 크기 | 0 |

---

## Spark Scheduler
`Spark Scheduler`는 하나의 `Spark Application` 내에서 `Job`에 리소스를 할당하는 역할을 합니다. 여러 작업이 동시에 실행될 때 리소스를 어떻게 분배할지 결정하며, 작업의 실행 순서도 관리합니다.

### FIFO
**FIFO(First In, First Out)** 스케쥴러 모드는 작업을 선입선출 방식으로 처리합니다. 즉, 먼저 제출된 작업이 먼저 실행됩니다. 이 방식은 구현이 간단하고 직관적이며, 우선순위나 리소스 요구 사항을 고려하지 않고 순차적으로 작업을 처리합니다.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FIFO Scheduler Example") \
    .config("spark.scheduler.mode", "FIFO") \
    .getOrCreate()

df = spark.read.csv("your_dataset.csv", header=True, inferSchema=True)
df.show()
```

### FAIR
`FAIR` 스케쥴러 모드는 Spark에서 여러 작업이 동시에 실행될 때 각 작업에 리소스를 공평하게 할당하는 방식입니다. 각 작업은 `Pool`에 할당된 리소스를 기준으로 실행되며, 리소스 할당 정책을 정의하는 `XML` 파일을 작성하여 Spark 설정에서 참조해야 합니다. 

```xml
<!-- fairscheduler.xml -->

<?xml version="1.0" encoding="UTF-8"?>
<spark-scheduler>
  <pool name="high-priority">
    <minShare>1</minShare>      <!-- 최소 리소스 비율: 1 -->
    <weight>2</weight>          <!-- 가중치: 2 (high-priority 풀은 더 많은 리소스를 할당받음) -->
  </pool>

  <pool name="low-priority">
    <minShare>0</minShare>      <!-- 최소 리소스 비율: 0 -->
    <weight>1</weight>          <!-- 가중치: 1 (low-priority 풀은 상대적으로 적은 리소스를 할당받음) -->
  </pool>
</spark-scheduler>
```

- `minShare`: 풀에 할당할 최소 리소스 비율을 설정 (값이 클수록 해당 풀에 더 많은 리소스 할당)
- `weight`: 풀의 가중치 설정 (가중치가 클수록 상대적으로 더 많은 리소스 할당)

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Pool Selection Example") \
    .config("spark.scheduler.mode", "FAIR") \
    .config("spark.scheduler.allocation.file", "path/to/fairscheduler.xml") \
    .getOrCreate()

spark.sparkContext.setLocalProperty("spark.scheduler.pool", "high-priority")

df = spark.read.csv("your_dataset.csv", header=True, inferSchema=True)
df.show()
```

- `spark.scheduler.mode`: 스케줄러 모드를 설정
- `spark.scheduler.allocation.file`: fairscheduler.xml 파일 경로 지정
- `spark.scheduler.pool`: 특정 작업에 대해 실행할 풀 지정

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
