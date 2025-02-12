---
title: Various Executor
category: Airflow
tag: [Executor, Airflow]
---

> Executor는 Apache Airflow에서 작업을 실행하는 핵심 구성 요소로, 작업을 어떻게 처리할지에 대한 중요한 역할을 합니다. 다양한 종류의 Executor는 서로 다른 환경과 요구 사항에 맞춰 작업을 병렬로 처리하거나 분산 시스템을 활용하는 등 다양한 방식으로 동작합니다.

---

## SequentialExecutor
SequentialExecutor는 가장 간단한 형태의 Executor입니다. 이 Executor는 단일 프로세스에서 작업을 순차적으로 실행합니다. 보통 개발 환경이나 테스트 환경에서 사용됩니다. 실제 프로덕션 환경에서는 성능이 제한적이기 때문에 사용되지 않습니다.

- 단일 프로세스에서 실행
- 작업을 순차적으로 실행하며, 병렬 처리 불가
- 개발 환경에서 빠르게 실행하고 테스트할 때 유용

---

## LocalExecutor
LocalExecutor는 단일 머신에서 여러 작업을 병렬로 실행할 수 있는 Executor입니다. 작업을 순차적으로 실행하는 대신, 멀티 프로세싱을 사용하여 여러 작업을 동시에 실행할 수 있습니다. 이 Executor는 작은 규모의 클러스터에서 적당하며, 특히 하드웨어 리소스가 한정된 환경에서 유용합니다.

- 병렬 실행으로 여러 작업을 동시에 실행
- 단일 머신에서 멀티 프로세싱을 사용
- 다수의 작업을 처리할 수 있지만, 클러스터 분산은 불가능

---

## CeleryExecutor
CeleryExecutor는 분산 시스템에서 작업을 실행할 수 있는 Executor입니다. Celery는 메시지 큐를 사용하여 분산 환경에서 작업을 병렬로 처리할 수 있게 해줍니다. 여러 Worker들이 각각의 작업을 받아서 실행하는 방식으로, 성능과 확장성이 뛰어나 대규모 환경에서 많이 사용됩니다.

- 분산 시스템에서 여러 작업을 병렬로 처리
- Celery 메시지 큐를 통해 작업을 분배하고 처리
- Worker들이 작업을 병렬로 실행

---

## KubernetesExecutor
KubernetesExecutor는 `Kubernetes` 클러스터를 이용하여 각 작업을 컨테이너화하여 실행하는 Executor입니다. 각 작업은 독립적인 Pod로 실행되며, `Kubernetes`의 스케줄링과 관리 기능을 활용할 수 있습니다. 클라우드 환경에서 유용하며, 확장성과 유연성을 제공합니다.

### Inside Cluster

[![](\assets\posts\2025-02-01-Various Executor\inside.png)](\assets\posts\2025-02-01-Various Executor\inside.png)

Kubernetes 클러스터 내부에서 실행되는 경우, Airflow와 작업을 실행하는 컨테이너가 동일한 `Kubernetes` 클러스터 내에 존재하며, 클러스터의 자원만을 활용합니다.

- `Kubernetes` 클러스터에서 작업을 컨테이너화하여 실행
- 각 작업은 독립적인 `Pod`에서 실행
- 자원 자동 확장 및 자동 복구 가능

### Outside Cluster

[![](\assets\posts\2025-02-01-Various Executor\outside.png)](\assets\posts\2025-02-01-Various Executor\outside.png)

Kubernetes 클러스터 외부에서 실행하는 경우, Airflow와 작업을 실행하는 컨테이너는 클러스터 외부에서 실행되며, `Kubernetes API`와 연결하여 작업을 실행하고 관리해야 합니다.

- Airflow가 외부에서 `Kubernetes` 클러스터와 `API`로 상호작용
- 작업은 클러스터 내의 `Pod`에서 실행되며, `Airflow` 구성 요소는 클러스터 외부에서 실행
- Airflow와 Kubernetes 클러스터 간의 연결 필요
   - `kubeconfig` 파일을 사용하여 인증 및 연결 설정
   - `kubeconfig` 파일은 `Kubernetes` 클러스터 인증 정보를 포함하며, Airflow 환경에 복사하여 사용

---

## References
- [Airflow Kubernetes 공식 문서](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/index.html)
- [Airflow 공식 문서](https://airflow.apache.org/docs/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
