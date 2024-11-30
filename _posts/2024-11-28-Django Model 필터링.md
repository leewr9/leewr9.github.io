---
title: Django Model 필터링
category: Study
tag: [Education, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

## `필터링`을 위한 메서드
> filter(), exclude()는 조건에 맞는 여러 객체를 쿼리셋 형태로 반환하며, 조건에 맞는 객체가 없으면 빈 쿼리셋을 반환합니다.
여러 조건이 필요하다면 조건을 결합하여 쿼리할 수 있습니다. 조건들은 모두 AND 연산으로 결합됩니다.

* 연산자 종류
  * exact: 정확히 일치하는 값
  * startswith: 앞부분 일치
  * endswith: 뒷부분 일치  
  * contains: 부분 일치  
  * gt: 값이 큰 (greater than)  
  * lt: 값이 작은 (less than)  
  * gte: 값이 크거나 같은 (greater than or equal to)  
  * lte: 값이 작거나 같은 (less than or equal to)  
* 연산자의 앞에 `i`가 붙을 경우에는 대소문자 구분없이 조회가 가능합니다.
  * iexact: 대소문자 구분없이 정확히 일치하는 값
  * istartswith: 대소문자 구분없이 앞부분 일치
  * ...
  
> 우선, Customer와 Order 모델을 정의합니다. Customer 모델은 고객 정보를 담고, Order 모델은 고객이 만든 주문 정보를 저장합니다. 
Order 모델은 ForeignKey를 통해 Customer 모델과 관계를 맺습니다.

```python
# models.py

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Customer와 1:N 관계
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()
    status = models.CharField(max_length=20, default='pending')  # 주문 상태 (예: 'pending', 'completed')

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
```

## Model 필터링 

### 1. filter()
* filter()는 조건에 맞는 결과를 반환합니다.

```python
from myapp.models import Customer

# name에 'John'이 포함된 모든 Customer 객체 조회
customers = Customer.objects.filter(name__contains='John')

# age가 10 이상이고, price가 30 이하인 Customer 객체 조회
customers = Customer.objects.filter(age__gte=10, age__lte=30)

for customer in customers:
    print(customer.name, customer.age)
```

### 2. exclude()
* exclude() 메서드는 조건에 맞지 않는 객체를 제외하고 결과를 반환합니다.

```python
from myapp.models import Customer

# name에 'John'이 포함되지 않은 모든 Customer 객체 조회
customers = Customer.objects.exclude(name__contains='John')

for customer in customers:
    print(customer.name, customer.age)
```

## Model 관계 기반 필터링
> Django에서는 ForeignKey 관계를 통해 연결된 모델을 기준으로 데이터를 필터링할 수 있습니다. 
이때 __(더블 언더스코어)를 사용하여 관련 모델의 필드에 접근합니다.

### 1. filter()
* filter()는 조건에 맞는 결과를 반환합니다.

```python
from myapp.models import Order

# 특정 고객 (예: id가 1인 고객)의 모든 주문 조회
orders = Order.objects.filter(customer__id=1)

# 고객의 주문 중 상태가 'completed'인 주문만 조회
orders = Order.objects.filter(customer__id=1, status='completed')

# 특정 고객의 주문 중, total_amount가 100 이상인 주문 조회
orders = Order.objects.filter(customer__name='John Doe', total_amount__gte=100)

for order in orders:
    print(order.id, order.order_date, order.total_amount, order.status)
```

### 2. exclude()
* exclude() 메서드는 조건에 맞지 않는 객체를 제외하고 결과를 반환합니다.

```python
# 고객이 'John Doe'인 주문 중, 상태가 'completed'가 아닌 주문만 조회
orders = Order.objects.exclude(customer__name='John Doe', status='completed')

# 특정 고객의 'completed' 상태가 아닌 주문 중, total_amount가 50 이상인 주문 조회
orders = Order.objects.exclude(customer__name='Jane Doe', status='completed').filter(total_amount__gte=50)

for order in orders:
    print(order.id, order.order_date, order.status)
```

## 알아두면 좋은 메서드
### 1. order_by()
* `order_by()` 메서드는 쿼리셋의 데이터를 정렬하는 데 사용됩니다. 

```python
# 특정 고객의 주문 조회 (주문 날짜가 오래된 순서대로) 오름차순
orders = Order.objects.filter(customer__id=1).order_by('order_date')

# 특정 고객의 주문 조회 (주문 날짜가 최신인 순서대로) 내림차순
orders = Order.objects.filter(customer__id=1).order_by('-order_date')

for order in orders:
    print(order.id, order.order_date, order.total_amount)
```
### 2. distinct()
* `distinct()` 메서드는 쿼리셋에서 중복된 결과를 제거하는 데 사용됩니다. 

```python
# 'completed' 상태인 주문을 만든 모든 고객 조회
customers = Customer.objects.filter(order_set__status='completed').distinct()

for customer in customers:
    print(customer.name, customer.email)
```

5. 결론
* Django에서 필터링할 때, filter()와 exclude() 메서드를 활용하여 관련 모델의 데이터를 쉽게 조회할 수 있습니다.
* __(더블 언더스코어)를 사용하여 관계 모델의 필드에 접근하고 필터링 조건을 설정할 수 있습니다.
* exact, contains, gt 등의 연산자를 활용하여 다양한 조건으로 데이터를 필터링할 수 있습니다.

## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)