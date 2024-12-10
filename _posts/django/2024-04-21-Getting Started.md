---
title: Getting Started
category: Django
tag: [Python, Django]
---

> Django는 Python 기반의 고급 웹 프레임워크로, 웹 애플리케이션을 빠르고 효율적으로 개발할 수 있도록 돕습니다. Django는 "배터리 포함(batteries-included)" 철학을 가지고 있어, 기본적으로 제공되는 데이터베이스 관리, URL 라우팅 등을 활용하여 개발자는 핵심 비즈니스 로직에 집중할 수 있습니다.

---

## Project Manager
- 빠른 개발: Django는 프로젝트를 빠르게 시작하고 운영할 수 있도록 설계되었습니다. 덕분에 개발자는 웹 애플리케이션을 효율적으로 구축할 수 있습니다.
- 보안: Django는 SQL 인젝션, 크로스 사이트 스크립팅(XSS), 크로스 사이트 요청 위조(CSRF)와 같은 보안 취약점으로부터 애플리케이션을 보호하는 기능을 제공합니다.
- 확장성: Django는 고성능 웹 애플리케이션을 구축할 수 있도록 설계되어 있으며, 대규모 트래픽을 처리할 수 있습니다.
- 관리자 인터페이스: Django는 자동으로 관리자 인터페이스를 생성해 줍니다. 이를 통해 관리자는 애플리케이션의 데이터를 직관적으로 관리할 수 있습니다.

```bash
pip install django

# 새로운 프로젝트 생성
django-admin startproject myproject
cd myproject

# 새로운 앱 생성
python manage.py startapp myapp

# 서버 실행
python manage.py runserver
```

---

## Structure
Django 프로젝트는 명확하게 정의된 디렉터리 구조를 가지고 있습니다.

```plaintext
myproject/
│
├── manage.py         # Django 명령어 실행 파일
│
├── myproject/        # 설정 파일들이 포함된 디렉터리
│   ├── __init__.py
│   ├── settings.py   # 프로젝트 설정
│   ├── urls.py       # URL 라우팅 설정
│   ├── asgi.py       # ASGI 설정
│   └── wsgi.py       # WSGI 설정
│
└── myapp/            # Django 앱 디렉터리
    ├── migrations/   # 데이터베이스 마이그레이션 파일
    ├── __init__.py
    ├── admin.py      # 관리자 인터페이스 설정
    ├── apps.py       # 앱 설정
    ├── models.py     # 데이터베이스 모델
    ├── tests.py      # 테스트 파일
    └── views.py      # 뷰 함수 설정
```

---

## Configuration
`settings.py` 파일은 Django 프로젝트의 핵심 설정 파일로, 프로젝트의 다양한 설정을 관리합니다.

### DEBUG
개발 중 디버깅을 활성화할지 여부를 설정합니다.

```python
DEBUG = True # 디버깅 모드 활성화
```

### DATABASES
데이터베이스 설정을 관리합니다. 기본적으로 `SQLite`가 설정되어 있지만, `MySQL`, `PostgreSQL` 등을 사용할 수도 있습니다.

* SQLite
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

* MySQL
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```
### INSTALLED_APPS
프로젝트에 포함된 앱 목록을 설정합니다.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp', # 내가 만든 앱
]
```
이 외에도 `TEMPLATES`, `MIDDLEWARE`, `STATIC_URL` 등 다양한 설정 항목이 포함되어 있습니다.

---

## URL Pattern Mapping
Django는 URL을 처리할 뷰 함수에 매핑하는 시스템을 제공합니다. 
`urls.py` 파일에서 URL 패턴을 정의하고, 각 URL에 해당하는 뷰를 지정합니다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 홈 페이지 URL
    path('about/', views.about, name='about'), # about 페이지 URL
]
```
위 예시에서는 `home`과 `about` 뷰를 각각의 URL에 연결하고 있습니다. `urlpatterns` 목록에 추가되는 각 항목은 URL 경로와 그에 해당하는 뷰 함수를 매핑합니다.

---

## View Request Flow
Django의 뷰(Views)는 사용자의 요청에 대한 응답을 처리하는 함수 또는 클래스를 의미합니다. `views.py` 파일에서 요청에 대해 적절한 HTML 페이지를 반환하거나 데이터를 반환하는 등의 작업을 정의할 수 있습니다.

![](\assets\posts\2024-04-21-Getting Started\home.png)
![](\assets\posts\2024-04-21-Getting Started\about.png)
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page")

def about(request):
    return HttpResponse("About Us")
```
- 사용자가 URL을 통해 요청을 보냅니다.
- Django는 `urls.py`에 정의된 내용을 통해 요청을 어떤 뷰 함수가 처리할지 결정합니다.
- 해당 뷰 함수는 요청을 처리하고, 보통 HTML 페이지나 데이터를 반환합니다.
- 브라우저는 반환된 데이터를 사용자에게 표시합니다.

---

## References
- [Django 공식 문서](https://www.djangoproject.com/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
