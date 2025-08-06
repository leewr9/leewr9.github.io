---
title: REST Framework
category: Django
tag: [REST Framework, Python, Django]
---

> Django REST Framework (DRF)는 Django로 RESTful API를 구축할 수 있도록 돕는 라이브러리입니다. DRF는 웹 API를 설계하고 구현하는 데 필요한 다양한 기능을 제공합니다. 이를 사용하면 Django 프로젝트에서 손쉽게 API를 구축할 수 있습니다.

---

## Serializer

`Serializer`는 DRF에서 중요한 역할을 합니다. 데이터 모델을 JSON 형식으로 변환하거나, JSON 데이터를 모델의 필드에 맞는 Python 객체로 변환하는 작업을 합니다. Django에서는 `models.py`에서 정의된 모델을 기반으로 데이터를 JSON 형식으로 출력하거나, 그 반대로 변환할 때 `Serializer`를 사용합니다.

```bash
pip install djangorestframework
```

```python
# settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### Usage

```python
# serializers.py

from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    published_date = serializers.DateField()
```

```python
# shell

from myapp.serializers import BookSerializer

book_data = {'title': 'Django for Beginners', 'author': 'John Doe', 'published_date': '2024-01-01'}

# Serializer 인스턴스 생성
serializer = BookSerializer(data=book_data)

# 유효성 검사 후 직렬화
if serializer.is_valid():
    print(serializer.data) # {'title': 'Django for Beginners', 'author': 'John Doe', 'published_date': '2024-01-01'}
else:
    print(serializer.errors)
```

위 예시에서 `BookSerializer`는 `title`, `author`, `published_date` 데이터를 직렬화하는 기능을 합니다. 이와 같이 기본 Serializer는 Python 객체와 JSON 간의 상호 변환을 처리합니다.

---

## ModelSerializer

`ModelSerializer`는 Django 모델을 기반으로 직렬화를 수행하는 데 사용됩니다. `ModelSerializer`는 Django 모델의 필드와 자동으로 매핑되며, 이를 통해 보다 빠르게 데이터를 직렬화할 수 있습니다.

```python
# serializers.py

from rest_framework import serializers
from .models import Book

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']
```

```python
# shell

from myapp.models import Book
from myapp.serializers import BookSerializer

book_instance = Book.objects.get(id=1)

# Serializer 인스턴스 생성
serializer = BookModelSerializer(book_instance)

# 직렬화된 데이터
print(serializer.data)
```

위 코드에서는 `BookModelSerializer`를 사용하여 `Book` 모델을 직렬화합니다. `ModelSerializer`는 모델의 필드 정의를 기반으로 직렬화를 자동으로 처리하기 때문에 `fields` 속성에 모델의 필드 목록만 지정하면 됩니다.

### Meta Class

Meta 클래스는 `ModelSerializer`에서 사용하는 중요한 설정을 정의합니다. Meta 클래스 안에서 `model`과 `fields`를 정의하여, 직렬화할 모델과 필드를 지정합니다.

- `model`: 직렬화할 모델을 지정합니다.
- `fields`: 직렬화할 필드 목록을 지정합니다. 기본적으로 모델의 모든 필드가 직렬화됩니다.
- `exclude`: 직렬화에서 제외할 필드를 지정할 수 있습니다. fields와 exclude는 함께 사용되지 않습니다.
- `read_only_fields`: 읽기 전용 필드를 지정합니다. 이 필드는 직렬화할 수 있지만, 역직렬화에서 제외됩니다.

```python
class Meta:
    model = Book
    fields = ['id', 'title', 'author', 'published_date'] # 직렬화할 필드만 지정
    read_only_fields = ['id'] # 'id' 필드는 읽기 전용
   # exclude = ['price'] # 가격 필드는 직렬화에서 제외할 수도 있습니다
```

Meta 클래스에서 `fields`와 `exclude`를 함께 사용할 수는 없지만, 각기 다른 방식으로 직렬화할 필드를 조정할 수 있습니다. `read_only_fields`를 사용하면 읽기 전용 필드를 지정할 수 있으며, 이를 통해 직렬화된 데이터의 불변 속성을 관리할 수 있습니다.

### validate

`ModelSerializer`에서 객체와 필드에 대한 유효성 검사를 `validate`나 `validate_<field_name>` 메서드를 사용하여 추가할 수 있습니다. 이는 여러 필드 간의 관계를 검사하거나, 필드들이 특정 조건을 만족하는지 확인할 때 유용합니다.

```python
def validate(self, data):
   # 예: 제목과 저자 모두 'Django'가 포함되어야 한다고 가정
    if 'Django' not in data.get('title') or 'Django' not in data.get('author'):
        raise serializers.ValidationError("Both title and author must contain 'Django'.")
    return data

# title 필드에 대한 유효성 검사
def validate_title(self, value):
    if "Django" not in value:
        raise serializers.ValidationError("Title must contain 'Django'.")
    return value
```

```python
# 유효성 검사에 실패할 데이터
book_data = {'title': 'Python for Beginners', 'author': 'John Doe', 'published_date': '2024-01-01'}
serializer = BookModelSerializer(data=book_data)

if not serializer.is_valid():
    print(serializer.errors)
   # {'title': ['Title must contain "Django".']}
```

---

## References

- [Django 공식 문서](https://www.djangoproject.com/)
- [REST Framework 공식 문서](https://www.django-rest-framework.org/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
