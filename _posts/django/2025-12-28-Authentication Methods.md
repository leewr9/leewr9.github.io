---
title: Authentication Methods
category: Django
tag: [Authentication, REST Framework, Python, Django]
---

> Django REST Framework (DRF)에서 인증은 “누가 요청했는가?”를 확인하는 과정이고, 인가는 “이 사용자가 이 작업을 할 수 있는가?”를 결정하는 과정입니다. 다양한 인증 방식을 이해하고, 서비스 요구사항에 맞는 적절한 방법을 선택하는 것이 중요합니다.

---

## Authentication

`Authentication`는 사용자의 신원을 확인하는 과정입니다. DRF에서는 여러 가지 인증 방식을 지원하며, 각 방식은 서로 다른 시나리오에 적합합니다.

- **settings.py**
  ```python
  REST_FRAMEWORK = {
      "DEFAULT_AUTHENTICATION_CLASSES": (
          "rest_framework.authentication.SessionAuthentication",
          "rest_framework.authentication.BasicAuthentication",
      ),
      "DEFAULT_PERMISSION_CLASSES": (
          "rest_framework.permissions.IsAuthenticated",
      ),
  }
  ```
- **views.py**

  ```python
  from rest_framework.views import APIView
  from rest_framework.response import Response
  from rest_framework.permissions import IsAuthenticated
  from rest_framework.authentication import SessionAuthentication

  class MeView(APIView):
      authentication_classes = [SessionAuthentication]
      permission_classes = [IsAuthenticated]

      def get(self, request):
          return Response({"username": request.user.username})
  ```

### SessionAuthentication

`SessionAuthentication`는 Django의 기본 세션 프레임워크를 사용하여 인증을 처리합니다. 주로 브라우저 기반 애플리케이션에서 사용되며, 로그인 후 세션 쿠키를 통해 사용자를 식별합니다.

```python
# settings.py
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
}
```

```bash
curl -H "Cookie: sessionid=YOUR_SESSION_ID" \
     -H "X-CSRFToken: YOUR_CSRF_TOKEN" \
     http://localhost:8000/api/me/
```

### BasicAuthentication

`BasicAuthentication`는 `HTTP` 기본 인증 방식을 사용하여 사용자 이름과 비밀번호를 `Base64`로 인코딩하여 전달합니다. 간단하지만 보안에 취약할 수 있으므로 `HTTPS`와 함께 사용하는 것이 권장됩니다.

```python
# settings.py
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
    ),
}
```

```bash
curl -u username:password http://localhost:8000/api/me/
```

### TokenAuthentication

`TokenAuthentication`는 고유한 토큰을 사용하여 인증을 처리합니다. 주로 모바일 앱이나 외부 클라이언트에서 사용되며, 토큰을 `Authorization` 헤더에 포함하여 요청합니다.

```python
# settings.py
INSTALLED_APPS = [
    "rest_framework.authtoken",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
}
```

```bash
curl -H "Authorization: Token YOUR_TOKEN" \
     http://localhost:8000/api/me/
```

#### obtain_auth_token

`obtain_auth_token` 뷰를 사용하여 토큰을 발급받을 수 있습니다. 유저 이름과 비밀번호를 POST 요청으로 보내면 토큰이 반환됩니다.

```python
# urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("api/auth/token/", obtain_auth_token),
]
```

```bash
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"username","password":"password"}'

# {"token":"abc123..."}
```

### JWT

**JWT(JSON Web Token)**는 자체 포함된 토큰을 사용하여 인증을 처리합니다. 토큰에는 사용자 정보와 만료 시간 등의 클레임이 포함되어 있어, 서버에서 상태를 유지하지 않고도 인증을 수행할 수 있습니다. 주로 `SPA`나 모바일 앱에서 사용됩니다.

```bash
pip install djangorestframework-simplejwt
```

```python
# settings.py
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
```

```bash
curl -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     http://localhost:8000/api/me/
```

#### TokenObtainPairView

`TokenObtainPairView`는 JWT 토큰을 발급하는 뷰입니다. 사용자 이름과 비밀번호를 POST 요청으로 보내면 액세스 토큰과 리프레시 토큰이 반환됩니다.

```python
# urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("api/auth/jwt/", TokenObtainPairView.as_view()),
]
```

```bash
curl -X POST http://localhost:8000/api/auth/jwt/ \
  -H "Content-Type: application/json" \
  -d '{"username":"username","password":"password"}'

# {"access":"...","refresh":"..."}
```

#### TokenRefreshView

`TokenRefreshView`는 리프레시 토큰을 사용하여 새로운 액세스 토큰을 발급하는 뷰입니다. 리프레시 토큰을 POST 요청으로 보내면 새로운 액세스 토큰이 반환됩니다.

```python
# urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("api/auth/jwt/refresh/", TokenRefreshView.as_view()),
]
```

```bash
curl -X POST http://localhost:8000/api/auth/jwt/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh":"REFRESH_TOKEN"}'
# {"access":"..."}
```

---

## References

- [Django 공식 문서](https://www.djangoproject.com/)
- [REST Framework 공식 문서](https://www.django-rest-framework.org/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
