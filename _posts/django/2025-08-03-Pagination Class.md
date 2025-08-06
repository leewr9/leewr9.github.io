---
title: Pagination Class
category: Django
tag: [Pagination, REST Framework, Python, Django]
---

> Django에서 API 응답에서 데이터가 많을 경우, 한 번에 모두 반환하면 네트워크 부담과 클라이언트 처리 비용이 커집니다. 이를 해결하기 위해 REST Framework는 페이지네이션 기능을 제공합니다.

---

## Pagination

DRF는 다양한 페이지네이션 클래스를 기본으로 제공하며, 프로젝트 설정 또는 뷰 단위에서 쉽게 적용할 수 있습니다.

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

- `DEFAULT_PAGINATION_CLASS`: 기본 페이지네이션 클래스 지정
- `PAGE_SIZE`: 한 페이지에 포함할 기본 아이템 수

### PageNumberPagination

`PageNumberPagination`은 가장 기본적인 페이지네이션 방식으로, 쿼리 파라미터 `page`를 사용해 페이지 번호를 지정합니다.

```python
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 100

# /api/items/?page=2&size=20
```

- `page_size`: 기본 페이지 크기
- `page_size_query_param`: 클라이언트가 페이지 크기를 지정할 수 있는 쿼리 파라미터
- `max_page_size`: 최대 페이지 크기 제한

### LimitOffsetPagination

`LimitOffsetPagination`은 `limit`과 `offset` 쿼리 파라미터를 사용해 데이터 범위를 지정하는 방식입니다.

```python
from rest_framework.pagination import LimitOffsetPagination

class LimitOffsetPaginationExample(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100
# /api/items/?limit=20&offset=40
```

- `default_limit`: 기본 반환 개수
- `max_limit`: 최대 반환 개수

### CursorPagination

`CursorPagination`은 안전하고 효율적인 커서 기반 페이지네이션으로, 주로 대규모 데이터셋에 적합하며, 페이지 번호 방식의 문제점을 해결합니다.

```python
from rest_framework.pagination import CursorPagination

class StandardCursorPagination(CursorPagination):
    page_size = 10
    ordering = '-created'
    cursor_query_param = 'cursor'

# /api/items/?cursor=abcd1234
```

- `ordering`: 기본 정렬 필드
- `cursor_query_param`: 커서 파라미터 이름

`cursor` 값은 정렬 필드 값과 추가 정보를 인코딩한 토큰으로, 페이지 번호 대신 다음 조회 시작 위치를 지정해 데이터 변경에 따른 페이징 오류를 방지합니다.

---

## Response

DRF는 페이지네이션 결과를 클라이언트에 전달할 때, 전체 아이템 수와 다음·이전 페이지 URL, 그리고 현재 페이지의 데이터 리스트를 포함한 일관된 구조로 응답합니다. 이를 통해 클라이언트는 현재 페이지 상태를 파악하고, 쉽게 페이지를 이동할 수 있습니다.

- **PageNumberPagination / LimitOffsetPagination**

```json
{
  "count": 102,
  "next": "http://api.example.com/items/?page=3",
  "previous": "http://api.example.com/items/?page=1",
  "results": [
    { "id": 21, "name": "Item 21" },
    { "id": 22, "name": "Item 22" }
  ]
}
```

- **CursorPagination**

```json
{
  "next": "http://api.example.com/items/?cursor=YXJyYXljb25uZWN0aW9uOjIw",
  "previous": null,
  "results": [
    { "id": 41, "name": "Item 41" },
    { "id": 42, "name": "Item 42" }
  ]
}
```

- `count`: 전체 데이터셋에 있는 아이템의 총 개수입니다.
- `next`: 다음 페이지를 요청할 수 있는 URL이며, 없으면 `null`입니다.
- `previous`: 이전 페이지를 요청할 수 있는 URL이며, 없으면 `null`입니다.
- `results`: 현재 페이지에 포함된 실제 데이터 리스트입니다.

---

## References

- [Django 공식 문서](https://www.djangoproject.com/)
- [REST Framework 공식 문서](https://www.django-rest-framework.org/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
