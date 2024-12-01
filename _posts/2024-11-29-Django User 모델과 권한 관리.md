---
title: Django User 모델과 권한 관리
category: Study
tag: [Education, Rest Framework, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## `User` 모델
> Django는 기본적으로 제공하는 `User` 모델을 통해 사용자를 관리합니다. 
이 모델은 사용자의 인증 및 권한을 처리하는 데 사용됩니다.

* 주요 필드
    * username: 사용자의 고유한 이름 (로그인 시 사용).
    * password: 사용자의 비밀번호 (해싱되어 저장됨).
    * first_name: 사용자의 이름.
    * last_name: 사용자의 성.
    * email: 사용자의 이메일 주소.
    * is_active: 사용자가 활성화 상태인지를 나타내는 Boolean 값.
    * is_staff: 관리자인지 여부를 나타내는 Boolean 값.
    * is_superuser: 슈퍼사용자 권한을 가지고 있는지 여부.
    * groups: 사용자가 속한 그룹 (그룹은 여러 권한을 묶어서 관리하는 데 사용됨).
    * user_permissions: 사용자가 가지고 있는 개별 권한.
* 이 외에도 User 모델은 로그인, 로그아웃, 패스워드 변경 등의 기본적인 인증과 관련된 기능들을 내장하고 있습니다.

```python
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
```

## `permissions` 모듈
> Django REST Framework는 API의 접근을 제어하기 위해 권한 관리를 위한 여러 클래스들을 제공합니다. 
이 클래스들은 주로 APIView나 ViewSet을 사용하는 뷰에서 사용됩니다.

### 1. AllowAny

```python
# views.py

from rest_framework.permissions import AllowAny

class MyView(APIView):
    permission_classes = [AllowAny] # 모든 사용자에게 API 접근을 허용
```

### 2. IsAuthenticated

```python
# views.py

from rest_framework.permissions import IsAuthenticated

class MyView(APIView):
    permission_classes = [IsAuthenticated] # 로그인한 사용자만 API 접근을 허용
```

### 3. IsAdminUser

```python
# views.py

from rest_framework.permissions import IsAdminUser

class MyView(APIView):
    permission_classes = [IsAdminUser] # 관리자만 API 접근을 허용
```

### 4. IsAuthenticatedOrReadOnly

```python
# views.py

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MyView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # 인증된 사용자만 데이터 변경을 할 수 있으며, 인증되지 않은 사용자는 읽기 전용으로 접근 허용
```

### 5. DjangoModelPermissions

```python
# views.py

from rest_framework.permissions import DjangoModelPermissions

class MyView(APIView):
    permission_classes = [DjangoModelPermissions] # Django의 모델 권한 시스템을 사용하여 API 접근 허용
```

## 권한 클래스 커스터마이징
> 기본 권한 클래스 외에도 Rest Framework에서는 사용자 정의 권한 클래스를 만들 수 있습니다. 
예를 들어, 특정 조건을 만족하는 사용자만 API를 사용할 수 있도록 설정할 수 있습니다.

```python
#permissions.py

from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    객체의 소유자만 접근할 수 있는 권한.
    """
    def has_object_permission(self, request, view, obj):
        # 객체의 소유자가 현재 요청한 사용자일 경우만 허용
        return obj.owner == request.user
```

```python
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwner # 사용자 정의 권한 클래스

class MyModelDetailView(APIView):
    permission_classes = [IsOwner]

    def get(self, request, *args, **kwargs):
        # 객체 가져오기
        obj = MyModel.objects.get(id=kwargs['pk'])
        self.check_object_permissions(request, obj)  # 권한 검사
        return Response({'data': obj})
```

## User와 권한의 관계
> User는 인증과 관련된 정보를 담고 있으며, 권한은 그 사용자가 무엇을 할 수 있는지를 결정합니다.
기본적인 권한 클래스(IsAuthenticated, IsAdminUser 등)는 User 객체의 속성들을 기반으로 API에 대한 접근을 제어합니다.

```python
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class MyModelView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user  # 인증된 사용자
        return Response({'message': f'Hello, {user.username}!'})
```

## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)
* [Django REST Framework 공식 문서](https://www.django-rest-framework.org/)

{% endraw %}