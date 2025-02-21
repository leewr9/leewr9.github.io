---
title: Generic Views
category: Django
tag: [Python, Django]
---

> Django에서는 웹 애플리케이션의 다양한 요청에 대해 기본적으로 사용할 수 있는 Generic Views를 제공합니다. 이 뷰들은 반복적인 코드 작성을 줄여주며, 다양한 상황에서 쉽게 재사용할 수 있습니다.

---

## Display View
Django의 `Generic Views`는 다양한 데이터를 출력할 때 유용하게 사용됩니다. 그 중 `ListView`와 `DetailView`는 매우 자주 사용되는 뷰입니다.

- `model`: 데이터를 출력할 모델을 지정합니다.
- `template_name`: 데이터를 출력할 템플릿을 지정합니다.
- `context_object_name`: 템플릿에서 사용할 변수 이름을 지정합니다.

```python
# urls.py

from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'), 
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
```

### ListView
`ListView`는 특정 모델의 객체 목록을 출력하는 뷰입니다. 데이터를 한 번에 여러 개 출력할 수 있습니다.

```python
# views.py

from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
```

```html
{% raw %}
<!-- book_list.html -->

<ul>
  {% for book in books %}
    <li>{{ book.title }}</li>
  {% endfor %}
</ul>
{% endraw %}
```

### DetailView
`DetailView`는 특정 모델의 객체를 하나씩 출력하는 뷰입니다. 개별 객체의 세부 정보를 확인할 수 있습니다.

```python
# views.py

from django.views.generic import DetailView
from .models import Book

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
```

```html
{% raw %}
<!-- book_detail.html -->

<h1>{{ book.title }}</h1>
<p>{{ book.description }}</p>
{% endraw %}
```

---

## CRUD View 
Django에서는 `Create`, `Read`, `Update`, `Delete` 작업을 쉽게 처리할 수 있는 여러 `Generic Views`를 제공합니다.

- `model`: 데이터를 저장할 모델을 지정합니다.
- `fields`: 입력 받을 필드를 지정합니다.
- `success_url`: 데이터가 저장된 후 리디렉션할 URL을 지정합니다. 

```python
# urls.py

from django.urls import path
from .views import BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'), 
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
```

### CreateView
`CreateView`는 데이터를 생성할 때 사용됩니다. 폼을 자동으로 제공하고, 제출된 데이터를 데이터베이스에 저장합니다.

```python
# views.py

from django.views.generic import CreateView
from .models import Book
from django.urls import reverse_lazy

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('book_list')
```
여기서는 `reverse_lazy`를 사용하여 URL을 동적으로 생성합니다.

### UpdateView
`UpdateView`는 이미 존재하는 데이터를 수정할 때 사용됩니다.

```python
# views.py

from django.views.generic import UpdateView
from .models import Book
from django.urls import reverse_lazy

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('book_list')
```

### DeleteView
`DeleteView`는 데이터를 삭제할 때 사용됩니다.

```python
# views.py

from django.views.generic import DeleteView
from .models import Book
from django.urls import reverse_lazy

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
```

---

## Dynamic URL

### RedirectView
`RedirectView`는 사용자를 다른 페이지로 리디렉션할 때 사용됩니다. 주로 다른 URL로의 자동 이동을 구현할 때 유용합니다.

```python
# urls.py

from django.urls import path
from .views import BookRedirectView

urlpatterns = [
    path('books/', BookRedirectView.as_view(), name='book_redirect'),
]
```

```python
# views.py

from django.views.generic import RedirectView

class BookRedirectView(RedirectView):
    url = '/book-redirect/'
```

- `url`: 리디렉션할 URL을 지정합니다. 사용자가 `books/`로 접근하면, `/book-redirect/`로 자동으로 이동됩니다.

### reverse
요청을 처리하는 동안 URL을 즉시 생성합니다. 주로 뷰 함수 내에서 사용됩니다.

```python
# views.py

from django.urls import reverse
from django.http import HttpResponseRedirect

def my_view(request):
    url = reverse('book_list') # URL을 동적으로 생성
    return HttpResponseRedirect(url)
```

### reverse_lazy
URL이 요청될 때까지 생성하지 않고, 지연시키는 방식입니다. 주로 클래스 기반 뷰에서 사용됩니다.
`reverse_lazy`는 클래스 기반 뷰에서 URL을 동적으로 생성할 때 유용합니다.

```python
# views.py

from django.urls import reverse_lazy
from django.views.generic import RedirectView

class MyRedirectView(RedirectView):
    url = reverse_lazy('book_list') # URL을 지연시켜 동적으로 생성
```

---

## References
- [Django 공식 문서](https://www.djangoproject.com/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
