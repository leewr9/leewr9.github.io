---
title: Object-Relational Mapping
category: Django
tag: [Python, Django]
---

> Django ORM(Object-Relational Mapping)은 데이터베이스와 상호작용하기 위해 SQL을 작성하지 않고 Python 코드로 데이터베이스 작업을 처리할 수 있게 해주는 Django의 핵심 도구입니다. 데이터베이스 테이블은 Python 모델 클래스로 정의되며, 이를 통해 데이터를 저장, 읽기, 업데이트, 삭제(CRUD) 작업을 수행합니다.

---

## Model
모델은 Django에서 데이터베이스 테이블을 정의하는 방식입니다. Django의 `models.Model` 클래스를 상속받아 모델을 정의하며, 각 모델에 기본적으로 `id`라는 기본키 필드를 추가합니다.

```python
from django.db import models

class Post(models.Model):
    id = models.CharField(max_length=50, primary_key=True), # 기본키
    title = models.CharField(max_length=100) # 제목
    content = models.TextField()             # 내용
    created_at = models.DateTimeField(auto_now_add=True) # 생성 시간
    updated_at = models.DateTimeField(auto_now=True)     # 수정 시간

    def __str__(self):
        return self.title
```
- `CharField`: 짧은 문자열 데이터
- `TextField`: 긴 텍스트 데이터
- `IntegerField`: 정수 데이터
- `FloatField`: 소수점 데이터
- `BooleanField`: 참/거짓 데이터
- `DateTimeField`: 날짜 및 시간 데이터
- `ForeignKey`: 다른 모델과의 1:N 관계
- `ManyToManyField`: 다른 모델과의 N:N 관계

---

## Migrations

### makemigrations
모델을 정의하거나 수정한 후, 이를 데이터베이스 스키마로 변환하기 위해 마이그레이션 파일을 생성해야 합니다. 이 작업은 `makemigrations` 명령어로 실행됩니다.

```bash
python manage.py makemigrations

# Migrations for 'myapp':
#   myapp/migrations/0001_initial.py
#     - Create model Post
```
이 명령어는 모델 변경 사항을 탐지하고, 이를 적용할 SQL 명령어를 포함한 마이그레이션 파일을 생성합니다.

### migrate
마이그레이션 파일을 데이터베이스에 실제로 적용하려면 `migrate` 명령어를 사용합니다.

```bash
python manage.py migrate

# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions, myapp
# Running migrations:
#   Applying myapp.0001_initial... OK
```
migrate 명령어는 생성된 마이그레이션 파일을 실행하여 데이터베이스 스키마를 변경합니다.
이 과정에서 Django는 모델에 정의된 테이블과 필드가 데이터베이스에 적절히 반영되도록 합니다.

---

## Meta Class
Django 모델의 `Meta` 클래스는 모델의 메타데이터를 정의하는 데 사용됩니다.

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['title', 'author'] # 제목과 작가 조합이 고유하도록 지정
        ordering = ['-id'] # ID를 기준으로 내림차순 정렬
        verbose_name = "Book Entry" # 관리자 화면에서의 모델 이름
        verbose_name_plural = "Book Entries" # 복수형 이름
```
- `unique_together`: 여러 필드의 값이 고유하도록 설정
- `ordering`: 기본 정렬 순서를 설정
- `verbose_name`: 모델의 사용자 지정 이름 설정

### constraints 
`Meta` 클래스 내에서는 데이터베이스 수준에서 제약조건을 설정할 수 있습니다. 제약조건은 데이터 무결성을 보장하는 데 중요합니다.

#### UniqueConstraint
`UniqueConstraint`는 특정 필드나 필드 조합이 고유해야 한다는 제약을 추가합니다. `unique_together`와 비슷하지만, 더 많은 옵션을 제공하고, `constraints` 옵션을 통해 설정할 수 있습니다.

```python
from django.db.models import Q

class Meta:
    constraints = [
       # 발행된 상태인 책의 제목과 작가 조합이 고유해야 한다는 조건을 추가
        models.UniqueConstraint(
            fields=['title', 'author'], 
            name='unique_post_author', 
            condition=models.Q(is_published=True)
        )
    ]
```
위 예시에서 `UniqueConstraint`는 `is_published`가 `True`인 경우에만 `title`과 `author` 필드의 조합이 고유해야 한다는 제약을 설정합니다.

#### CheckConstraint
`CheckConstraint`는 특정 조건을 만족하는지 데이터가 검사되는 제약을 추가할 때 사용됩니다.

```python
from django.db.models import Q

class Meta:
    constraints = [
        # 가격이 0 이상이어야 한다는 조건을 추가
        models.CheckConstraint(check=models.Q(price__gte=0), name='price_gte_0'),
        # 재고가 0 이상이어야 한다는 조건을 추가
        models.CheckConstraint(check=models.Q(stock__gte=0), name='stock_gte_0')
    ]
```
위 예시에서 `CheckConstraint`는 `price`와 `stock ` 필드가 각각 0 이상이어야 한다는 조건을 설정합니다. 이 제약은 해당 필드 값이 조건을 만족하지 않으면 데이터베이스에 저장되지 않게 됩니다.

---

## User Customization
Django는 기본적으로 제공되는 `User` 모델이 있지만, 프로젝트에 따라 사용자 데이터를 확장하거나 구조를 변경해야 하는 경우가 많습니다.

### AbstractUser
기본 User 모델을 확장하는 방법은 `AbstractUser`를 상속받아 추가 필드를 정의하는 것입니다.

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True) # 사용자 소개
    profile_image = models.ImageField(upload_to='profiles/', blank=True) # 프로필 이미지

    def __str__(self):
        return self.username
```

### AbstractBaseUser
만약 기본 User 모델을 완전히 대체하고 싶다면, `AbstractBaseUser`를 상속받아 새롭게 정의합니다.

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
```

```python
# settings.py에서 새로운 User 모델을 설정
AUTH_USER_MODEL = 'myapp.CustomUser'
```

---

## References
- [Django 공식 문서](https://www.djangoproject.com/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
