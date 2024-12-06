---
title: Django Class 기반 뷰
category: Study
tag: [Education, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## `View` 클래스란?
> `View` 클래스는 Django에서 모든 클래스 기반 뷰의 최상위 클래스입니다. 
View를 상속받아 **HTTP 메서드(GET, POST 등)**에 맞는 처리 로직을 정의할 수 있습니다.

* 특징
    * 상속 및 메서드 오버라이딩: View 클래스를 상속받고, get(), post(), put(), delete() 등의 메서드를 오버라이드하여 각 HTTP 메서드에 대한 처리를 정의합니다.
    * 구조적이고 유연함: 클래스 기반 뷰를 사용하면 HTTP 메서드에 대한 처리를 각 메서드 내에서 분리하여 처리할 수 있기 때문에, 코드가 더 구조적이고 유지보수하기 용이해집니다.
    * 클래스 기반 뷰의 기본: View 클래스를 직접 상속받지 않고 TemplateView나 DetailView 같은 Django의 제네릭 뷰를 사용할 수도 있습니다.

```python
# views.py

from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("GET 요청을 처리하는 클래스 기반 뷰")
    
    def post(self, request, *args, **kwargs):
        return HttpResponse("POST 요청을 처리하는 클래스 기반 뷰")
```

### 1. Generic View
#### ListView
> ListView는 특정 모델의 객체 목록을 조회하고 보여주는 뷰입니다.

```python
# views.py
from django.views.generic import ListView
from .models import MyModel

class MyModelListView(ListView):
    model = MyModel
    template_name = 'myapp/my_model_list.html'  # 렌더링할 템플릿 파일
    context_object_name = 'my_model_list'  # 템플릿에서 사용할 컨텍스트 변수명 (기본값은 object)
```

```html
<!-- my_model_list.html -->

<h1>MyModel List</h1>
<ul>
    {% for obj in my_model_list %}
        <li><a href="{% url 'my_model_detail' obj.pk %}">{{ obj.name }}</a></li>
    {% endfor %}
</ul>
<a href="{% url 'my_model_create' %}">Create New</a>
```

#### DetailView
> DetailView는 모델의 개별 객체를 상세히 보여주는 뷰입니다.

```python
# views.py
from django.views.generic import DetailView
from .models import MyModel

class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'myapp/my_model_detail.html' # 렌더링할 템플릿 파일
    context_object_name = 'my_model' # 템플릿에서 사용할 컨텍스트 변수명 (기본값은 object)
```

```html
<!-- my_model_detail.html -->

<h1>{{ my_model.name }}</h1>
<p>{{ my_model.description }}</p>
<a href="{% url 'my_model_update' my_model.pk %}">Edit</a>
<a href="{% url 'my_model_delete' my_model.pk %}">Delete</a>
```

#### CreateView
> CreateView는 새로운 객체를 생성할 수 있는 뷰입니다. 폼을 통해 사용자로부터 입력을 받아 객체를 저장합니다.

```python
# views.py
from django.views.generic import CreateView
from .models import MyModel
from django.urls import reverse_lazy

class MyModelCreateView(CreateView):
    model = MyModel
    template_name = 'myapp/my_model_form.html' # 렌더링할 템플릿 파일
    fields = ['name', 'description']  # 폼에서 사용할 필드들
    success_url = reverse_lazy('my_model_list')  # 저장 후 이동할 URL
```

```html
<!-- my_model_form.html -->

<h1>{% if object %}Edit{% else %}Create{% endif %} MyModel</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
```

#### UpdateView
> UpdateView는 기존 객체를 수정하는 뷰입니다. 주로 객체의 정보를 수정할 때 사용됩니다.

```python
# views.py
from django.views.generic import UpdateView
from .models import MyModel
from django.urls import reverse_lazy

class MyModelUpdateView(UpdateView):
    model = MyModel
    template_name = 'myapp/my_model_form.html' # 렌더링할 템플릿 파일
    fields = ['name', 'description']  # 수정할 필드들
    success_url = reverse_lazy('my_model_list')  # 수정 후 이동할 URL
```

```html
<!-- my_model_form.html -->

<h1>{% if object %}Edit{% else %}Update{% endif %} MyModel</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
```

#### DeleteView
> DeleteView는 객체를 삭제하는 뷰입니다. 객체 삭제 전에 확인 페이지를 제공하는 것이 일반적입니다.

```python
# views.py
from django.views.generic import DeleteView
from .models import MyModel
from django.urls import reverse_lazy

class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'myapp/my_model_confirm_delete.html' # 렌더링할 템플릿 파일
    success_url = reverse_lazy('my_model_list')  # 삭제 후 이동할 URL
```

```html
<!-- my_model_confirm_delete.html -->

<h1>Are you sure you want to delete {{ object.name }}?</h1>
<form method="post">
    {% csrf_token %}
    <button type="submit">Yes, delete</button>
</form>
<a href="{% url 'my_model_list' %}">Cancel</a>
```

### 2. as_view()
> View 클래스나 그 하위 클래스에서 뷰 인스턴스를 생성하려면 as_view() 메서드를 호출해야 합니다. 
as_view()는 뷰를 인스턴스화하고 HTTP 요청을 처리할 준비가 된 콜러블 객체를 반환합니다.

```python
# urls.py

from django.urls import path
from .views import MyView

urlpatterns = [
    path('my-view/', MyView.as_view(), name='my-view'),
]
```

## RedirectView 클래스
> RedirectView는 리디렉션을 처리하는 클래스 기반 뷰입니다. 주로 URL을 다른 URL로 리디렉션하는 기능을 구현할 때 사용됩니다. 
RedirectView는 리디렉션 대상 URL을 정의하고, 특정 조건에 맞는 요청에 대해 자동으로 리디렉션 응답을 반환합니다.

* 특징
    * 리디렉션 처리: RedirectView는 상수 URL로 리디렉션하거나, 동적으로 URL을 생성하여 리디렉션할 수 있습니다.
    * 간단한 리디렉션: 주로 URL을 다른 위치로 리디렉션하는 데 사용되며, HttpResponseRedirect나 HttpResponsePermanentRedirect와 같은 리디렉션을 간소화할 수 있습니다.
    * url 속성 또는 pattern_name 속성: RedirectView는 리디렉션할 URL을 url 속성에 하드코딩하거나, URL 패턴 이름을 pattern_name 속성에 지정하여 URL을 동적으로 생성할 수 있습니다.

### 1. 고정 URL 리디렉션
```python
# views.py

from django.views.generic import RedirectView

class MyRedirectView(RedirectView):
    url = '/new-url/'
```

```python
# urls.py

from django.urls import path
from .views import MyRedirectView

urlpatterns = [
    path('old-url/', MyRedirectView.as_view(), name='old-url'), # new-url로 연결
]
```

### 2. 동적 URL 리디렉션

```python
# views.py
from django.views.generic import RedirectView

class DynamicRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # URL 패턴의 일부를 동적으로 생성
        return f'/profile/{kwargs["username"]}/'
```

```python
# urls.py
from django.urls import path
from .views import DynamicRedirectView

urlpatterns = [
    path('user/<str:username>/', DynamicRedirectView.as_view(), name='user-profile'), # profile/username으로 연결
]
```

## RedirectView의 permanent 속성
> RedirectView는 영구 리디렉션을 위해 permanent 속성을 사용하여 **301 (Moved Permanently)** 상태 코드를 반환할 수 있습니다. 
기본적으로 RedirectView는 **302 (Found)** 상태 코드를 반환하지만, permanent=True로 설정하면 301 상태 코드로 리디렉션됩니다.


```python
# views.py
from django.views.generic import RedirectView

class PermanentRedirectView(RedirectView):
    url = '/new-url/'
    permanent = True  # 301 상태 코드로 리디렉션
```

## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)

{% endraw %}