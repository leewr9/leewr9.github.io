---
title: Object-Oriented Programming
category: Python
tag: [Python]
---

> 객체지향 프로그래밍(Object-Oriented Programming)은 데이터를 객체로 표현하고, 이 객체들이 상호작용하도록 설계하는 프로그래밍 패러다임입니다. Python은 객체지향 언어로 설계되어 클래스, 상속, 다형성 등 OOP의 다양한 개념을 지원합니다.

---

## Classes and Objects  
클래스는 객체를 생성하기 위한 설계도입니다. 객체는 클래스의 인스턴스(instance)입니다.

```python
# 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

# 객체 생성
person = Person("Alice", 25)

# 메서드 호출
print(person.greet()) # 출력: Hello, my name is Alice.
```

---

## Inheritance and Polymorphism  
상속은 기존 클래스를 기반으로 새로운 클래스를 만드는 것을 의미하며, 다형성은 같은 메서드가 다른 클래스에서 다르게 동작하도록 합니다.

```python
# 부모 클래스
class Animal:
    def speak(self):
        return "I make a sound."

# 자식 클래스
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 객체 생성
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
# 출력: 
# Woof!
# Meow!
```

---

## Methods and Attributes  
속성은 객체의 데이터를 저장하며, 메서드는 객체의 동작을 정의합니다.

```python
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10

# 객체 생성
car = Car("Toyota", 50)
print(car.speed) # 출력: 50

# 메서드 호출
car.accelerate()
print(car.speed) # 출력: 60
```

---

## Abstract Classes and Interfaces  
추상 클래스는 구현되지 않은 메서드를 가지며, 이를 상속받는 클래스에서 반드시 구현해야 합니다.

```python
from abc import ABC, abstractmethod

# 추상 클래스
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# 추상 클래스 상속
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 객체 생성
rect = Rectangle(5, 10)
print(rect.area()) # 출력: 50
```

---

## Magic Methods and Operator Overloading  
매직 메서드는 특별한 이름의 메서드로, 연산자 오버로딩을 통해 객체 간 연산을 정의할 수 있습니다.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# 객체 생성 및 연산
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3) # 출력: Vector(4, 6)
```

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
