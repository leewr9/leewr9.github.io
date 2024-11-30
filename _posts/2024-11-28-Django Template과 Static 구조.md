---
title: Django Template과 Static 구조
category: Study
tag: [Education, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## Templates(템플릿) 경로 설정
> Django는 기본적으로 `settings.py > TEMPLATES` 설정에서 템플릿 파일을 찾습니다. 일반적으로 프로젝트의 루트 디렉터리 하위에 templates 디렉터리를 생성하고 사용합니다.

```arduino
myproject/
│
├── myproject/
│   ├── settings.py
│   └── ...
├── myapp/
│   ├── templates/
│   │   └── myapp/
│   │       └── home.html
│   └── ...
└── templates/
    └── base.html
```

```python
# settings.py

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 프로젝트 루트 템플릿 경로
        'APP_DIRS': True,  # 앱 내의 templates 디렉터리도 자동 탐색
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

## CSS 및 JS 정적 파일 경로 설정
> Django에서는 정적 파일(CSS, JS, 이미지 등)을 static 디렉터리에 배치하며, STATICFILES_DIRS와 STATIC_URL을 설정합니다.

```arduino
myproject/
│
├── myproject/
│   ├── settings.py
│   └── ...
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
└── myapp/
    └── static/
        └── myapp/
            └── css/
                └── app_style.css
```

```python
#settings.py 

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'  # 정적 파일의 URL 경로

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # 프로젝트 루트 static 디렉터리
]
```

## 템플릿에서 CSS/JS 파일 불러오기
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Django App</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <h1>Welcome to My Django App</h1>
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

## 정리

| 항목 | 디렉터리 위치 예시 | settings.py 설정 예시 |
| - | - | - |
| Templates | myproject/templates/ | 'DIRS': [os.path.join(BASE_DIR, 'templates')] |
| Static Files (CSS, JS) | myproject/static/ | TATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] |
| App Static | myapp/static/myapp/ | APP_DIRS: True (자동으로 탐색) |

* **Templates**: 프로젝트 루트의 templates/ 또는 각 앱의 templates/를 사용.
* **Static**: 프로젝트 루트의 static/ 또는 각 앱의 static/을 사용. STATICFILES_DIRS에 추가 가능.

## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)

{% endraw %}