---
title: Testing and API
category: Django
tag: [REST Framework, Python, Django]
---

> Django는 웹 애플리케이션을 개발할 때 중요한 부분 중 하나인 테스트를 매우 잘 지원합니다. 테스트를 작성함으로써 코드의 안정성을 높이고, 예상치 못한 버그를 방지할 수 있습니다.

---

## TestCase
Django는 내장된 `unittest` 프레임워크를 사용하여 테스트를 작성하고 실행할 수 있게 지원합니다. Django 프로젝트에서 테스트는 `tests.py` 파일에 작성됩니다. 기본적으로 `tests.py`는 Django 애플리케이션 디렉토리 내에 위치하며, 여기에 테스트 케이스를 작성합니다.

```python
# tests.py

from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        # 데이터 모델 생성
        self.obj = MyModel.objects.create(name='Test')

    def test_model_creation(self):
        # 모델 객체가 제대로 생성되었는지 확인
        self.assertEqual(self.obj.name, 'Test')
```

```bash
python manage.py test

# Found 1 test(s).
# Creating test database for alias 'default'...
# System check identified no issues (0 silenced).
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
# 
# OK
# Destroying test database for alias 'default'...
```

Django는 `TestCase` 클래스를 제공하여 데이터베이스의 변경 사항을 테스트 환경에서 안전하게 처리할 수 있습니다. `TestCase`는 여러 테스트 메서드(test_로 시작하는 메서드)로 구성되며, 각 테스트 메서드는 독립적으로 실행됩니다.

- `setUp()`: 각 테스트 전에 실행되는 메서드로, 테스트에 필요한 데이터를 준비하는 역할을 합니다.
- `tearDown()`: 각 테스트 후 실행되는 메서드로, 리소스를 정리하거나 초기화하는 데 사용됩니다.
- `assertEqual()`, `assertTrue()` 등의 다양한 검증 메서드를 사용하여 테스트 결과를 확인합니다.

### Model
모델 테스트는 Django에서 데이터베이스의 데이터가 예상대로 처리되는지 확인하는 중요한 부분입니다. 모델을 테스트할 때는 객체 생성, 필드 값 검증, 데이터베이스 저장 등을 검증할 수 있습니다.

```python
# tests.py

from django.test import TestCase
from .models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Laptop', price=1000)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Laptop')
        self.assertEqual(self.product.price, 1000)
    
    def test_product_discount(self):
        self.product.apply_discount(10)
        self.assertEqual(self.product.price, 900)
```

위 예시에서는 Product 모델에 대한 테스트를 작성합니다. `test_product_creation()` 메서드는 객체가 잘 생성되는지 확인하고, `test_product_discount()`는 할인 적용 로직을 검증합니다.

### View
뷰 테스트는 주로 HTTP 응답 상태 코드, 템플릿 렌더링, 컨텍스트 데이터 등을 확인하는 데 사용됩니다. Django에서는 Client 객체를 사용하여 실제 HTTP 요청을 보내고, 이에 대한 응답을 확인할 수 있습니다.

```python
# tests.py

from django.test import TestCase
from django.urls import reverse

class MyViewTest(TestCase):
    def test_view_status_code(self):
        response = self.client.get(reverse('my_view'))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('my_view'))
        self.assertTemplateUsed(response, 'my_template.html')

    def test_view_context(self):
        response = self.client.get(reverse('my_view'))
        self.assertIn('some_variable', response.context)
```

위 예시에서는 뷰 테스트를 수행합니다. `self.client.get()`을 사용하여 HTTP `GET` 요청을 보내고, 응답의 상태 코드, 템플릿, 컨텍스트를 검증합니다.

---

## APITestCase
Django REST Framework에서는 API 테스트를 작성할 때, APIClient를 사용하여 실제 HTTP 요청을 보내고 응답을 확인할 수 있습니다. 이는 API의 동작을 검증하는 중요한 과정입니다.

```python
# tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from .models import MyModel

class MyModelAPITestCase(APITestCase):
    def setUp(self):
        self.obj = MyModel.objects.create(name='Test')

    def test_model_api(self):
        url = f'/api/mymodel/{self.obj.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test')
```

위 예시에서는 `APITestCase`를 사용하여 REST API의 동작을 테스트합니다. `self.client.get()`을 통해 API에 `GET` 요청을 보내고, 응답 코드와 데이터를 검증합니다.

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
