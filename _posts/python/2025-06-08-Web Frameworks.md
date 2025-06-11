---
title: Web Frameworks
category: Python
tag: [FastAPI, Flask, Django, Python]
---

> Python을 사용하여 웹 서비스를 개발할 때, 어떤 웹 프레임워크를 선택하느냐는 전체 프로젝트의 방향성과 유지보수 전략에 결정적인 영향을 미칩니다. 다양한 프레임워크들이 여러 기능과 특성을 제공하며, 이에 대한 상세한 비교와 선택 기준을 제공합니다.

---

## Interface
Python은 다양한 웹 서버 인터페이스를 지원하여, 동기와 비동기 방식 모두에 대응할 수 있습니다.  

| 항목 | WSGI | ASGI |
|-|-|-|-|
| 약자 | Web Server Gateway Interface | Asynchronous Server Gateway Interface |
| 동작 방식 | 동기 방식 (Synchronous) | 비동기 및 동기 방식 모두 지원 |
| 지원 프로토콜 | HTTP 1.1 | HTTP/1.1, HTTP/2, WebSocket 등 |
| 비동기 처리 | 불가능 | 기본 지원 |
| 사용 예 | Django, Flask (기본 설정)| FastAPI, Django (ASGI 설정 시) |
| 서버 예시 | Gunicorn, uWSGI | Uvicorn, Daphne |
| 장점 | 안정적이고 호환성 높음 | 고성능, 실시간 양방향 통신 가능 |
| 단점 | 비동기 처리 불가능 | 상대적으로 새로워 지원 환경 제한 가능 |

### WSGI
`WSGI`는 Python 웹 애플리케이션과 웹서버 간에 데이터를 주고받기 위한 표준 인터페이스로, 동기 방식만 지원합니다. 대부분의 전통적인 Python 웹 프레임워크가 기본적으로 WSGI를 사용하며, `Gunicorn`, `uWSGI` 같은 서버에서 실행됩니다. 비동기 처리를 지원하지 않아 실시간 웹, WebSocket 등의 기능 구현에 제약이 있습니다.

### ASGI
`ASGI`는 `WSGI`의 한계를 극복하고자 등장한 비동기 및 동기 모두 지원하는 인터페이스입니다. HTTP/2와 WebSocket 같은 최신 프로토콜도 지원하며, 비동기 처리를 기본으로 하여 고성능 API 서버 개발에 적합합니다. FastAPI가 기본적으로 ASGI를 사용하고 있으며, 서버로는 `Uvicorn`, `Daphne` 등이 사용됩니다.

## Framework

### Django  
[![](/assets/posts/2025-06-08-Web Frameworks.md/django.png)](/assets/posts/2025-06-08-Web Frameworks.md/django.png)

`Django`는 Python 기반의 대표적인 풀스택 웹 프레임워크로, 배터리 포함 철학을 바탕으로 다양한 기능을 기본 제공하는 것이 특징입니다. ORM, 관리자 페이지, 인증, 마이그레이션 시스템 등 웹 개발에 필요한 모든 요소가 내장되어 있어 복잡한 백엔드 시스템을 빠르게 구축할 수 있습니다. Django는 명확한 구조와 강력한 커뮤니티를 갖추고 있어, 유지보수성과 확장성이 높은 웹 프로젝트에 적합합니다.

- 장점
    - 거의 모든 기능을 기본 제공 (ORM, Admin, 인증 등)
    - 빠른 MVP 개발 가능
    - 자동 관리자 페이지 생성
    - 보안 기능 기본 제공 (CSRF, XSS 방지 등)
    - 커뮤니티와 레퍼런스가 풍부

- 단점
    - 프로젝트 구조가 무겁고 진입장벽이 다소 있음
    - API 개발에 적합하지 않음 (DRF로 보완 필요)
    - 비동기 처리에 제약 있음

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")
```

### Flask  
[![](/assets/posts/2025-06-08-Web Frameworks.md/flask.png)](/assets/posts/2025-06-08-Web Frameworks.md/flask.png)

`Flask`는 최소한의 기능만 제공하는 마이크로 웹 프레임워크로, 자유도와 유연성이 가장 큰 강점입니다. 기본적으로 라우팅과 템플릿 렌더링만 제공하며, ORM, 인증, 폼 처리 등은 확장 패키지를 통해 구성합니다. 코드 구조나 사용 방식에 제약이 적어 작은 프로젝트나 실험적인 개발에 유리하며, 경량 API 서버에도 자주 활용됩니다.

- 장점
    - 단순하고 가벼운 구조로 빠른 개발 가능
    - 높은 유연성과 자유도
    - 필요한 기능만 선택해서 구성 가능
    - 빠른 테스트 및 프로토타이핑에 적합

- 단점
    - 규모가 커질수록 구조 정리가 어려움
    - 기본 기능이 적어 초보자에겐 부담
    - 비동기 처리가 기본 지원되지 않음

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

### FastAPI  
[![](/assets/posts/2025-06-08-Web Frameworks.md/fastapi.png)](/assets/posts/2025-06-08-Web Frameworks.md/fastapi.png)

`FastAPI`는 최신 Python 기능인 타입 힌트와 비동기 처리 기반으로 설계된 고성능 API 전용 프레임워크입니다. 자동 `Swagger` 문서 생성, `Pydantic` 기반의 데이터 검증, 비동기 지원 등이 강력한 장점이며, 특히 AI, 데이터, 머신러닝 API와 같은 시스템에서 자주 사용됩니다.

- 장점
    - Python 타입 힌트 기반으로 API 자동 문서 생성 (Swagger, ReDoc)
    - 비동기 처리로 고성능 구현 가능
    - 데이터 검증과 직렬화 자동 처리
    - `REST API` 중심의 경량 서비스에 적합

- 단점
    - UI 제공은 어려워 웹페이지 구현은 부적합
    - ORM, 인증, 마이그레이션 등은 외부 라이브러리 필요
    - 타입 힌트와 비동기에 익숙하지 않으면 진입장벽 존재

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello, World!"}
```

| 항목 | Django | Flask | FastAPI |
|-|-|-|-|
| 프레임워크 유형 | 풀스택 | 마이크로 | API 특화 |
| 기본 기능 | ORM, Admin, Auth 등 내장 | 최소한의 기능 | 타입 기반 API + 비동기 처리 |
| 비동기 지원 | 제한적 (ASGI 설정 필요) | 미지원 (외부 필요) | 기본 지원 |
| API 문서 자동 생성 | 미지원 | 미지원 | Swagger / OpenAPI |
| 진입장벽 | 중간 | 낮음 | 낮음 ~ 중간 |
| 확장성 | 높음 | 중간 | 높음 |
| 적합한 용도 | 관리자 웹 서비스 | 소규모 앱, 프로토타입 | AI, 데이터 API 서버 |
| 주요 사용자 | Instagram 등 | Netflix 등 | Hugging Face 등 |

---

## References
- [Python 공식 문서](https://docs.python.org/3/)
- [Django 공식 문서](https://www.djangoproject.com/)
- [Flask 공식 문서](https://fastapi.tiangolo.com/)
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
