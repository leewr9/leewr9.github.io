---
title: System Architecture
category: Airflow
tag: [Airflow]
---

> Apache Airflow는 작업의 자동화 및 스케줄링을 위한 강력한 플랫폼으로, 여러 중요한 구성 요소가 함께 작동하여 DAG(Directed Acyclic Graph) 기반의 작업 흐름을 관리합니다. 각 구성 요소의 역할과 동작 방식을 정확히 이해하는 것이 중요합니다.

---

## Lifecycle

[![](\assets\posts\2025-01-31-System Architecture\diagram.png)](\assets\posts\2025-01-31-System Architecture\diagram.png)

### Scheduler

Scheduler는 시스템 내에서 작업을 예약하는 역할을 합니다. 주기적으로 실행될 작업이나, 수동으로 트리거된 작업을 큐에 추가하고, 해당 작업이 실행될 시점과 우선순위를 결정합니다. Scheduler는 작업의 의존성을 관리하고, 실행할 때 `Worker`에게 작업을 전달합니다.

- 작업 예약 및 실행 시점 결정
- 작업 의존성 관리
- 작업 큐에 작업 추가 및 실행 준비

### Executor
`Executor`는 `Worker`가 작업을 실행할 수 있는 환경을 설정합니다. 작업이 실행될 방법과 방식을 결정하는 역할을 하며, `Worker`가 작업을 어떻게 실행할지 설정합니다. 

- 작업 실행 환경 설정
- 실행 방식 결정 (로컬, 분산 등)
- 여러 실행 모드 제공
   - `LocalExecutor`: 로컬 작업
   - `CeleryExecutor`: 분산 환경 작업

### Worker
Worker는 실제로 `Scheduler`가 예약한 작업을 실행하는 구성 요소입니다. `Scheduler`로부터 받은 작업을 `Executor`가 설정한 환경에 맞춰 실행하고, 그 결과를 다시 `Scheduler`에게 보고합니다. 여러 Worker가 동시에 작업을 실행하여, 병렬 처리로 시스템의 성능을 향상시킬 수 있습니다.

- 작업 실행
- 실행 결과 보고
- 병렬 처리로 성능 최적화

---

## Architecture

[![](\assets\posts\2025-01-31-System Architecture\architecture.png)](\assets\posts\2025-01-31-System Architecture\architecture.png)

### Webserver
Web Server는 클라이언트와 시스템 간의 인터페이스 역할을 합니다. 사용자는 웹 브라우저를 통해 요청을 보내고, Web Server는 이 요청을 처리하여 적절한 응답을 클라이언트에게 반환합니다. 웹 서버는 주로 `RESTful API`나 웹 애플리케이션을 통해 시스템과 상호작용합니다.

- HTTP 요청 처리
- RESTful API 제공
- 클라이언트와 시스템 간의 인터페이스 역할

### Metadata Database
Metadata Database는 시스템에서 발생한 작업의 상태, 실행 기록, 의존성 정보 등을 저장하는 데이터베이스입니다. 이 데이터베이스는 작업 흐름을 추적하고, 실패한 작업의 디버깅을 돕습니다. 

- 작업의 상태, 실행 기록 저장
- 작업 간 의존성 및 흐름 추적
- 시스템 모니터링 및 디버깅 지원

---

## References
- [Airflow 공식 문서](https://airflow.apache.org/docs/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
