---
title: Model Relationship
category: Django
tag: [ManyToManyField, OneToOneField, ForeignKey, Python, Django]
---

> Django에서 모델 간의 관계를 정의하는 것은 데이터베이스 설계의 핵심입니다. Django에서는 다양한 필드를 제공하여 모델 간의 관계를 쉽게 설정할 수 있도록 합니다. 이러한 관계를 이해하고 적절히 활용하는 것은 효율적인 데이터 관리를 위해 매우 중요합니다.

---

## ForeignKey

`ForeignKey`는 가장 일반적으로 사용되는 관계로, 한 모델의 인스턴스가 다른 모델의 여러 인스턴스와 연결될 수 있습니다. 즉, **일대다(1:N)** 관계를 표현할 때 사용합니다.

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    publication_date = models.DateField()

books_by_author = author.book_set.all()  # 역참조
```

### on_delete

`on_delete`는 참조된 객체가 삭제될 경우, 연결된 객체를 어떻게 처리할지 정의합니다. 이는 데이터 무결성을 유지하기 위한 중요한 설정입니다.

- `CASCADE`: 참조된 객체가 삭제되면 이를 참조하는 객체도 삭제
- `PROTECT`: 참조된 객체가 삭제되지 않도록 보호
- `SET_NULL`: 참조된 객체가 삭제되면 NULL로 설정 (`null=True` 필요)
- `SET_DEFAULT`: 참조된 객체가 삭제되면 기본값으로 설정
- `SET()`: 참조된 객체가 삭제되면 지정한 값으로 설정
- `DO_NOTHING`: 아무것도 하지 않음 (데이터베이스 레벨에서 처리)

### related_name

`related_name`은 역참조에 사용되는 속성 이름을 지정합니다. `ForeignKey` 관계에서는 기본적으로 `modelname_set` 형태로 역참조하지만, related_name을 사용하면 더 의미 있는 이름으로 접근할 수 있습니다.

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    publication_date = models.DateField()

author = Author.objects.get(name='Some Author')
books_by_author = author.books.all()  # related_name 사용
```

### related_query_name

`related_query_name`은 쿼리셋 필터링 시 역참조 이름을 어떻게 사용할지 정의합니다. `related_name`이 객체 접근에서 쓰인다면, `related_query_name`은 쿼리 메서드 (`filter`, `exclude` 등)에서 사용됩니다. 복잡한 조인 조건을 사용하는 쿼리에서 직관적인 쿼리 표현이 가능해집니다.

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_query_name='book'
    )
    publication_date = models.DateField()

authors_with_books = Author.objects.filter(book__title__icontains='Django') # related_query_name 사용
```

### limit_choices_to

`limit_choices_to`는 ForeignKey 필드에서 선택할 수 있는 객체를 제한하는 데 사용됩니다. 특정 조건을 지정하여 관리 인터페이스나 폼에서 선택 가능한 옵션을 필터링할 수 있습니다.

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        limit_choices_to={'email__endswith': '@example.com'}  # 특정 도메인 이메일 가진 저자만 선택 가능
    )
```

---

## OneToOneField

`OneToOneField`는 두 모델 간에 고유한 **일대일(1:1)** 관계를 만듭니다. 데이터베이스 관점에서는 `Unique` 제약 조건이 자동으로 생성되며, 한 쪽 객체가 반드시 다른 한 객체와만 연결됨을 보장합니다.

```python
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

user = User.objects.get(username='john')
profile = user.userprofile  # 역참조
```

---

## ManyToManyField

`ManyToManyField`는 두 모델 간에 **다대다(N:N)** 관계를 표현합니다. 자동으로 중간 테이블을 생성하여 관계를 저장하며, `add`, `remove`, `set` 메서드를 통해 관계를 동적으로 조절할 수 있습니다.

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.ManyToManyField(Category, blank=True)

tech = Category.objects.create(name='Technology')
science = Category.objects.create(name='Science')

article = Article.objects.create(
    title='AI Revolution',
    content='Content about AI...'
)

# 관계 추가
article.categories.add(tech)
article.categories.add(science)

# 여러 개 한번에 추가
article.categories.set([tech, science])

# 관계 제거
article.categories.remove(tech)

# 모든 관계 제거
article.categories.clear()

# 관계 조회
categories = article.categories.all()
articles_in_tech = tech.article_set.all()
```

### through

`through`는 `ManyToManyField`가 자동으로 생성하는 중간 테이블을 직접 정의하고 싶을 때 사용합니다. 단순한 관계가 아니라 관계 자체에 의미 있는 데이터가 존재할 때 사용되는 방식입니다.

```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.ManyToManyField(
        Category,
        through='ArticleCategory',
        blank=True,
    )

# 중간 테이블 모델 정의
class ArticleCategory(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True) # 관계 생성 시간 기록

    class Meta:
        unique_together = ('article', 'category')

# 관계 추가
ArticleCategory.objects.create(
    article=article,
    category=tech
)

ArticleCategory.objects.create(
    article=article,
    category=science
)

# 관계 조회
categories = article.categories.all()
articles_in_tech = tech.article_set.all()
```

---

## Optimization

### select_related()

`select_related`는 `ForeignKey`와 `OneToOneField` 관계에 대해 `SQL JOIN`을 사용하여
관련된 객체를 한 번의 쿼리로 미리 가져옵니다. 이는 데이터베이스 쿼리 횟수를 줄여 `N+1` 문제를 해결하는 핵심 최적화 기법입니다. 주로 `1:1` 또는 `N:1` 관계에서 사용됩니다.

```python
books = Book.objects.select_related('author').all()
for book in books:
    print(f"{book.title} by {book.author.name}")  # 추가 쿼리 없음
```

### prefetch_related()

`prefetch_related`는 `ManyToManyField` 및 역참조에 대해 별도의 쿼리를 사용하여 관련 객체를 미리 불러오는 방식입니다. 관련 데이터를 Python 레벨에서 매칭하기 때문에, 복잡한 `N:N` 관계나 리스트 형태의 관계에서 효과적으로 성능을 최적화합니다. 주로 `1:N`, `N:N` 관계에서 사용됩니다.

```python
articles = Article.objects.prefetch_related('categories').all()
for article in articles:
    categories = article.categories.all()  # 추가 쿼리 없음
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
