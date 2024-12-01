---
title: Django View와 Template을 사용한 렌더링
category: Study
tag: [Education, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## 뷰 (View)
> 뷰(View)는 사용자의 요청을 처리하고, 처리된 데이터를 템플릿에 전달하는 역할을 합니다. 뷰는 주로 `views.py` 파일에 정의됩니다.

### 1. 뷰 함수
* 뷰 함수는 HTTP 요청을 처리하고 HTTP 응답을 반환하는 함수입니다.

```python
# views.py

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to the Home Page!")
```

### 2. 템플릿 렌더링
* 뷰에서 템플릿을 렌더링하려면 render() 함수를 사용합니다. render() 함수는 템플릿을 렌더링하고, 그 결과를 HTTP 응답으로 반환합니다.

```python
# views.py

from django.shortcuts import render

def home(request):
    context = {'name': 'John'}
    return render(request, 'home.html', context)
```

### 3. 클래스 기반 뷰
* Django는 함수 기반 뷰뿐만 아니라 클래스 기반 뷰(Class-Based Views, CBV)를 제공합니다. 
* 클래스 기반 뷰는 좀 더 구조화된 방식으로 뷰를 작성할 수 있게 해줍니다.

```python
# views.py

from django.views import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request):
        context = {'name': 'John'}
        return render(request, 'home.html', context)
```

## 템플릿 (Template)
> 템플릿은 HTML 파일로, 뷰에서 전달된 데이터를 사용자에게 보여주는 역할을 합니다. 
Django 템플릿 시스템은 템플릿 언어를 사용하여 동적인 콘텐츠를 삽입할 수 있습니다.

### 1. 템플릿 문법
* 템플릿에서 데이터는 **{{}}**을 사용하여 삽입합니다. 이를 통해 뷰에서 전달된 변수를 HTML로 렌더링할 수 있습니다.

```html
<!-- home.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home Page</title>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
</body>
</html>
```

### 2. 템플릿 태그
* 템플릿에서 제어문이나 반복문을 사용할 때는 템플릿 태그 **{% %}**를 사용합니다. 
* 예를 들어, for 반복문, if 조건문 등을 사용하여 동적 콘텐츠를 렌더링할 수 있습니다.

* if 태그

```html
{% if user_is_logged_in %}
    <p>Welcome back, {{ username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

* for 태그

```html
<ul>
    {% for product in products %}
        <li>{{ product.name }} - ${{ product.price }}</li>
    {% endfor %}
</ul>
```

### 3. 템플릿 필터
* 템플릿에서는 필터를 사용하여 데이터를 변환할 수 있습니다. 필터는 {{ value │ filter_name }} 형식으로 사용됩니다.

```html
<p>{{ user.date_of_birth | date:"Y-m-d" }}</p>
```

### 4. 템플릿 상속
* Django 템플릿 시스템은 템플릿 상속을 지원합니다. 이를 통해 반복되는 레이아웃을 효율적으로 관리할 수 있습니다.
* extends는 부모 템플릿을 상속하고, block 태그를 사용하여 부모 템플릿의 일부를 덮어쓸 수 있습니다.

```html
<!-- base.html -->

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Site</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

```html
<!-- home.html -->

{% extends 'base.html' %}

{% block title %}Home Page{% endblock %}

{% block content %}
    <h2>Welcome to the Home Page!</h2>
    <p>{{ name }}</p>
{% endblock %}
```

## 뷰와 템플릿 사용
### 1. URL 연결하기
* 뷰와 템플릿을 URL과 연결하려면 `urls.py`에서 URL 패턴을 정의합니다.

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home 뷰와 연결
    path('detail/', views.product_detail, name='detail'),  # product_detail 뷰와 연결
    path('list/', views.product_list, name='list'),  # product_list 뷰와 연결
]
```

### 2. if 조건문
```python
# views.py

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})
```

```html
<!-- product_detail.html -->

<h1>{{ product.name }}</h1>
<p>{% if product.stock > 0 %}In Stock{% else %}Out of Stock{% endif %}</p>
```

### 3. for 반복문
```python
# views.py

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
```

```html
<!-- product_list.html -->
<ul>
    {% for product in products %}
        <li>{{ product.name }} - ${{ product.price }}</li>
    {% endfor %}
</ul>
```

## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)

{% endraw %}