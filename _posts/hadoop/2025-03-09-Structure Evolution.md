---
title: Structure Evolution
category: Hadoop
tag: [Hadoop]
---

> Hadoop은 분산 데이터 처리 플랫폼으로, 데이터 처리의 혁신을 이끌며 큰 인기를 얻었습니다. Hadoop의 발전은 크게 Hadoop 1.0과 Hadoop 2.0으로 나눌 수 있으며, 이 두 버전의 구조적 차이는 리소스 관리, 작업 실행 모델, 확장성 측면에서 많은 변화를 가져왔습니다. 

---

## Hadoop 1.0

Hadoop은 대규모 데이터를 분산 처리할 수 있도록 설계된 오픈 소스 프레임워크입니다. `Hadoop 1.0`은 그 초기 버전으로, `MapReduce`와 `HDFS` 두 가지 주요 구성 요소로 구성되어 있습니다.

### HDFS

[![](\assets\posts\{{ page.name }}\hdfs.png)](\assets\posts\{{ page.name }}\hdfs.png)

Hadoop의 핵심 파일 시스템인 **HDFS(Hadoop Distributed File System)**는 대규모 데이터를 블록 단위로 나누어 여러 노드에 분산 저장하고, 블록의 복제본을 두어 데이터의 내구성을 보장합니다. `Rack Awareness`를 통해 복제본을 다른 Rack에 배치하여 장애 발생 시에도 데이터를 보호합니다.

- `NameNode`: 메타데이터를 관리하는 주 노드로, 파일 시스템의 메타데이터(파일, 블록 위치 등)를 담당합니다.
- `DataNode`: 실제 데이터를 저장하는 노드로, NameNode에서 요구하는 데이터를 제공하거나 저장합니다.

### MapReduce
`MapReduce`는 대규모 데이터를 처리하기 위한 분산 처리 모델로, `Hadoop`에서 주로 사용되는 처리 방식입니다.
이 구조에서는 `JobTracker`와 `TaskTracker`가 리소스를 관리하고 작업을 처리하는 핵심 역할을 합니다.

- `JobTracker`: 작업을 전체적으로 관리하고, 각 작업을 처리할 TaskTracker에 할당합니다.
- `TaskTracker`: 실제 작업을 실행하는 노드로, JobTracker에서 할당한 작업을 수행합니다.

#### Framework
MapReduce의 복잡성 및 비효율성을 해결하기 위해 다양한 프레임워크들이 등장했습니다. 이들 프레임워크는 MapReduce를 활용하면서도 보다 효율적이고 사용자 친화적인 데이터 처리 방식을 제공합니다.

- `Hive`: 대용량 데이터 처리에 최적화된 `SQL` 기반 쿼리 언어인 HiveQL을 사용하여, `MapReduce` 작업을 통해 데이터를 처리합니다.
- `Pig`: 데이터를 변환하고 분석하는 데 사용되는 스크립팅 언어로, `MapReduce`를 기반으로 작업을 수행합니다.
- `HBase`: HDFS 위에서 실시간 데이터 접근을 지원하는 분산 `NoSQL` 데이터베이스로, `MapReduce`와 결합하여 배치 처리 및 실시간 데이터를 함께 처리할 수 있습니다.

---

## Hadoop 2.0

`Hadoop 2.0`은 `Hadoop 1.0`의 한계를 극복하기 위해 여러 가지 중요한 개선이 이루어진 버전입니다. 주요 변화 중 하나는 **YARN(Yet Another Resource Negotiator)**의 도입으로, YARN은 리소스 관리 및 작업 스케줄링을 담당하며, 이를 통해 여러 애플리케이션이 클러스터 자원을 효율적으로 공유할 수 있게 되었습니다.

### HDFS
`HDFS`는 Hadoop 2.0에서도 여전히 핵심 파일 시스템으로 사용됩니다. 그러나 Hadoop 2.0에서는 HDFS의 `확장성`과 `안정성`이 크게 향상되었습니다. 이로 인해 대규모 데이터 처리와 분산 저장 환경에서 더 높은 성능과 안정성을 제공합니다.

### YARN

[![](\assets\posts\{{ page.name }}\yarn.png)](\assets\posts\{{ page.name }}\yarn.png)

`YARN`은 Hadoop 2.0의 핵심 컴포넌트로, 리소스 관리 및 작업 스케줄링을 담당합니다. YARN의 도입으로 Hadoop은 `MapReduce` 외에도 `Spark`, `Tez`와 같은 다양한 프레임워크를 실행할 수 있게 되었습니다. 

- `ResourceManager`: 클러스터 리소스를 관리하고, 애플리케이션에 할당할 자원을 결정합니다.
- `NodeManager`: 각 노드에서 리소스를 관리하고 작업을 실행합니다. NodeManager는 각 작업을 컨테이너 형태로 실행하고, 실행 상태를 `ResourceManager`에 보고합니다.
- `ApplicationMaster`: 각 애플리케이션의 실행을 관리합니다. ApplicationMaster는 자원 요청을 `ResourceManager`에 보내고, 실행될 노드를 결정합니다.

#### Framework
Hadoop 2.0에서 YARN을 활용하여 여러 프레임워크가 동시에 실행될 수 있습니다. Hadoop 1.0에서 MapReduce의 한계가 있었던 것과 달리, Hadoop 2.0은 더 효율적이고 빠른 데이터 처리 모델을 제공합니다.

- `Spark`: Spark는 메모리 내 데이터 처리 모델을 사용하여, 빠른 속도로 데이터를 처리할 수 있습니다. **RDD(Resilient Distributed Dataset)**를 사용하여 병렬 처리를 효율적으로 수행합니다.
- `Tez`: `DAG(Directed Acyclic Graph)` 기반의 실행 모델을 사용하여 `MapReduce`의 성능을 개선합니다. 복잡한 데이터 처리 작업을 효율적으로 관리합니다.
- `Flink`: 실시간 스트리밍 데이터 처리에 강력한 기능을 제공하는 분산 처리 엔진으로, `YARN`을 통해 리소스를 관리하며 실시간 데이터를 실시간으로 처리할 수 있습니다.

---

## References
- [Hadoop 공식 문서](https://hadoop.apache.org/docs)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
