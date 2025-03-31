---
title: Frontend Resources
category: Django
tag: [Python, Django]
---

> Django의 프론트엔드 리소스 관리는 웹 애플리케이션 개발에서 중요한 역할을 합니다. 프론트엔드 리소스는 HTML 템플릿을 통해 페이지 구조를 정의하고, CSS, JavaScript, 이미지 등 정적 파일을 관리하여 웹 애플리케이션의 시각적 및 기능적 요소를 제공합니다.

---

## Templates
Django의 템플릿 시스템은 HTML 파일을 관리하고 서버 데이터를 동적으로 렌더링할 수 있도록 합니다.

### Structure
Django 템플릿은 `settings.py`에서 템플릿 디렉토리를 지정하며, 다음 디렉터리 구조를 가지고 있습니다.

```python
# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # 템플릿 디렉토리 경로
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

```plaintext
project/
│
├── myproject/
│   ├── settings.py
│   └── ...
│
├── myapp/
│   ├── templates/
│   │   └── myapp/
│   │       └── index.html
│   └── ...
│
└── templates/
    ├── base.html
    ├── head.html
    ├── header.html
    └── footer.html
```

{% raw %}
### Inheritance
Django 템플릿 상속을 사용하면 반복되는 HTML 코드를 효율적으로 관리할 수 있습니다. 템플릿에서 `블록(Block)`은 상속받는 템플릿에서 특정 영역을 변경하거나 추가할 수 있도록 해줍니다. 블록은 `{% block 블록이름 %}`과 `{% endblock %}` 사이에 정의됩니다.
{% endraw %}

{% raw %}
```html
<!-- base.html -->

<!DOCTYPE html>
<html lang='ko'>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Site</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2024 My Site</p>
    </footer>
</body>
</html>
```
{% endraw %}

[![](\assets\posts\2025-02-02-Frontend Resources.md\index.png)](\assets\posts\2025-02-02-Frontend Resources.md\index.png)

{% raw %}
```html
<!-- index.html -->
 
{% extends 'base.html' %} <!-- base.html 상속 -->

{% block title %}Home - My Site{% endblock %}

{% block content %}
    <h2>Welcome to My Site</h2>
    <p>This is the home page.</p>
{% endblock %}
```
{% endraw %}

### Filters and Tags
Django 템플릿은 데이터 출력과 제어를 위해 필터와 태그를 제공합니다.

{% raw %}
```html
<p>{{ user.username|upper }}</p> <!-- 사용자 이름을 대문자로 표시 -->
<p>{{ post.created_at|date:'Y-m-d' }}</p> <!-- 날짜 형식 지정 -->

{% if user.is_authenticated %} <!-- 조건 태그 -->
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}

{% for post in posts %} <!-- 반복 태그 -->
    <h3>{{ post.title }}</h3>
    <p>{{ post.content }}</p>
{% endfor %}
```
{% endraw %}

---

## Static
Django에서 정적 파일은 CSS, JavaScript, 이미지와 같은 리소스를 관리합니다. 

### Structure
Django 정적 파일은 `settings.py`에서 정적 파일 디렉토리를 지정하며, 다음 디렉터리 구조를 가지고 있습니다.

```python
# settings.py

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles' # 배포 시 사용할 정적 파일 경로
```

```plaintext
project/
│
├── myproject/
│   ├── settings.py
│   └── ...
│
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/
       └── logo.png
```

### Using
{% raw %}
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <img src="{% static 'images/logo.png' %}" alt='Logo'>
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```
{% endraw %}

---

## References
- [Django 공식 문서](https://www.djangoproject.com/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
