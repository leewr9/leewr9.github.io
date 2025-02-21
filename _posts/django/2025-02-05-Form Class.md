---
title: Form Class
category: Django
tag: [Python, Django]
---

> Django에서 Form은 사용자의 입력을 처리하고, 이를 검증하거나 변환하는 데 사용됩니다. 폼을 통해 데이터를 받아오고, 유효성 검사를 수행하며, 검증된 데이터를 모델에 저장하거나 다양한 처리를 할 수 있습니다.

---

## Using Form 
Django의 `forms.Form` 클래스를 사용하면 간단하게 HTML 폼을 생성하고 이를 처리할 수 있습니다. 이 폼 클래스는 사용자 입력을 쉽게 처리하고 검증하는 기능을 제공합니다.

```python
# forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

- `name`: 100자 이하로 입력을 받습니다.
- `email`: 이메일 형식이 맞지 않으면 오류가 발생합니다.
- `message`: 빈 값으로 제출할 수 없습니다.

```python
# views.py

from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # 폼이 유효하면 데이터를 처리
            print(form.cleaned_data)  # {'name': 'John', 'email': 'john@example.com', 'message': 'Hello'}
            # 데이터 저장 또는 이메일 전송 등
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
```

[![](\assets\posts\{{ page.name }}\form.png)](\assets\posts\{{ page.name }}\form.png)
```html
{% raw %}
<!-- contact.html -->

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
{% endraw %}
```

위 코드는 `name`, `email`, `message` 필드를 가진 폼을 생성합니다. 이 폼을 템플릿에 `as_p`를 사용하여 렌더링하면 HTML 폼 요소들이 `<p>` 태그 안에 자동으로 생성됩니다. `as_table`, `as_ul` 등의 다양한 렌더링 방식도 제공합니다.

### clean
Django는 폼 검증 기능을 제공하여 사용자가 제출한 데이터가 유효한지 `clean`나 `clean_<field_name>` 메서드를 오버라이드하여  확인할 수 있습니다.

```python
def clean(self):
    cleaned_data = super().clean()
    email = cleaned_data.get('email')
    name = cleaned_data.get('name')
    if name and email:
        if name == email:
            raise forms.ValidationError("이름과 이메일은 같을 수 없습니다.")
    return cleaned_data
    
    
def clean_email(self):
    email = self.cleaned_data.get('email')
    if "example.com" not in email:
        raise forms.ValidationError("example.com 도메인만 허용됩니다.")
    return email
```

---

## ModelForm
`ModelForm`은 Django 모델을 기반으로 자동으로 폼을 생성하는 클래스입니다. 모델과 폼을 연결하여, 데이터베이스와의 상호작용을 단순화할 수 있습니다.

예를 들어, Article 모델을 기반으로 폼을 생성하는 방법은 다음과 같습니다.

```python
# forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
```

```python
# views.py

from django.shortcuts import render, redirect
from .forms import ArticleForm

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  # 모델에 데이터 저장
            return redirect('article_list')  # 글 목록 페이지로 리디렉션
    else:
        form = ArticleForm()

    return render(request, 'create_article.html', {'form': form})
```

[![](\assets\posts\{{ page.name }}\model.png)](\assets\posts\{{ page.name }}\model.png)

```html
{% raw %}
<!-- create_article.html -->

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
{% endraw %}
```

위 코드는 `title`과 `content` 필드를 가진 폼이 자동으로 생성되며, 이를 템플릿에 렌더링할 수 있습니다.
`ModelForm`을 사용하여 폼 제출 시 모델에 데이터를 자동으로 저장할 수 있어 매우 편리합니다.

---

## References
- [Django 공식 문서](https://www.djangoproject.com/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
