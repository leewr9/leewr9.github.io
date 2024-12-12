---
title: DRF API View
category: Django
tag: [REST Framework, Python, Django]
---

{% raw %}

> Django REST Framework (DRF)는 웹 애플리케이션에서 RESTful API를 쉽게 구현할 수 있게 도와주는 강력한 도구입니다. API 뷰는 클라이언트가 요청을 보내고 응답을 받을 수 있는 인터페이스를 제공합니다. DRF에서는 함수 기반 API 뷰 (FBV), 클래스 기반 API 뷰 (CBV), ViewSet을 사용하여 API를 더욱 효율적으로 구축할 수 있습니다.

---

## Function-Based API Views
함수 기반 뷰는 간단한 API 구현에 적합한 방식으로, HTTP 요청에 따라 처리할 로직을 함수로 정의합니다. `DRF`에서는 `@api_view` 데코레이터를 사용하여 함수 기반 뷰를 구현할 수 있습니다.

```python
# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookModelSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
위 예시에서 `book_list`는 `GET` 요청으로 모든 책을 반환하고, `POST` 요청으로 새로운 책을 추가하는 함수 기반 뷰입니다. DRF의 `@api_view` 데코레이터를 사용하여 이 뷰가 처리할 HTTP 메서드를 지정할 수 있습니다.

---

## Class-Based API Views
클래스 기반 API 뷰는 보다 구조적이고 확장 가능한 방식으로, 클래스 내에서 여러 HTTP 메서드를 처리하는 로직을 정의합니다. `DRF`에서는 `APIView` 클래스를 상속받아 메서드를 구현합니다.

```python
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookModelSerializer

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
위의 예시에서 `BookListView`는 `GET` 요청으로 모든 책을 반환하고, `POST` 요청으로 새로운 책을 추가하는 API 뷰입니다. 클래스 기반 뷰는 각 HTTP 메서드를 클래스 내 메서드로 구현할 수 있어 관리와 확장이 용이합니다.

### Mixins
`Mixins`는 DRF에서 기본적인 `CRUD` 작업을 처리할 수 있는 메서드들을 제공하는 클래스입니다. Mixins를 사용하면 클래스 기반 뷰에 `Create`, `List`, `Retrieve`, `Update`, `Destroy` 등의 작업을 처리하는 메서드를 사용할 수 있습니다.

```python
# views.py

from rest_framework import mixins, generics
from .models import Book
from .serializers import BookModelSerializer

class BookListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, *args, **kwargs): # GET
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs): # POST
        return self.create(request, *args, **kwargs)


class BookRetrieveUpdateDestroyView(mixins.RetrieveModelMixin, 
                                    mixins.UpdateModelMixin, 
                                    mixins.DestroyModelMixin, 
                                    generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, *args, **kwargs): # GET
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs): # PUT
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs): # DELETE
        return self.destroy(request, *args, **kwargs)
```
`BookListCreateView`는 GET과 POST 요청을 처리하고, `BookRetrieveUpdateDestroyView`는 GET, PUT, PATCH, DELETE 요청을 처리합니다.

### Generics
`Generics`는 `Mixins`보다 좀 더 추상화된 클래스로, CRUD 작업을 훨씬 간편하게 처리할 수 있도록 도와줍니다. `GenericAPIView`를 상속받아 `queryset`과 `serializer_class`를 지정하는 데 사용됩니다.

```python
# views.py

from rest_framework import generics
from .models import Book
from .serializers import BookModelSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
```
`ListCreateAPIView`는 GET과 POST 요청을 처리하고, `RetrieveUpdateDestroyAPIView`는 GET, PUT, PATCH, DELETE 요청을 처리합니다.

---

## ViewSet
`ViewSet`은 DRF에서 `CRUD` 기능을 쉽게 구현할 수 있도록 도와주는 클래스입니다. `ViewSet`을 사용하면 RESTful API의 기본적인 CRUD 작업을 한 번에 자동으로 처리할 수 있으며, 이를 `Router`와 함께 사용하여 URL 패턴을 자동으로 생성할 수 있습니다.

```python
# views.py

from rest_framework import viewsets
from .models import Book
from .serializers import BookModelSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
```

```python
# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```
BookViewSet은 `ModelViewSet`을 상속받아, Book 모델에 대한 CRUD 작업을 자동으로 처리합니다. `DefaultRouter`는 BookViewSet을 `books/` 경로에 자동으로 매핑해줍니다. 이 방식은 RESTful API의 구현을 매우 간편하게 만들어 줍니다.

---

## Override
`APIView`나` ViewSet`에서 제공하는 다양한 메서드를 오버라이드하여 클라이언트의 요청을 효율적으로 처리하고, 추가적인 비즈니스 로직을 적용할 수 있습니다.

```python
# views.py

from rest_framework import viewsets
from .models import Book
from .serializers import BookModelSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, *args, **kwargs):
        """
        GET 요청을 처리하여 모든 책 데이터를 반환합니다.
        """
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        POST 요청을 처리하여 새로운 책을 생성합니다.
        """
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # 데이터가 유효하면 책을 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def perform_create(self, serializer):
        """
        새로운 책을 저장할 때, 추가적인 로직을 수행할 수 있습니다.
        예를 들어, 책을 저장하기 전에 작성자를 현재 로그인한 사용자로 설정하는 등
        """
        user = self.request.user  # 현재 로그인한 사용자
        serializer.save(user=user)  # 책 저장 시 user 필드에 현재 사용자 지정
```

---

## Filtering
`Django Filter`를 사용하면 데이터를 조건에 맞게 필터링할 수 있습니다. DRF에서는 `FilterSet`을 사용하여 필터링 조건을 정의합니다. `FilterSet`은 필터링을 위한 조건을 정의할 수 있는 DRF의 도구입니다. `django_filters` 라이브러리를 설치한 후 필터셋을 정의하고 사용합니다.

```bash
pip install django-filter
```

```python
# views.py
import django_filters
from rest_framework import viewsets
from .models import Book
from .serializers import BookModelSerializer

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    published_date = django_filters.DateFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filterset_class = BookFilter
```
위 예시에서는 BookFilter를 사용하여 `title`, `author`, `published_date`를 필터링할 수 있도록 설정하였습니다. 이제 API 요청에 필터링 조건을 추가하면 해당 조건에 맞는 데이터만 반환됩니다.
- 제목으로 필터링: `GET /api/books/?title=django`
- 저자 이름으로 필터링: `GET /api/books/?author=John`
- 출판 날짜로 필터링: `GET /api/books/?published_date=2020-01-01`

---

## Paging
DRF에서는 페이징을 설정하여 데이터가 많을 때 성능을 최적화할 수 있습니다. 기본적으로 DRF는 페이지네이션을 지원하며, `settings.py`에서 설정을 변경하거나, `PageNumberPagination` 클래스로 변경하여 사용할 수 있습니다.

```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10, # 한 페이지에 10개 데이터만 반환
}
```

```python
# views.py

from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import Book
from .serializers import BookModelSerializer

class BookPagination(PageNumberPagination):
    page_size = 5  # 한 페이지에 5개 데이터만 반환

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    pagination_class = BookPagination
```

---

## References
- [Django 공식 문서](https://www.djangoproject.com/)
- [REST Framework 공식 문서](https://www.django-rest-framework.org/)
- [Python 공식 문서](https://docs.python.org/3/)

{% endraw %}

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
