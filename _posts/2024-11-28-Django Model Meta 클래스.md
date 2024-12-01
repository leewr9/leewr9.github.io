---
title: Django Model Meta 클래스
category: Study
tag: [Education, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## `Meta` 클래스란?
> Django 모델의 `Meta` 클래스는 모델의 구성 및 설정을 관리하는 데 사용됩니다. 
Meta 클래스는 모델에 대한 다양한 옵션을 설정할 수 있습니다.

### 1. db_table

```python
# models.py

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'my_custom_table_name' # 모델에 대한 데이터베이스 테이블의 이름을 지정
```
### 2. ordering

```python
# models.py

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # 모델 인스턴스를 조회할 때 기본 정렬 순서를 지정, 내림차순
```

### 3. verbose_name / verbose_name_plural

```python
# models.py

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta: # 관리 페이지에서 모델을 표시될 때 사용
        verbose_name = 'My Custom Model' # 모델의 단수 이름을 지정
        verbose_name_plural = 'My Custom Models' # 모델의 복수 이름을 지정
```

### 4. constraints

```python
# models.py

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_name') # 모델에 대한 제약 조건을 설정
        ]
```

### 5. indexes

설명: 할 수 있습니다. 이 옵션은 데이터베이스에서 조회 성능을 최적화하는 데 사용됩니다.
사용 예시:

```python
# models.py

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        indexes = [ # 데이터베이스에 성능 최적화
            models.Index(fields=['name']) # 모델에 대해 인덱스를 설정
        ]
```

### 6. managed

```python
# models.py

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False  # Django가 해당 모델의 테이블을 관리하지 않음
```

## 제약 조건 (Constraint)
> Meta 클래스 내부에 있는 constraints 속성을 통해 설정할 수 있습니다. 
Serializer에서 제약 조건을 지정하는 것과는 다르게, 모델에서 유효성 검사 및 제약을 설정하는 데 사용됩니다.

### 1. UniqueConstraint
> 두 개 이상의 필드가 고유값을 갖도록 설정하여 고유한 값인 만족하는 데이터만 저장할 수 있도록 제한하는 제약입니다.

```python
# models.py

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'description'], name='unique_name_description')
        ] # 같은 name과 description 값의 레코드가 존재할 수 없음
```

### 2. CheckConstraint
> 특정 조건을 만족하는 데이터만 저장할 수 있도록 제한하는 제약입니다. 

```python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name='age_greater_than_18')
        ] # age 필드의 값이 18 이상
```



## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)

{% endraw %}