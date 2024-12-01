---
title: Django Serializer와 다양한 API 뷰
category: Study
tag: [Education, Rest Framework, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## `mixins` 모듈
> `mixins`는 Rest Framework에서 제공하는 여러 기본적인 뷰 메서드를 제공하는 클래스들입니다. 

* 주요 Mixins 클래스
    * CreateModelMixin: 객체 생성 기능을 제공합니다.
    * UpdateModelMixin: 객체 수정 기능을 제공합니다.
    * DestroyModelMixin: 객체 삭제 기능을 제공합니다.
    * ListModelMixin: 객체 목록을 조회하는 기능을 제공합니다.
    * RetrieveModelMixin: 개별 객체를 조회하는 기능을 제공합니다.

### 1. List / CreateModelMixin
```python
# views.py

from rest_framework import mixins
from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelListCreateView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    queryset = MyModel.objects.all() 
    serializer_class = MyModelSerializer

    def get(self, request, *args, **kwargs): # GET
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs): # POST
        return self.create(request, *args, **kwargs)
```

### 1. Retrieve / Update / DestroyModelMixin
```python
# views.py

from rest_framework import mixins
from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelRetrieveUpdateDestroyView(mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin,
                                       generics.GenericAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get(self, request, *args, **kwargs): # GET
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs): # PUT
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs): # DELETE
        return self.destroy(request, *args, **kwargs)
```

## `generics` 모듈
> `generics`는 mixins를 기반으로 좀 더 높은 수준의 추상화를 제공합니다. 
`generics` 클래스는 CRUD 작업을 위한 기본적인 동작을 자동으로 처리해 주므로, 코드가 더 간결해집니다.

* 주요 Generics 클래스
    * ListCreateAPIView: 객체 목록 조회와 객체 생성을 처리합니다.
    * RetrieveAPIView: 개별 객체 조회를 처리합니다.
    * UpdateAPIView: 객체 수정 처리를 합니다.
    * DestroyAPIView: 객체 삭제 처리를 합니다.
    * RetrieveUpdateAPIView: 객체 조회 및 수정을 처리합니다.
    * RetrieveDestroyAPIView: 객체 조회 및 삭제를 처리합니다.

### 1. ListCreateAPIView
```python
# views.py

from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelListCreateView(generics.ListCreateAPIView): # GET/POST
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

#### 오버라이드
```python
# views.py

from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    # get() 메서드 오버라이드 (목록 조회 방식 변경)
    def get(self, request, *args, **kwargs):
        # 필터링을 추가하여 결과를 반환
        queryset = self.get_queryset().filter(active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # post() 메서드 오버라이드 (객체 생성 방식 변경)
    def post(self, request, *args, **kwargs):
        # 요청 데이터에 추가적인 정보를 처리
        data = request.data.copy()
        data['created_by'] = request.user.id  # 사용자 정보를 추가
        return super().post(request, *args, **kwargs)  # 기본 동작 호출
```

### 2. RetrieveUpdateDestroyAPIView
```python
# views.py

from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): # GET/PUT/DELETE
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

#### 오버라이드
```python
# views.py

from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    # get() 메서드 오버라이드 (객체 조회 방식 변경)
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        # 특정 조건을 체크 후 조회
        if not obj.is_active:
            return Response({"error": "This object is inactive."}, status=400)
        return super().get(request, *args, **kwargs)

    # put() 메서드 오버라이드 (객체 수정 방식 변경)
    def put(self, request, *args, **kwargs):
        # 요청 데이터를 처리하여 수정
        data = request.data.copy()
        data['updated_at'] = timezone.now()
        request.data = data  # 수정된 데이터로 대체
        return super().put(request, *args, **kwargs)

    # delete() 메서드 오버라이드 (객체 삭제 방식 변경)
    def delete(self, request, *args, **kwargs):
        # 삭제 전에 조건 체크
        obj = self.get_object()
        if obj.is_locked:
            return Response({"error": "This object cannot be deleted."}, status=400)
        return super().delete(request, *args, **kwargs)
```

### 3. perform_create()
> perform_create()는 새로운 객체를 생성하고 저장하는 작업을 커스터마이징하려는 경우 사용됩니다. 
예를 들어, perform_create()를 오버라이드하여 객체 생성 시 추가적인 로직(예: 생성자 정보 추가, 특정 필드 설정 등)을 수행할 수 있습니다.

```python
from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelCreateView(generics.CreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def perform_create(self, serializer):
        # 객체를 저장하기 전에 추가적인 로직을 수행
        # 사용자 정보를 객체에 추가
        serializer.save(created_by=self.request.user)
```

## mixins와 generics의 차이점

| 기능 | mixins | generics |
| - | - | - |
| 코드 길이 | 상대적으로 길다 (여러 클래스를 결합) | 간결하다 (하나의 클래스만 사용) |
| 직관성 | CRUD 메서드를 직접 정의해야 한다. | CRUD 메서드가 자동으로 처리된다. |
| 확장성 | 필요에 맞게 세분화된 클래스를 사용할 수 있다. | 기본적인 CRUD 동작을 쉽게 처리할 수 있다. |
| 사용 용도 | 세부적인 동작을 세밀하게 제어할 때 | 기본적인 CRUD API를 빠르게 작성할 때 |

## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)
* [Django REST Framework 공식 문서](https://www.django-rest-framework.org/)

{% endraw %}