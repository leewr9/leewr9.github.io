---
title: Django PrimaryKey와 ForeignKey
category: Study
tag: [Education, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

## PrimaryKey 필드
> PrimaryKey는 데이터베이스 테이블에서 각 행을 고유하게 식별하는 필드입니다. Django 모델에서 기본적으로 각 모델은 id라는 필드를 Primary Key로 사용합니다. 그러나 필요에 따라 primary_key=True 옵션을 사용하여 다른 필드를 Primary Key로 설정할 수 있습니다.

### 1. 기본 Primary Key
* Django는 각 모델에 대해 자동으로 id라는 Primary Key를 생성합니다. 이 필드는 기본적으로 자동 증가하는 정수형 값입니다.

```python
# models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

### 2. 사용자 정의 Primary Key
* `primary_key=True`를 사용하여 다른 필드를 Primary Key로 지정할 수 있습니다.

```python
# models.py

from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()
```

## ForeignKey 필드
> ForeignKey는 한 모델이 다른 모델과 관계를 맺을 때 사용됩니다. 외래 키는 관계형 데이터베이스에서 1:N (일 대 다) 관계를 정의하는 데 사용됩니다. 즉, 한 객체가 다른 객체와 연결될 때 사용됩니다.

### 1. ForeignKey 사용
```python
# models.py

from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()

class Order(models.Model):
    order_number = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ForeignKey 필드
```

* Order 모델은 customer 필드에 ForeignKey를 사용하여 Customer 모델과 관계를 설정합니다.
* `on_delete=models.CASCADE`는 만약 관련된 Customer 객체가 삭제되면 해당 Order 객체도 삭제된다는 뜻입니다.

#### on_delete
```python
class Order(models.Model):
    order_number = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, 
      on_delete=models.SET_NULL, null=True)  # 삭제 시 NULL로 설정
```

* on_delete 옵션
  * CASCADE: 참조된 객체가 삭제되면 해당 객체를 참조하는 모든 객체도 삭제됨.
  * SET_NULL: 참조된 객체가 삭제되면 해당 필드가 NULL로 설정됨 (이 경우 null=True를 필드에 추가해야 함).
  * PROTECT: 참조된 객체가 삭제되지 않도록 보호함.
  * SET_DEFAULT: 참조된 객체가 삭제되면 기본값으로 설정됨.
  * DO_NOTHING: 아무 작업도 하지 않음.

### 3. ForeignKey 역참조

```python
# Customer 객체에서 관련된 모든 주문을 가져오기
customer = Customer.objects.get(username='john_doe')
orders = customer.order_set.all()  # 기본적으로 역참조는 '모델명_set' 형식으로 생성됨
```

#### related_name
* `related_name`을 사용하여 역참조 이름을 변경할 수 있습니다.

```python
class Order(models.Model):
    order_number = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, 
      on_delete=models.CASCADE, related_name='orders')  # 역참조 이름 설정
```

```python
customer = Customer.objects.get(username='john_doe')
orders = customer.orders.all()  # 'orders'로 역참조
```

## 정리

| 필드 타입	| 설명 | 예시 |
| - | - | - |
| PrimaryKey | 각 객체를 고유하게 식별하는 필드로 자동 생성됨 (기본 id) | id = models.AutoField(primary_key=True) |
| ForeignKey | 다른 모델과의 1:N 관계를 설정하는 필드 | customer = models.ForeignKey(Customer, on_delete=models.CASCADE) |


## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)