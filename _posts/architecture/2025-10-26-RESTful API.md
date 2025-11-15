---
title: RESTful API
category: Architecture
tag: [RESTful API, Architecture]
---

> RESTful API는 웹 서비스 설계의 표준으로, 일관성 있고 확장성 높은 시스템을 구축할 수 있게 해주는 아키텍처 스타일입니다. HTTP 메서드와 URI를 활용해 자원을 명확히 표현하고, 상태 비저장성과 캐싱을 통해 효율적인 통신을 지원합니다.

---

## REST

**REST(Representational State Transfer)**는 웹 아키텍처 스타일로, 리소스를 중심으로 설계된 분산 시스템의 원칙과 제약 조건을 정의합니다

- 자원은 `명사`, `소문자 복수형`으로 URI에 표현
- 행위는 HTTP 메서드로 구분
- URI는 계층적 구조로 설계
- 서버는 클라이언트 상태를 저장하지 않으며, 각 요청은 독립적으로 처리
- HTTP 캐시를 활용해 성능을 최적화

| Action | HTTP Method | URI        | Description      |
| ------ | ----------- | ---------- | ---------------- |
| List   | GET         | /items     | 아이템 목록 조회 |
| Get    | GET         | /items/123 | 특정 아이템 조회 |
| Create | POST        | /items     | 아이템 생성      |
| Update | PUT         | /items/123 | 아이템 전체 수정 |
| Patch  | PATCH       | /items/123 | 아이템 일부 수정 |
| Delete | DELETE      | /items/123 | 아이템 삭제      |

### Status Code

`Status Code`는 RESTful API에서 클라이언트에게 요청 처리 결과를 명확히 전달하는 데 사용됩니다. 주요 HTTP 상태 코드는 다음과 같습니다.

| Code    | Meaning               | Description                   |
| ------- | --------------------- | ----------------------------- |
| **200** | OK                    | 성공적으로 처리됨             |
| **201** | Created               | 새 리소스 생성 성공           |
| **204** | No Content            | 성공(응답 본문 없음)          |
| **400** | Bad Request           | 잘못된 요청(파라미터 오류 등) |
| **401** | Unauthorized          | 인증 필요                     |
| **403** | Forbidden             | 권한 없음                     |
| **404** | Not Found             | 자원 없음                     |
| **409** | Conflict              | 중복 데이터 등 충돌           |
| **422** | Unprocessable Entity  | 유효성 검사 실패              |
| **500** | Internal Server Error | 서버 오류                     |

### Request

`Request`는 클라이언트가 서버에 보내는 HTTP 요청입니다. `GET`, `POST`, `PUT`, `PATCH`, `DELETE` 등의 메서드를 사용하여 특정 자원에 대한 행위를 지시합니다. 요청에는 URI, 헤더 등이 포함됩니다.

```http
GET /items/123 HTTP/1.1
Host: api.example.com
Authorization: Bearer <token>
```

### Response

`Response`는 서버가 클라이언트의 요청에 대해 보내는 HTTP 응답입니다. 상태 코드, 헤더, 본문으로 구성되며, 요청 처리 결과와 데이터를 포함합니다.

```json
{
  "id": 123,
  "name": "leewr9",
  "email": "leewr9@gmail.com",
  "created_at": "2025-11-15T12:34:56Z"
}
```

---

## Reference

- [Wikipedia 공식 문서](https://wikipedia.org/wiki/)

<nav class="post-toc" markdown="1">
  <h2>Table of Contents</h2>
* TOC
{:toc}
</nav>
