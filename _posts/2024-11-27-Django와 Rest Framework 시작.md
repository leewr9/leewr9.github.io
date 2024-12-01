---
title: Django와 Rest Framework 시작
category: Study
tag: [Education, Rest Framework, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}


## Django / Rest Framwork 셋팅

### 1. 설치
```bash
pip install django
pip install djangorestframework
```

### 2. 가상환경 설정

```bash
# 가상환경 생성 (myvenv는 가상환경 이름, 변경가능)
python -m venv myvenv

# 가상환경 활성화
venv\Scripts\activate # Windows
source venv/bin/activate # macOS/Linux

#가상환경 비활성화
deactivate
```

```bash
pip freeze > requirements.txt # 가상환경 모듈 파일 생성
pip install -r requirements.txt # 가상환경 모듈 설치
```

| 이유 | 설명 |
| - | - |
| 패키지 충돌 방지 | 프로젝트마다 별도의 패키지 버전 관리 가능 |
| 전역 환경 오염 방지 | 전역 파이썬 환경을 오염시키지 않음 |
| 이식성 및 재현성 보장 | requirements.txt로 동일한 환경을 쉽게 재현 가능 |
| 배포 및 관리 용이성 | 배포 서버에서도 동일한 환경을 유지 가능 |
| 다중 프로젝트 관리 | 여러 프로젝트를 독립적으로 관리 가능 |

## 프로젝트 생성하기
* Django 프로젝트를 시작하려면 다음 명령어를 사용합니다.
* 명령 실행 후 프로젝트 디렉터리가 생성됩니다.
* 프로젝트 디렉터리 내부의 settings.py에 Rest Framework을 등록합니다.

```bash
django-admin startproject myproject # myproject는 프로젝트 이름, 변경가능
```

```python
# myproject/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # djangorestframework 등록
]
```

### 1. 앱 생성하기
* 프로젝트 안에서 특정 기능을 수행하는 앱을 생성하려면 다음을 실행합니다.

```bash
python manage.py startapp myapp # myapp은 앱 이름, 변경가능
```

### 2. 경로 설정하기
* `urls.py`에서 URL 경로를 설정하여 뷰와 연결할 수 있습니다.
* 해당 파일이 없을 경우에는 직접 생성합니다.

```python
# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # myapp의 URL 설정 포함
]
```

```python
# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 루트 URL에 대해 home 뷰 연결
]
```

### 3. 뷰 생성하기

```python
# myapp/views.py

from django.http import HttpResponse  # HttpResponse 객체 사용

def home(request):
    return HttpResponse("Welcome to the Home Page!") # 단순한 문자열 응답
```

## 모델 만들기
* `models.py`에서 데이터베이스 테이블과 매핑되는 모델을 정의합니다.
* 모델 필드 종류
  * CharField: 문자열 필드
  * TextField: 긴 텍스트 필드
  * IntegerField: 정수 필드
  * FloatField: 소수점 필드
  * BooleanField: 참/거짓 필드
  * DateTimeField: 날짜 및 시간 필드

```python
# myapp/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    stock = models.IntegerField()
    price = models.FloatField()
    on_sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

### 1. 마이그레이션 (Migration)
* `settings.py`에서 앱을 등록해야 Django가 해당 앱을 인식하고 마이그레이션을 실행할 수 있습니다.

```python
# myproject/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig',  # 앱 등록 필수
]
```

* 모델 변경사항 추적 - makemigrations 실행
* 이 명령은 모델 변경사항을 감지하고, 마이그레이션 파일을 생성합니다.

``` bash
python manage.py makemigrations

# Migrations for 'myapp':
#   myapp/migrations/0001_initial.py
#     - Create model Product
```

* 데이터베이스에 적용 - migrate 실행
* 이 명령은 생성된 마이그레이션 파일을 사용하여 데이터베이스에 테이블을 생성합니다.

``` bash
python manage.py migrate

# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions, myapp
# Running migrations:
#   Applying myapp.0001_initial... OK
```

### 2. 데이터베이스 접속하기
```bash
sqlite3 db.sqlite3

# SQLite version 3.x.x
# Enter ".help" for usage hints.
# sqlite> .tables
# auth_group                  myapp_product
# auth_group_permissions      django_admin_log
# auth_permission             django_content_type
# ...
# sqlite> SELECT * FROM myapp_product;
# 1|Sample Product|Description|100|10.5|0|2024-11-30 12:00:00
# sqlite> .exit
```

* 기본 명령어
    * .tables: 데이터베이스 내의 모든 테이블 목록 보기
    * .schema <테이블명>: 특정 테이블의 스키마(구조) 보기
    * .exit: SQLite3 종료

## 관리자 계정 관리하기

### 1. 계정 생성
* 관리자 계정을 생성하려면 다음 명령어를 실행합니다:

```bash
python manage.py createsuperuser
```
> 명령어를 실행하면 사용자 이름, 이메일, 비밀번호를 설정합니다.

### 2. 모델 등록
* 관리자 페이지에서 모델을 관리하려면 `admin.py`에 모델을 등록해야 합니다.

```python
# myapp/admin.py

