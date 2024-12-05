---
title: Django Serializer를 사용한 API 처리
category: Study
tag: [Education, Rest Framework, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## `Serializer` 기본 개념
> `Serializer`는 데이터를 **직렬화(Serialization)**하고 **역직렬화(Deserialization)**하는 데 사용됩니다.
`Serializer`를 사용하면 모델 데이터를 HTTP 응답으로 보내거나, 클라이언트에서 받은 데이터를 Django 모델에 저장할 수 있습니다.

* 직렬화: 파이썬 객체(예: 모델 인스턴스, 쿼리셋 등)를 JSON이나 XML 형식으로 변환
* 역직렬화: JSON이나 XML 데이터를 파이썬 객체로 변환

```python
# serializers.py

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField()

    def create(self, validated_data):
        return MyModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
```

### 1. 직렬화
```python
from rest_framework.renderers import JSONRenderer
from .models import MyModel
from .serializers import MyModelSerializer

# 모델 인스턴스 직렬화
my_model_instance = MyModel.objects.get(id=1)
serializer = MyModelSerializer(my_model_instance)
json_data = JSONRenderer().render(serializer.data)

# JSON 응답
print(json_data)

# {
#     "name": "Example Name",
#     "description": "Example Description",
#     "created_at": "2024-12-01T00:00:00Z"
# }
```

### 2. 역직렬화
```python
from rest_framework.parsers import JSONParser
from io import BytesIO
from .models import MyModel
from .serializers import MyModelSerializer

# JSON 데이터
json_data = '{"name": "Example Name", "description": "Example Description", "created_at": "2024-12-01T00:00:00Z"}'

# JSON 데이터를 파이썬 객체로 변환 (역직렬화)
stream = BytesIO(json_data.encode('utf-8'))
data = JSONParser().parse(stream)

# 역직렬화된 데이터를 사용하여 모델 인스턴스 생성
serializer = MyModelSerializer(data=data)

# 유효성 검사 후 객체 저장
if serializer.is_valid():
    my_model_instance = serializer.save()  # 모델 인스턴스를 생성하거나 업데이트
else:
    print("Invalid data:", serializer.errors)
```

## `ModelSerializer` 클래스란?
> `ModelSerializer`는 Django 모델을 기반으로 직렬화를 자동으로 처리해주는 Serializer의 서브클래스입니다.
모델의 필드를 자동으로 추출하여 직렬화하고, create()와 update() 메서드를 자동으로 처리합니다.

### 1. Meta 클래스
> Meta 클래스 내부의 model 속성에 Django 모델을 지정하고, fields 속성에 직렬화할 필드를 지정합니다.
fields 속성은 모델의 필드명을 나열하거나, __all__을 사용하여 모든 필드를 직렬화할 수 있습니다.

```python
# serializers.py

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['name', 'description', 'created_at'] # 직렬화할 모델의 필드를 지정
```

#### exclude
```python
# serializers.py

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        exclude = ['id', 'created_at'] # 직렬화할 모델의 필드 중 제외할 필드를 지정
```

#### read_only_fields
```python
# serializers.py

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['name', 'description', 'created_at']
        read_only_fields = ['created_at']  # 해당 필드를 읽기 전용으로 지정
```

#### write_only_fields
```python
# serializers.py

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['password']
        write_only_fields = ['password'] # 해당 필드를 쓰기 전용으로 지정
```

#### extra_kwargs
```python
# serializers.py

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['name', 'description']
        extra_kwargs = {
            'name': {'validators': [custom_name_validator]},
            'description': {'max_length': 500}
        } # 필드에 추가적인 속성을 지정
```

### 2. 유효성 검사
> ModelSerializer에서 특정 필드나 객체에 대해 유효성 검사를 추가할 수 있습니다. 
`validate_<field_name>` 메서드를 오버라이드하여 필드 단위로 유효성 검사를 할 수 있습니다.

```python
# serializers.py

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['name', 'description', 'created_at']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value
```

#### 객체 전체에 대한 유효성 검사
> 객체 전체에 대한 유효성 검사는 validate() 메서드를 오버라이드하여 수행할 수 있습니다. 
이 메서드는 직렬화된 객체 전체에 대한 검사에 사용됩니다.

```python
# serializers.py

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['name', 'description', 'created_at']

    def validate(self, attrs):
        if attrs['name'] == 'admin':
            raise serializers.ValidationError("The name 'admin' is not allowed.")
        return attrs
```

### 3. Serializer Method Field
> 필드에 대해 특별한 계산을 수행하거나 외부 데이터를 가져와서 표시하려면 **SerializerMethodField**를 사용할 수 있습니다.
`get_<field_name>` 메서드에서 특별한 필드 값을 생성할 수 있습니다.

```python
# serializers.py

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    custom_field = serializers.SerializerMethodField()

    class Meta:
        model = MyModel
        fields = ['name', 'description', 'custom_field']

    def get_custom_field(self, obj):
        return f"Custom: {obj.name}"
```

## `APIView` 클래스와 `Serializer` 결합
> Django REST Framework에서는 `APIView` 클래스를 사용하여 RESTful API를 구축할 수 있습니다.

```python
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelView(APIView):
    def get(self, request, *args, **kwargs):
        my_model_instance = MyModel.objects.get(id=1)
        serializer = MyModelSerializer(my_model_instance)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid(): # 데이터 유효성 검증
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

```python
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelView(APIView):
    def get(self, request, *args, **kwargs):
        # 여러 모델 인스턴스를 직렬화할 때
        queryset = MyModel.objects.all()
        serializer = MyModelSerializer(queryset, many=True) # many=True 지정
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid(): # 데이터 유효성 검증
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)
* [Django REST Framework 공식 문서](https://www.django-rest-framework.org/)

{% endraw %}