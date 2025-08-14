---
title: Relational System
category: Database
tag: [MySQL, MariaDB, SQLite, PostgreSQL, Oracle, RDBMS, Database]
---

> 관계형 데이터베이스는 데이터를 행과 열로 구성된 테이블에 저장하고 SQL로 정의 및 조작하는 시스템으로, 데이터 무결성과 일관성을 보장하며 복잡한 트랜잭션과 쿼리를 안정적으로 처리할 수 있습니다. 효율적인 검색과 데이터 관리가 가능해 웹 서비스, 엔터프라이즈 시스템 등 다양한 분야에서 활용됩니다.

---

## RDBMS

**RDBMS(Relational Database Management System)**는 데이터를 행과 열로 구성된 테이블에 저장하며, SQL을 통해 데이터를 정의하고 조작합니다. `ACID` 트랜잭션과 데이터 무결성을 지원하며, `CRUD` 중심 웹 서비스와 일반적인 엔터프라이즈 시스템에 적합합니다.

### MySQL

`MySQL`은 설치와 배포가 매우 간단하고 읽기 성능이 뛰어나, 다양한 웹 서비스에서 오랜 기간 널리 사용되어 온 데이터베이스입니다. 안정적이고 성숙한 생태계를 가지고 있어, 라이브러리와 툴 지원이 풍부하며, 운영과 관리가 비교적 쉽습니다.

[![](\assets\posts\2025-08-31-Relational System.md\mysql.png)](\assets\posts\2025-08-31-Relational System.md\mysql.png)

- JSON, 배열 등 고급 데이터 타입 제한
- 일부 SQL 표준 미준수
- 대규모 트랜잭션 환경에는 한계

### MariaDB

`MariaDB`는 MySQL을 기반으로 만들어진 포크로, MySQL과 완벽하게 호환되면서도 성능과 스토리지 엔진이 개선되어 더 효율적인 데이터 처리가 가능합니다. `Galera Cluster`를 사용하면 멀티마스터 환경에서 데이터 일관성을 유지하면서 고가용성을 지원할 수 있어 확장성과 안정성이 뛰어납니다.

[![](\assets\posts\2025-08-31-Relational System.md\mariadb.png)](\assets\posts\2025-08-31-Relational System.md\mariadb.png)

- 최신 MySQL 기능 일부 미지원
- `Galera Cluster`: 모든 노드에서 동시에 읽기·쓰기 가능, 고가용성·데이터 일관성 지원

### SQLite

`SQLite`는 서버 없이 단일 파일로 동작하는 임베디드 데이터베이스로, 설치와 설정이 거의 필요 없고 관리가 매우 간단합니다. 소규모 서비스, 테스트 환경, 모바일 앱과 같은 경량 환경에서 특히 유용하며, 작은 프로젝트에서 빠르게 데이터 저장과 조회가 가능합니다.

[![](\assets\posts\2025-08-31-Relational System.md\sqlite.png)](\assets\posts\2025-08-31-Relational System.md\sqlite.png)

- 동시성 처리 제한
- 대규모 트랜잭션 부적합
- 서버 기반 기능 제한

---

## ORDBMS

**ORDBMS(Object-Relational Database Management System)**는 RDBMS 기능을 기반으로 객체 지향 기능을 추가한 데이터베이스입니다. 한 컬럼에 배열, JSON 같은 복잡한 데이터도 바로 저장할 수 있고, 테이블 상속 기능을 이용해 부모-자식 구조를 가진 데이터를 다루는 것도 가능합니다.

### Oracle Database

`Oracle Database`는 상용 ORDBMS로, RDBMS 기능에 객체 지향 데이터 타입, 컬렉션, 사용자 정의 타입, 테이블 상속, 패키지, 함수 등을 제공하여 대규모 엔터프라이즈 시스템에서 강점을 가집니다. 금융, ERP, 분석용 시스템과 같이 안정성과 신뢰성이 중요한 환경에서 탁월하며, 대규모 트랜잭션 처리에도 최적화되어 있습니다.

[![](\assets\posts\2025-08-31-Relational System.md\oracle.png)](\assets\posts\2025-08-31-Relational System.md\oracle.png)

- 상용 라이선스 비용 발생

### PostgreSQL

`PostgreSQL`은 오픈소스 ORDBMS로, SQL 표준을 엄격하게 준수하며 다양한 객체형 데이터 타입을 지원합니다. JSON, 배열, 사용자 정의 타입, 테이블 상속 등 복잡한 데이터 구조를 다룰 수 있으며, ACID 트랜잭션을 철저히 지원해 안정적인 데이터 무결성을 제공합니다.

[![](\assets\posts\2025-08-31-Relational System.md\postgresql.png)](\assets\posts\2025-08-31-Relational System.md\postgresql.png)

- 일부 고급 기능 초기 설정 필요

| 항목              | PostgreSQL                                   | MySQL                             |
| ----------------- | -------------------------------------------- | --------------------------------- |
| **타입**          | ORDBMS                                       | RDBMS                             |
| **SQL 표준 준수** | 표준 SQL 엄격 준수                           | 일부 비표준 허용                  |
| **데이터 타입**   | JSON, 배열, 사용자 정의 타입, 테이블 상속 등 | 기본형, JSON 지원                 |
| **트랜잭션**      | ACID 강력, 복잡한 트랜잭션/분석 환경 적합    | ACID 지원, 단순 환경 적합         |
| **확장성**        | 멀티노드, 파티셔닝, 복잡한 구조 지원         | 단일 노드 및 마스터-슬레이브 가능 |

---

## References

- [Wikipedia 공식 문서](https://wikipedia.org/wiki/)
- [MySQL 공식 문서](https://dev.mysql.com/doc/)
- [MariaDB 공식 문서](https://mariadb.com/docs/)
- [SQLite 공식 문서](https://www.sqlite.org/docs.html)
- [PostgreSQL 공식 문서](https://www.postgresql.org/docs/)
- [Oracle 공식 문서](https://docs.oracle.com/database/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
