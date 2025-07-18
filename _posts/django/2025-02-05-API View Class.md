---
title: API View Class
category: Django
tag: [REST Framework, Python, Django]
---

> Django REST Framework API 뷰는 클라이언트가 요청을 보내고 응답을 받을 수 있는 인터페이스를 제공합니다. DRF에서는 함수 기반 API 뷰 (FBV), 클래스 기반 API 뷰 (CBV), ViewSet을 사용하여 API를 더욱 효율적으로 구축할 수 있습니다.

---

## Function-Based
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

## Class-Based
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

- `BookListCreateView`: GET과 POST 요청을 처리
- `BookRetrieveUpdateDestroyView`: GET, PUT, PATCH, DELETE 요청을 처리

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

- `ListCreateAPIView`: GET과 POST 요청을 처리
- `RetrieveUpdateDestroyAPIView`: GET, PUT, PATCH, DELETE 요청을 처리

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

BookViewSet은 `ModelViewSet`을 상속받아, Book 모델에 대한 CRUD 작업을 자동으로 처리합니다. `DefaultRouter`는 BookViewSet을 `/api/books/` 경로에 자동으로 매핑해줍니다. 이 방식은 RESTful API의 구현을 매우 간편하게 만들어 줍니다.

### Override
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
            serializer.save() # 데이터가 유효하면 책을 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def perform_create(self, serializer):
        """
        새로운 책을 저장할 때, 추가적인 로직을 수행할 수 있습니다.
        예를 들어, 책을 저장하기 전에 작성자를 현재 로그인한 사용자로 설정하는 등
        """
        user = self.request.user # 현재 로그인한 사용자
        serializer.save(user=user) # 책 저장 시 user 필드에 현재 사용자 지정
```

### Custom Action
기본 제공되는 CRUD 액션(`list`, `retrieve`, `create`, `update`, `destroy`) 외에도,
ViewSet에 특정 비즈니스 로직을 수행하는 커스텀 엔드포인트를 추가하고 싶을 때 사용할 수 있습니다.
```python
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        """
        특정 Book 인스턴스에 대해 '좋아요'를 추가하는 커스텀 액션입니다.
        """
        book = self.get_object()
        book.likes += 1
        book.save()
        return Response({'status': 'liked', 'likes': book.likes}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """
        최근에 생성된 Book 목록 5개를 반환하는 커스텀 액션입니다.
        """
        recent_books = self.get_queryset().order_by('-created_at')[:5]
        serializer = self.get_serializer(recent_books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
```
- `@action`: 커스텀 URL 및 HTTP 메서드를 추가할 때 사용합니다.
- `detail`: 단일 객체에 대한 액션인지 여부를 나타냅니다. `True`일 경우 URL에 `pk`가 포함됩니다.
- `methods=['post']`: 커스텀 액션에서 사용할 HTTP 메서드를 지정합니다.
- `get_object()`: 요청에서 전달된 pk에 해당하는 객체를 조회합니다. (`detail=True` 사용)
- `get_queryset()`: 요청에서 정의한 쿼리셋 전체를 가져옵니다. (`detail=False` 사용)

---

## Permission
Django REST Framework는 API에 대한 접근을 제어할 수 있도록 `permission_classes` 속성을 제공합니다. 이 시스템을 통해 특정 사용자나 그룹에만 API 접근을 허용하거나, 사용자가 인증되었는지 등을 검사할 수 있습니다.

```python
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class BookView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'message': 'Hello, world!'})
```
- `IsAuthenticated`: 사용자가 인증되었는지 확인합니다. 인증되지 않은 사용자는 접근할 수 없습니다.
- `IsAdminUser`: 사용자가 관리자 권한을 가지고 있는지 확인합니다. 관리자만 접근할 수 있습니다.
- `IsAuthenticatedOrReadOnly`: 인증된 사용자에게는 읽기/쓰기 권한을 제공하고, 
인증되지 않은 사용자에게는 읽기 권한만 제공합니다.
- `AllowAny`: 모든 사용자가 접근할 수 있습니다. 인증 여부에 관계없이 API에 접근할 수 있도록 허용합니다.

### Custom
기본 제공되는 권한 클래스 외에도, 자체적인 권한 클래스를 만들어 더 복잡한 권한 로직을 구현할 수 있습니다. 커스텀 권한 클래스는 `permissions.BasePermission`을 상속하여 정의합니다.

```python
# permissions.py

from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # 객체의 'owner' 필드가 요청한 사용자와 일치하는지 확인
        return obj.owner == request.user
```

```python
from .permissions import IsOwner
from .models import Book

class BookView(APIView):
    permission_classes = [IsOwner]

    def get(self, request, pk):
        obj = Book.objects.get(pk=pk)
        self.check_object_permissions(request, obj) # has_object_permission 호출
        return Response({'message': 'You have access to this object.'})
```

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