from django.contrib import admin
from .models import Product

admin.site.register(Product)
```

## Shell 사용하기
* 장고 셸을 사용하여 데이터베이스와 상호 작용하려면 다음 명령어를 실행합니다:

```bash
python manage.py shell
```

### 1. 현재 시간
* Django 셸에서 시간을 가져오려면 다음을 실행합니다.

```python
from django.utils.timezone import now
print(now()) # 2024-11-27 00:00:00.000000+00:00
```

#### TIME_ZONE 설정
* `settings.py`에서 TIME_ZONE 항목을 다음과 같이 설정하세요.

```python
# myproject/settings.py

TIME_ZONE = 'Asia/Seoul'
USE_TZ = True  # True로 설정하면 UTC 기반으로 저장되고 KST로 변환됩니다.
```

* TIME_ZONE: 'Asia/Seoul'로 설정하면 KST(한국 표준시)로 변경됩니다.
* USE_TZ 옵션 설명
  * USE_TZ = True: UTC를 기본으로 사용하고, TIME_ZONE에 맞춰 변환합니다.
  * USE_TZ = False: 데이터베이스에 로컬 시간(설정된 TIME_ZONE)으로 저장합니다.

```python
from django.utils.timezone import now, localtime

print(now())  # UTC 2024-11-27 00:00:00.000000+00:00
print(localtime(now()))  # KST 2024-11-27 09:00:00.000000+09:00
```

### 2. 모델 관리
* Django 셸에서 모델의 인스턴스를 관리할 수 있습니다.

#### 객체 생성
* 새로운 Product 객체를 생성하고 데이터베이스에 저장할 수 있습니다. 
* 아래 예시에서는 Product 객체를 생성하고 save() 메서드를 사용해 데이터베이스에 저장합니다.
* save() 메서드를 사용하면 데이터베이스에 새로운 레코드가 저장됩니다. id는 자동으로 생성된 Primary Key입니다.

```python
from myapp.models import Product

# 새 Product 객체 생성
new_product = Product(
    name="New Product",
    description="This is a description of the new product.",
    stock=100,
    price=29.99
)

# 데이터베이스에 저장
new_product.save()

# 생성된 객체 확인
print(new_product.id)  # 생성된 객체의 id 확인
```

#### 여러 객체 생성
* bulk_create()를 사용하여 여러 개의 객체를 한 번에 생성할 수도 있습니다.
* bulk_create()는 여러 객체를 한 번에 생성하고 데이터베이스에 저장하는 방법입니다.
* 단, 해당 메서드는 데이터베이스에 바로 저장하는 방법이기에 별도 다른 행동을 취할 수 없습니다.

```python
# 여러 Product 객체 생성
product1 = Product(name="Product 1", description="Desc 1", stock=50, price=9.99, on_sale=True)
product2 = Product(name="Product 2", description="Desc 2", stock=150, price=19.99, on_sale=False)

# 한 번에 저장
Product.objects.bulk_create([product1, product2])
```

#### 객체 조회
* Product 객체를 조회할 때 get(), filter() 메서드를 사용하여 데이터를 조회할 수 있습니다.
* get()은 조건에 맞는 단일 객체를 반환하며, 만약 조건에 맞는 객체가 없거나 여러 개 존재할 경우 `DoesNotExist` 예외가 발생합니다.

```python
from myapp.models import Product

# 모든 Product 객체 조회
products = Product.objects.all()

for product in products:
    print(product.name, product.price)  # 조회된 객체의 필드 출력
    
# 특정 조건에 맞는 Product 조회 (예: 이름이 'New Product'인 제품)
product = Product.objects.get(name="New Product")

print(product.name, product.price)  # 조회된 객체의 필드 출력
```

#### 객체 수정
* Product 객체를 수정하려면 먼저 해당 객체를 조회한 후, 변경하려는 필드를 수정하고 save() 메서드를 호출합니다.
* save() 메서드를 호출하면 기존의 객체가 수정되어 데이터베이스에 저장됩니다.

```python
from myapp.models import Product

# 'New Product' 객체 조회
product = Product.objects.get(name="New Product")

# 필드 값 수정
product.price = 19.99
product.stock = 150

# 변경 사항을 데이터베이스에 저장
product.save()

# 수정된 객체 확인
print(product.name, product.price, product.stock)
```

#### 객체 삭제
* Product 객체를 삭제하려면 해당 객체를 조회한 후 delete() 메서드를 호출합니다.
* delete() 메서드를 호출하면 해당 객체가 데이터베이스에서 삭제됩니다.

```python
from myapp.models import Product

# 'New Product' 객체 조회
product = Product.objects.get(name="New Product")

# 객체 삭제
product.delete()

# 삭제 후 확인
print("Deleted product:", product.name)
```

## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)

{% endraw %}