---
title: Style Pattern 
category: Architecture
tag: [MVC, MVVM, MVP, MVI, Architecture]
---

> 소프트웨어 개발에서 아키텍처 스타일과 패턴은 시스템 구조를 설계하고 구현하는 데 반복적으로 사용되는 방법입니다. 아키텍처 스타일은 소프트웨어 전체 구조의 기본 틀과 원리를 제공하며, 패턴은 특정 문제를 해결하기 위한 구체적 구현 방법을 제시합니다. 

---

## Architecture Style
`Architecture Style`은 시스템 전체의 구조적 특징과 설계 철학을 나타내는 상위 개념입니다. 시스템을 어떻게 구조화할 것인가라는 큰 그림 관점에서 설계를 정의합니다.

### Layered Architecture
`Layered Architecture`는 애플리케이션을 여러 계층으로 나누어 각 계층이 명확한 책임을 갖도록 하는 스타일입니다. 가장 널리 사용되는 서버/웹 애플리케이션 구조로, 유지보수와 확장이 용이합니다. 계층별로 책임이 분리되어 테스트가 쉽고, 변경이 다른 계층에 미치는 영향을 최소화할 수 있습니다.

[![](\assets\posts\2025-09-07-Style Pattern.md\layered.png)](\assets\posts\2025-09-07-Style Pattern.md\layered.png)

- `Presentation Layer`: 사용자 인터페이스와 입력 처리
- `Business Logic Layer`: 핵심 비즈니스 로직 처리
- `Data Access Layer`: 데이터 저장소와의 상호작용

### Client-Server
`Client-Server`는 클라이언트와 서버를 명확히 분리하여, 클라이언트는 사용자 인터페이스와 입력 처리, 서버는 데이터 저장과 처리에 집중하도록 하는 스타일입니다. 거의 모든 네트워크 기반 애플리케이션의 기본 구조입니다. 클라이언트와 서버의 역할이 명확하여 개발과 유지보수가 효율적이며, 서버 확장이나 클라이언트 변경이 독립적으로 가능합니다.

[![](\assets\posts\2025-09-07-Style Pattern.md\client-server.png)](\assets\posts\2025-09-07-Style Pattern.md\client-server.png)

- `Client`: 요청 생성 및 UI 제공
- `Server`: 요청 처리, 데이터 저장, 응답 생성

### Microservices
`Microservices`는 애플리케이션을 여러 독립 서비스 단위로 나누어 개발, 배포, 확장이 가능하도록 하는 스타일입니다. 현대 웹/클라우드 기반 서비스에서 핵심적으로 사용됩니다. 서비스 간 독립성이 높아 한 서비스 장애가 전체 시스템에 미치는 영향을 줄일 수 있고, 팀 단위 개발과 기술 선택의 유연성을 높입니다.

- `Service`: 독립적으로 배포 가능한 작은 단위
- `API Gateway`: 외부 요청을 서비스별로 라우팅
- `Database per Service`: 각 서비스가 자체 데이터 저장소 사용

---

## Architecture Pattern
`Architecture Pattern`은 특정 문제를 해결하기 위해 반복적으로 사용되는 재사용 가능한 설계 솔루션입니다. 어떻게 구현할 것인가라는 세부 설계 관점에서 활용됩니다.

### MVC
`MVC`는 `Model`, `View`, `Controller`를 분리하여 데이터, 화면, 제어 로직을 명확히 구분하는 패턴입니다. 웹, 데스크톱, 모바일 등 다양한 환경에서 기본 UI 패턴으로 널리 사용됩니다. 코드 재사용성을 높이고, 테스트 용이성이 뛰어나며, UI와 비즈니스 로직의 의존성을 최소화할 수 있습니다.

[![](\assets\posts\2025-09-07-Style Pattern.md\mvc.png)](\assets\posts\2025-09-07-Style Pattern.md\mvc.png)

- **Model**
  - 애플리케이션 상태 유지
  - 데이터 검증 및 처리
  - View나 Controller에 의존하지 않고 독립적
- **View**
  - 사용자에게 데이터 시각화
  - 입력 요소(UI) 렌더링
  - Controller를 통해 사용자 입력 전달
- **Controller**
  - 사용자 이벤트 수신 및 처리
  - 필요한 경우 Model 업데이트
  - 업데이트 후 View 갱신 지시

### MVVM
`MVVM`은 데이터 바인딩을 통해 View와 Model을 자동으로 동기화하는 패턴입니다. 클라이언트 애플리케이션, 특히 `WPF`, `Qt`, `Android`, `iOS`, `React` 등 현대 프론트엔드 환경에서 많이 사용됩니다. UI 상태 관리가 쉽고, View와 비즈니스 로직을 깔끔하게 분리할 수 있습니다.

[![](\assets\posts\2025-09-07-Style Pattern.md\mvvm.png)](\assets\posts\2025-09-07-Style Pattern.md\mvvm.png)

- **Model**
  - 핵심 데이터와 상태 관리
  - 비즈니스 규칙 및 검증 처리
  - ViewModel에 의해 View와 연결됨
- **View**
  - 사용자 입력을 ViewModel에 전달
  - ViewModel 상태를 자동으로 반영
  - UI 업데이트 로직 최소화
- **ViewModel**
  - View와 Model 사이 데이터/이벤트 중계
  - UI 상태 유지 및 계산
  - 사용자 입력을 처리하여 Model 업데이트

### MVP
`MVP`는 MVC 변형으로, `Presenter`가 View와 Model 간 상호작용을 담당합니다. 전통 Android 앱이나 데스크톱 UI에서 많이 활용되며, UI와 로직 분리를 통해 테스트와 유지보수가 용이합니다.

[![](\assets\posts\2025-09-07-Style Pattern.md\mvp.png)](\assets\posts\2025-09-07-Style Pattern.md\mvp.png)

- **Model**
  - 핵심 데이터 처리 및 상태 유지
  - Presenter에 의해 제어
  - View와 직접 상호작용하지 않음
- **View**
  - 사용자 입력 수집
  - Presenter에게 이벤트 전달
  - 화면 렌더링 담당
- **Presenter**
  - View 이벤트 수신 및 처리
  - Model 상태 변경
  - 변경된 상태를 View에 반영

### MVI
`MVI`는 단방향 데이터 흐름을 기반으로 UI 상태를 관리하는 패턴입니다. 모바일/웹에서 상태 일관성과 예측 가능한 UI 업데이트를 제공합며, `Reducer`가 이전 상태와 Intent를 받아 새로운 상태를 계산하고 상태 변경 로직을 수행합니다.

- **Model**
  - 현재 UI 상태 저장
  - 단일 불변 상태(Single Source of Truth)
  - Reducer/State Transformation을 통해 업데이트
- **View**
  - Model 상태를 읽어 UI 표시
  - 사용자 이벤트를 Intent로 변환
- **Intent**
  - 사용자 입력, 외부 이벤트 등 수집
  - 상태 변경 로직(Reducer)에 전달
  - Model 상태 업데이트 유도


---

## References

- [Wikipedia 공식 문서](https://wikipedia.org/wiki/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
