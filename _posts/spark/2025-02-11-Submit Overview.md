---
title:  Submit Overview
category: Spark
tag: [Spark]
---

> spark-submit은 Spark 애플리케이션을 클러스터에 제출하고 실행하는 명령어입니다. 이 명령어는 애플리케이션을 실행할 환경을 설정하고 리소스를 할당하는 여러 옵션을 제공합니다.

---

## Master Configuration
`--master`는 Spark 애플리케이션이 실행되는 클러스터의 중심 역할을 합니다. 다양한 클러스터 매니저를 사용할 수 있으며, 각 마스터는 리소스를 할당하고, 작업을 스케줄링하며, 전체 시스템을 관리합니다.

```bash
spark-submit --master local[4] --deploy-mode client my_app.py # 로컬 모드에서 4개의 스레드를 사용
```

- `Local`: Spark 애플리케이션이 로컬 머신에서 실행되는 모드입니다. 클러스터 없이 로컬 머신에서 모든 작업이 실행됩니다. 
- `Standalone`: Spark의 자체 클러스터 관리 시스템입니다. Spark 클러스터를 자체적으로 설정하고 관리할 수 있습니다.
- `YARN`: Hadoop YARN 클러스터에서 자원을 관리하고 작업을 스케줄링합니다. YARN은 대규모 클러스터 환경에서 Spark를 실행하는 데 적합합니다.
- `Kubernetes`: Kubernetes 클러스터에서 Spark 애플리케이션을 실행하며, Kubernetes가 자원 관리와 작업 스케줄링을 담당합니다.

---

## Deployment Configuration
`--deploy-mode`는 Spark 애플리케이션의 드라이버가 어디에서 실행될지를 결정합니다. 

- `Client Mode`
    - 드라이버가 로컬 머신에서 실행
    - 클러스터에 있는 작업을 로컬 머신에서 관리합니다.
    - 로컬에서 디버깅이나 테스트할 때 유용합니다.
- `Cluster Mode`
    - 드라이버가 클러스터 내에서 실행
    - Spark 클러스터에서 자원을 효율적으로 활용하고, 드라이버도 클러스터 내에서 관리됩니다.
    - 클러스터 환경에서 애플리케이션을 실행할 때 성능이나 안정성에 유리합니다.

---

## Execution Location
`--master`와 `--deploy-mode` 옵션에 따라 Spark 애플리케이션의 실행 위치가 달라집니다. --master 옵션은 클러스터 매니저를 지정하고, Spark 클러스터가 어떻게 구성되는지를 정의하며, --deploy-mode 옵션은 드라이버의 실행 위치를 결정합니다.

### Local
- Master: 해당 없음 (로컬 모드에서는 마스터 노드가 없으며, 로컬 시스템에서만 실행)
- Cluster Manager: 사용되지 않음 (로컬 환경에서는 클러스터 매니저가 존재하지 않음)
- Client
    ```bash
spark-submit --master local[4] --deploy-mode client my_app.py
    ```
    - Driver: 로컬 머신에서 실행 (애플리케이션의 중앙 제어를 담당)
- Cluster
    - 사용 불가: 로컬 모드에서는 `--deploy-mode cluster`를 사용할 수 없습니다.

### Standalone
- Master: `spark://localhost:7077` (Standalone 클러스터의 마스터 노드)
- Cluster Manager: Spark 자체 클러스터 매니저가 자원 관리 및 작업 스케줄링을 담당
- Client
    ```bash
spark-submit --master spark://localhost:7077 --deploy-mode client my_app.py
    ```
    - Driver: 로컬 머신에서 실행 (애플리케이션의 중앙 제어를 담당)
- Cluster
    ```bash
spark-submit --master spark://localhost:7077 --deploy-mode cluster my_app.py
    ```
    - Driver: 클러스터 내에서 실행 (클러스터 내에서 자원을 할당하고 작업을 관리)

### YARN
- Master: `YARN ResourceManager` (YARN ResourceManager가 클러스터의 리소스를 관리)
- Cluster Manager: `YARN ResourceManager` (YARN이 자원 관리 및 작업 스케줄링을 담당)
- Client
    ```bash
spark-submit --master yarn --deploy-mode client my_app.py
    ```
    - Driver: 로컬 머신에서 실행 (애플리케이션을 로컬에서 제어)
- Cluster
    ```bash
spark-submit --master yarn --deploy-mode cluster my_app.py
    ```
    - Driver: YARN 클러스터 내에서 실행 (YARN 클러스터 내에서 드라이버 실행)

### Kubernetes
- Master: `K8S Master` (Kubernetes 클러스터의 마스터 노드)
- Cluster Manager: `Kubernetes` (Kubernetes가 자원 관리 및 작업 스케줄링을 담당)
- Client
    ```bash
spark-submit --master k8s://https://<k8s-master-url> --deploy-mode client --conf spark.kubernetes.container.image=<image-name> my_app.py
    ```
    - Driver: 로컬 머신에서 실행 (로컬 머신에서 애플리케이션을 제어)
- Cluster
[![](\assets\posts\2025-02-11-Submit Overview\k8s.png)](\assets\posts\2025-02-11-Submit Overview\k8s.png)
    ```bash
spark-submit --master k8s://https://<k8s-master-url> --deploy-mode cluster --conf spark kubernetes.container.image=<image-name> my_app.py
    ```
    - Driver: Kubernetes 클러스터 내에서 실행 (Kubernetes의 Pod에서 실행)

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
