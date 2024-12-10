---
title: QuerySet and Filtering
category: Django
tag: [Python, Django]
---

> QuerySet은 Django ORM에서 데이터베이스 쿼리의 결과 집합을 표현하는 객체입니다. QuerySet은 데이터를 읽고 필터링하거나 정렬하는 데 사용되며, 필요할 때만 실행되므로 성능 면에서도 효율적입니다.

```python
# 샘플 모델
from django.db import models

# 작성자 모델
class Author(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 태그 모델
class Tag(models.Model):
    name = models.CharField(max_length=100)

# 게시글 모델 (ForeignKey 관계)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

## Filtering
필터링은 조건에 맞는 여러 객체를 쿼리셋 형태로 반환하며, 조건에 맞는 객체가 없으면 빈 쿼리셋을 반환합니다. 여러 조건이 필요하다면 조건을 결합하여 쿼리할 수 있으며, 조건들은 모두 `AND` 연산으로 결합됩니다.

```python
from datetime import datetime, timedelta

# 모든 게시글 조회
posts = Post.objects.all()

# 특정 조건으로 데이터 필터링
filtered_posts = Post.objects.filter(title__icontains='Python')

# 제목이 'Python'을 포함하고, 생성 날짜가 7일 이내인 게시글
start_date = datetime.now() - timedelta(days=7)
filtered_posts = Post.objects.filter(title__icontains='Python', created_at__gte=start_date)
```

| 연산자 | 연산자 (대소문자 구분하지 않음) | 조건 |
| - | - | - |
| exact | iexact | 정확히 일치하는 값 |
| startswith | istartswith | 앞부분 일치 |
| endswith | iendswith | 뒷부분 일치   |
| contains | icontains | 부분 일치   |
| gt | igt | 값이 큰 |
| lt | ilt | 값이 작은 |
| gte | igte | 값이 크거나 같은 |
| lte | ilte | 값이 작거나 같은 |

### exclude
`exclude` 메서드는 `filter`와는 반대로 조건에 맞지 않는 데이터를 반환합니다.

```python
# 게시글 제목에 'Python'이 포함되지 않은 데이터 조회
filtered_posts = Post.objects.exclude(title__icontains='Python')
```

### order_by
`order_by` 메서드는 특정 필드를 기준으로 데이터를 정렬합니다.

- `-필드명`: 내림차순 정렬.
- `필드명`: 오름차순 정렬.

```python
# 게시글을 생성 날짜 기준으로 내림차순 정렬
posts = Post.objects.order_by('-created_at')

# 좋아요 수 기준으로 오름차순 정렬
posts = Post.objects.order_by('likes')

# 생성 날짜 기준으로 내림차순, 조회수 기준으로 오름차순 정렬
posts = Post.objects.order_by('-created_at', 'views')
```

### distinct
`distinct` 메서드는 쿼리셋에서 중복된 데이터를 제거합니다.

```python
# 작성자를 기준으로 중복 제거된 게시글 조회
authors = Post.objects.values('author').distinct()
```

### Case and When
`Case`와 `When` 객체를 사용하면 조건에 따라 다른 값을 처리할 수 있습니다.

```python
from django.db.models import Case, When, Value

# 조회수가 100 이상인 게시글은 '인기', 그렇지 않은 게시글은 '일반'으로 라벨링
posts = Post.objects.annotate(
    popularity=Case(
        When(views__gte=100, then=Value('Popular')),
        default=Value('Normal'),
        output_field=models.CharField()
    )
)

# 조회수가 100 이상인 게시글을 우선 정렬
posts = Post.objects.annotate(
    is_popular=Case(
        When(views__gte=100, then=Value(1)),
        default=Value(0),
        output_field=IntegerField()
    )
).order_by('-is_popular', '-views')
```

### Subquery 
서브쿼리를 작성할 때 사용됩니다. SQL의 서브쿼리와 유사한 쿼리를 작성할 수 있습니다.

```python
from django.db.models import Subquery, OuterRef

# 가장 최근 댓글의 내용을 게시글에 추가
recent_comments = Comment.objects.filter(post=OuterRef('pk')).order_by('-created_at').values('content')[:1]
posts = Post.objects.annotate(latest_comment=Subquery(recent_comments))
```

---

## Relationship-Based Filtering
외래키(ForeignKey)와 다대다 관계(ManyToMany) 필드 관계를 통해 연결된 모델을 기준으로 데이터를 필터링할 수 있습니다. 이를 통해 관계된 모델의 데이터를 기반으로 쿼리를 수행할 수 있습니다.

### ForeignKey
외래키 관계에서 관련된 모델의 필드를 통해 데이터를 필터링할 수 있습니다.
`__(더블 언더스코어)`를 사용하여 관련 모델의 필드에 접근합니다.

```python
from django.db.models import Count

# 특정 작성자가 작성한 게시글 조회
posts = Post.objects.filter(author__username='john_doe')

# 게시글의 카테고리가 'Python'인 게시글 조회
posts = Post.objects.filter(category__name='Python')

# 댓글 수가 3개 이상인 게시글 조회
posts = Post.objects.annotate(comment_count=Count('comments')).filter(comment_count__gte=3)
```

### ManyToMany
다대다 관계에서 특정 조건을 만족하는 데이터를 필터링합니다.
`__(더블 언더스코어)`를 사용하여 관련 모델의 필드에 접근합니다.

```python
# 특정 태그를 포함한 게시글 조회
posts = Post.objects.filter(tags__name='Django')
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
