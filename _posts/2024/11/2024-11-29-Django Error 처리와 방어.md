---
title: Django Error 처리와 방어
category: Study
tag: [Education, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## `get_object_or_404` 함수란?
> `get_object_or_404`는 주어진 모델에서 객체를 조회하고, 객체가 존재하지 않으면 404 (Not Found) 에러를 발생시키는 함수입니다. 
객체가 필수적으로 존재해야 하는 경우, 수동으로 예외 처리를 하지 않아도 자동으로 404 응답을 반환해줍니다.

```python
from django.shortcuts import get_object_or_404
from .models import MyModel

def my_view(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)
    return render(request, 'my_template.html', {'object': obj})
```

## `get_list_or_404` 함수란?
> `get_list_or_404`는 조건에 맞는 객체 리스트를 반환하며, 조건에 맞는 객체가 하나도 없을 경우 404 에러를 발생시킵니다.

```python
from django.shortcuts import get_list_or_404
from .models import MyModel

def my_list_view(request):
    objects = get_list_or_404(MyModel, is_active=True)
    return render(request, 'my_list_template.html', {'objects': objects})
```

## 커스텀 에러 처리 방법
> Django에서는 직접 예외를 처리하여 더 세밀한 에러 방어를 할 수 있습니다.

### 1. try-except 블록 사용
```python
from django.http import Http404
from .models import MyModel

def my_view(request, pk):
    try:
        obj = MyModel.objects.get(pk=pk)
    except MyModel.DoesNotExist:
        raise Http404("해당 객체를 찾을 수 없습니다.")
    return render(request, 'my_template.html', {'object': obj})
```

### 2. try-except와 redirect 조합
```python
from django.shortcuts import redirect
from .models import MyModel

def my_view(request, pk):
    try:
        obj = MyModel.objects.get(pk=pk)
    except MyModel.DoesNotExist:
        return redirect('error_page')  # 에러 페이지로 리디렉션
    return render(request, 'my_template.html', {'object': obj})
```

### 3. 커스텀 예외 처리 데코레이터 사용

```python
from django.http import JsonResponse
from functools import wraps

def handle_not_found(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)
        except MyModel.DoesNotExist:
            return JsonResponse({'error': '해당 객체를 찾을 수 없습니다.'}, status=404)
    return wrapper

@handle_not_found
def my_view(request, pk):
    obj = MyModel.objects.get(pk=pk)
    return render(request, 'my_template.html', {'object': obj})
```

## 에러 방어를 위한 팁
* get_object_or_404 사용: 간단한 객체 조회에 가장 적합.
* try-except 블록: 예외 상황에 대해 더 유연한 처리 가능.
* 커스텀 에러 페이지: handler404와 같은 설정으로 404 페이지를 커스터마이징.
* 로그 기록: logging 모듈을 사용해 예외를 기록하여 디버깅에 활용.

### 1. 커스텀 에러 페이지
```python
# urls.py

from django.conf.urls import handler404
from . import views

handler404 = 'myapp.views.custom_404_view'
```

```python
# views.py

from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
```

```html
<!-- 404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>페이지를 찾을 수 없습니다</title>
</head>
<body>
    <h1>404 - 페이지를 찾을 수 없습니다.</h1>
    <p>요청한 페이지가 존재하지 않습니다.</p>
</body>
</html>
```

## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)

{% endraw %}