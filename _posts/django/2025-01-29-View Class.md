---
title: View Class
category: Django
tag: [Python, Django]
---

> Django의 View 클래스는 웹 애플리케이션에서 매우 중요한 역할을 하며, 클라이언트의 HTTP 요청을 처리하고 적절한 HTTP 응답을 반환하는 기능을 담당합니다.이 과정을 함수 기반 뷰(FBV)나 클래스 기반 뷰(CBV)로 구현할 수 있도록 지원하여, 개발자가 필요에 따라 더 간단하거나 구조적인 방식으로 요청을 처리할 수 있도록 돕습니다.

---

## Rendering

### render
Django에서 뷰에서 템플릿으로 데이터를 전달하려면 `render`와 `context`를 사용합니다.
render는 템플릿을 렌더링하고, 컨텍스트 데이터를 HTML에 전달합니다.

```python
# views.py

from django.shortcuts import render

def my_view(request):
    context = {"message": "Hello, render"}
    return render(request, "myapp/template.html", context)
```


### TemplateResponse
`TemplateResponse`는 뷰에서 템플릿과 데이터를 결합할 때 컨텍스트 데이터를 템플릿에 전달하는 방법을 제공합니다. 이 객체는 기본적으로 `render` 함수와 비슷하지만, 템플릿을 처리할 때 더 많은 유연성을 제공합니다.

```python
# views.py

from django.template.response import TemplateResponse
from django.views import View

class MyView(View):
    def get(self, request):
        context = {"message": "Hello, TemplateResponse!"}
        return TemplateResponse(request, "myapp/template.html", context)
```

---

## Function-Based
함수 기반 뷰는 Python 함수로 뷰를 정의하는 방식입니다. `request` 방식에 따라 조건문으로 처리 가능합니다.

```python
# views.py

from django.http import HttpResponse

def my_view(request):
    if request.method == "GET":
        return HttpResponse("This is a GET request")
    elif request.method == "POST":
        return HttpResponse("This is a POST request")
```

---

## Class-Based
클래스 기반 뷰는 클래스를 사용하여 뷰를 정의합니다. 객체 지향 프로그래밍을 기반으로 작성되기 때문에, 뷰를 함수로 바로 호출할 수 없습니다. 대신, `as_view()` 메서드를 사용하여 `urls.py`에서 클래스 기반 뷰를 뷰 함수로 변환합니다.

```python
# views.py

from django.views import View
from django.http import HttpResponse

class MyView(View):
    def get(self, request):
        return HttpResponse("This is a GET request")
        
    def post(self, request):
        return HttpResponse("This is a POST request")
```

```python
# urls.py

from django.urls import path
from .views import MyView

urlpatterns = [
    path('my-view/', MyView.as_view(), name='my_view'),
]
```

---

## Error Handling
Django에서는 `404`, `500`과 같은 HTTP 에러를 커스터마이징하여 사용자가 보다 친숙한 오류 페이지를 볼 수 있도록 할 수 있습니다. 기본적으로 Django는 템플릿을 사용하여 오류 페이지를 표시합니다.

```plaintext
myproject/
    └── myapp/
        └── templates/
            └── 404.html  # 404 에러 페이지 템플릿
```

```html
<!-- 404.html -->

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Page Not Found</title>
</head>
<body>
    <h1>Sorry, the page you are looking for could not be found.</h1>
    <p>Please check the URL or go back to the <a href="/">homepage</a>.</p>
</body>
</html>
```

### handler
에러를 뷰에서 별도로 처리하려면 다음과 같이 `views.py`와 `urls.py`를 작성합니다.

```python
# views.py

from django.http import HttpResponseNotFound, HttpResponseServerError

# 404 에러 처리 함수
def custom_404(request, exception):
    return HttpResponseNotFound("Custom 404 Error: Page not found!")

# 500 에러 처리 함수
def custom_500(request):
    return HttpResponseServerError("Custom 500 Error: Server error!")
```

```python
# urls.py

from django.conf.urls import handler404, handler500

handler404 = 'myapp.views.custom_404'
handler500 = 'myapp.views.custom_500'
```

### get_object_or_404
`get_object_or_404()`는 Django에서 자주 사용되는 유용한 함수로, 특정 객체를 쿼리셋에서 가져오거나 없으면 404 오류를 발생시킵니다.

```python
# views.py

from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import MyModel

def my_view(request, pk):
    try:
        obj = get_object_or_404(MyModel, pk=pk)
    except Http404:
        return render(request, '404.html', status=404)
    
    return render(request, 'myapp/my_template.html', {'object': obj})
```
`get_object_or_404()`를 사용하여 객체를 가져오고, `Http404` 예외가 발생했을 경우 `404.html` 템플릿을 사용하여 404 페이지를 표시합니다.

---

## References
- [Django 공식 문서](https://www.djangoproject.com/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
