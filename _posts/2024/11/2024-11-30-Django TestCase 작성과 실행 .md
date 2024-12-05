---
title: Django TestCase 작성과 실행
category: Study
tag: [Education, Rest Framework, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## `TestCase` 클래스란?
> TestCase는 Django의 내장 테스트 클래스입니다. 
Django 애플리케이션에서 모델, 뷰, 폼, 템플릿 등을 테스트하기 위한 환경을 제공합니다.

* 주요 특징
    * Django의 테스트 데이터베이스를 자동으로 생성하고, 각 테스트마다 초기화하여 테스트 간 독립성을 보장합니다.
    * ORM을 통해 데이터베이스와의 상호작용을 테스트할 수 있습니다.
    * HTTP 요청 시 Django의 내부 테스트 클라이언트를 제공합니다.

```python
# tests.py

from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        # 테스트 데이터 생성
        MyModel.objects.create(name="Test1", age=25)
        MyModel.objects.create(name="Test2", age=30)

    def test_model_creation(self):
        # 객체 수 확인
        self.assertEqual(MyModel.objects.count(), 2)

    def test_model_field(self):
        # 특정 객체 필드 값 확인
        obj = MyModel.objects.get(name="Test1")
        self.assertEqual(obj.age, 25)

    def tearDown(self):
        # 테스트 데이터 삭제 
        MyModel.objects.all().delete()
```

* 주요 메서드
    * setUp(): 각 테스트 전에 실행되며, 테스트에 필요한 초기 데이터를 설정합니다.
    * tearDown(): 각 테스트 후에 실행되며, 리소스를 정리하거나 초기화합니다.
* assertEqual(), assertTrue(), assertFalse() 등의 다양한 단언 메서드를 제공합니다.

## `APITestCase` 클래스란?
> APITestCase는 **Django REST Framework (DRF)**에서 제공하는 테스트 클래스입니다. 
RESTful API의 요청과 응답을 테스트하는 데 특화되어 있습니다.

* 주요 특징
    * TestCase를 상속하며, DRF의 API 클라이언트(self.client)를 제공합니다.
    * HTTP 메서드(GET, POST, PUT, DELETE)를 사용한 API 테스트가 가능하며, JSON 데이터를 처리할 수 있습니다.
    * REST API의 응답 상태 코드와 JSON 데이터 검증에 유용합니다.

```python
# tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class UserAPITestCase(APITestCase):
    def setUp(self):
        # 테스트 유저 생성
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

    def test_get_user_list(self):
        # GET 요청 테스트
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        # POST 요청 테스트
        data = {"username": "newuser", "password": "newpassword"}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def tearDown(self):
        # 테스트 유저 삭제 
        User.objects.all().delete()
```

* 주요 메서드
    * self.client.get(): GET 요청을 보냅니다.
    * self.client.post(): POST 요청을 보냅니다.
    * self.client.put(): PUT 요청을 보냅니다.
    * self.client.delete(): DELETE 요청을 보냅니다.
* self.assertEqual(), self.assertContains(), self.assertIn() 등 다양한 단언 메서드 제공.

## 테스트 실행 방법
```bash
myapp/
├── models.py
├── views.py
├── tests.py  # 단일 테스트 파일
└── tests/
    ├── test_models.py   # 모델 테스트
    ├── test_views.py    # 뷰 테스트
    └── test_apis.py     # API 테스트
```
### 1. 전체 테스트 실행
```bash
python manage.py test
```

### 2. 특정 앱의 테스트 실행
```bash
python manage.py test myapp
```

### 3. 특정 테스트 파일 실행
```bash
python manage.py test myapp.tests.test_models
```
### 4. 특정 테스트 클래스나 메서드 실행

```bash
python manage.py test myapp.tests.test_models.MyModelTestCase
python manage.py test myapp.tests.test_models.MyModelTestCase.test_model_creation
```

### 5. 결과 확인
* 성공

```bash
python manage.py test

# Creating test database for alias 'default'...
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.024s
# 
# OK
```

* 실패

```bash
python manage.py test

# Creating test database for alias 'default'...
# .F
# ======================================================================
# FAIL: test_model_field_value (myapp.tests.test_models.MyModelTestCase)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/path/to/myapp/tests/test_models.py", line 12, in test_model_field_value
#     self.assertEqual(obj.age, 26)
# AssertionError: 25 != 26
# 
# ----------------------------------------------------------------------
# Ran 2 tests in 0.026s
# 
# FAILED (failures=1)
```

## `TestCase`와 `APITestCase`의 차이점

| 구분 | TestCase | APITestCase |
| - | - | - |
| 제공 위치 | Django 내장 | Django REST Framework |
| 주요 목적	| 모델, 뷰, 폼 등 Django 내부 기능 테스트 | REST API의 요청 및 응답 테스트 |
| 클라이언트 | Django의 self.client 사용 | Rest Framwork의 API 클라이언트 사용 |
| 데이터 포맷 | 주로 HTML 응답 확인 | 주로 JSON 데이터 응답 확인 |
| 사용 메서드 | ORM을 활용한 데이터베이스 상태 검증 | REST API의 응답 상태 코드 및 JSON 데이터 검증 |

## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)
* [Django REST Framework 공식 문서](https://www.django-rest-framework.org/)

{% endraw %}