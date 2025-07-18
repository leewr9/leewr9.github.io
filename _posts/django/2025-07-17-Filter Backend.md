---
title: Filter Backend
category: Django
tag: [Filter, REST Framework, Python, Django]
---

> Django에서 RESTful API를 개발하다 보면 데이터 조회 시 조건에 맞게 데이터를 필터링하는 기능이 필수적입니다. Django와 REST Framework는 이를 위해 여러 필터링 기능과 도구를 제공합니다.

---

## django-filter
`django-filter`는 Django ORM 기반 쿼리셋에 대해 URL 쿼리 파라미터로 필터 조건을 지정할 수 있게 해주는 서드파티 라이브러리입니다.

```bash
pip install django-filter
```

```python
# settings.py

INSTALLED_APPS = [
    ...
    'django_filters',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ]
}
```
`DEFAULT_FILTER_BACKENDS` 설정은 프로젝트 전역에서 기본적으로 사용할 필터 백엔드를 지정하는 설정입니다. 각 View에 `filter_backends`를 따로 지정하지 않은 경우 이 설정이 적용됩니다.

### DjangoFilterBackend
`DjangoFilterBackend`는 `/api/items/?field1=value1`처럼 쿼리스트링으로 전달된 조건을 Django ORM 필터로 변환해 복잡한 조건 검색을 쉽게 구현할 수 있는 DRF용 필터 백엔드입니다.

```python
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'category', 'price']

# /api/books/?author=Tom&price=10000
```

### FilterSet
`FilterSet`은 복잡한 필터 조건을 명시적으로 정의할 수 있는 클래스이며, `filterset_class`로 등록하면 `DjangoFilterBackend`가 쿼리스트링을 Django ORM 필터로 자동 변환해줍니다.

```python
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    published_after = django_filters.DateFilter(field_name='published_date', lookup_expr='gte')

    class Meta:
        model = Book
        fields = ['author', 'category', 'min_price', 'max_price', 'published_after']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

# /api/books/?author=Tom&min_price=5000&published_after=2024-01-01
```

---

## filters
`filters`는 DRF에서 기본 제공하는 필터 백엔드 모듈로, 검색과 정렬 기능을 쉽게 추가할 수 있도록 지원합니다.

```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ]
}
```

### SearchFilter
`SearchFilter`는 `/api/items/?search=keyword`처럼 특정 필드에 대해 키워드 기반의 부분 일치 검색을 지원하는 필터 백엔드입니다.

```python
from rest_framework.filters import SearchFilter

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^title', '=author__name']

# /api/books/?search=Python
```
- `search_fields`: 검색 대상 필드를 지정 (`__`로 ForeignKey 접근 가능)
- `^`: 제목이 검색어로 시작하는 것만 검색
- `=`: 제목이 정확히 검색어와 일치하는 것만 검색
- `@`: DB의 full-text 검색 지원 시 사용
- `$`: 제목이 검색어로 끝나는 것만 검색

### OrderingFilter
`OrderingFilter`는 `/api/items/?ordering=target`처럼 결과 정렬을 지원하는 필터 백엔드입니다.

```python
from rest_framework.filters import OrderingFilter

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['published_date', 'price']
    ordering = ['-published_date']

# /api/books/?ordering=published_date
```
- `ordering_fields`: 정렬 허용 필드 지정
- `ordering`: 기본 정렬 기준 지정 (`-`는 내림차순)

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
