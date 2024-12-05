---
title: Django Http 응답 클래스
category: Study
tag: [Education, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## `HttpResponse` 클래스
> `HttpResponse`는 기본적인 HTTP 응답 객체로, 클라이언트에게 직접 데이터를 반환할 때 사용됩니다.
기본적으로 HttpResponse는 텍스트 데이터를 반환합니다. 추가적으로 헤더, 상태 코드, 컨텐츠 타입을 설정할 수 있습니다.

```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, world!")
```

```python
from django.http import HttpResponse

def my_view(request):
    response = HttpResponse("This is a response with custom header.")
    response['X-Custom-Header'] = 'My Custom Value'
    return response
```

* 주요 속성
    * content: 응답 본문
    * status_code: HTTP 상태 코드 (기본값은 200)
    * headers: 응답 헤더


## `HttpResponseRedirect` 클래스
> `HttpResponseRedirect`는 클라이언트를 다른 URL로 리디렉션하는 데 사용되는 응답 객체입니다.
HTTP 상태 코드 **302 (Found)**를 반환하며, 클라이언트에게 새로운 URL로 이동하도록 지시합니다.

```python
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/new-url/')
```

## `HttpResponsePermanentRedirect` 클래스
> HttpResponsePermanentRedirect는 영구적인 리디렉션을 구현하는 데 사용됩니다. 
HTTP 상태 코드 **301 (Moved Permanently)**을 반환하며, 클라이언트에게 해당 URL이 영구적으로 이동했음을 알립니다.
일반적으로 SEO 최적화 시에 영구 리디렉션을 사용할 때 유용합니다.

```python
from django.http import HttpResponsePermanentRedirect

def permanent_redirect_view(request):
    return HttpResponsePermanentRedirect('/new-permanent-url/')
```

## `redirect()` 함수
> `redirect()`는 HttpResponseRedirect의 고수준 API로, URL, 뷰 이름, 또는 모델 인스턴스를 인수로 받아 리디렉션을 수행합니다.
이 함수는 URL을 동적으로 생성하고 리디렉션을 처리하는 데 매우 유용합니다.

```python
from django.shortcuts import redirect

def my_view(request):
    # URL로 리디렉션
    return redirect('/new-url/')

def another_view(request):
    # 뷰 이름으로 리디렉션
    return redirect('home-view')

def redirect_with_params(request):
    # 모델 인스턴스를 사용하여 리디렉션
    return redirect('model-detail-view', pk=123)
```

## `reverse()` 함수
> reverse() 함수는 URL 패턴 이름을 사용하여 해당 뷰에 대한 URL을 동적으로 생성할 수 있습니다.
이 함수는 URL을 하드코딩하지 않고, 뷰 이름을 사용하여 URL을 생성할 수 있기 때문에 URL 패턴이 변경되더라도 코드의 유연성을 유지할 수 있습니다.

```python
from django.urls import reverse
from django.http import HttpResponseRedirect

def my_view(request):
    # reverse()로 URL을 동적으로 생성한 후 리디렉션
    url = reverse('home-view', kwargs={'pk': 123})
    return HttpResponseRedirect(url)
```

## reverse_lazy() 함수
> reverse_lazy()는 reverse() 함수와 비슷하지만, 지연 평가(lazy evaluation)를 지원하는 함수입니다.
reverse_lazy()는 URL을 즉시 계산하는 대신, 실제로 사용될 때까지 계산을 미룹니다. 이는 주로 **settings.py, 클래스 기반 뷰(CBV)**에서 사용됩니다.

```python
# settings.py

LOGIN_REDIRECT_URL = reverse_lazy('home')
```

```python
# views.py

from django.urls import reverse_lazy
from django.views.generic import RedirectView

class MyRedirectView(RedirectView):
    url = reverse_lazy('home-view')
```

## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)

{% endraw %}