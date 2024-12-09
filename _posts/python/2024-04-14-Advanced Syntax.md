---
title: Advanced Syntax
category: Python
tag: [Syntax, Python]
---

> Python의 고급 문법은 보다 효율적이고 세련된 코드를 작성하는 데 유용한 기능들을 제공합니다.

---

## Lambda Functions
람다 함수는 익명 함수로, 함수를 한 줄로 정의할 수 있게 해줍니다. 기본적으로 `lambda` 키워드를 사용하여 간단한 함수를 작성할 때 유용합니다.

```python
# 두 수의 합을 반환하는 함수
add = lambda x, y: x + y

print(add(3, 5))  # 출력: 8
```
람다 함수는 주로 짧은 함수나 일시적인 함수가 필요할 때 유용합니다. 예를 들어, 리스트에서 값을 처리할 때 자주 사용됩니다.

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))

print(squared)  # 출력: [1, 4, 9, 16]
```

---

## List and Dictionary Comprehension
리스트 컴프리헨션은 단일 줄에서 리스트를 생성하는 방법입니다. 동일한 방식으로 딕셔너리 컴프리헨션도 가능합니다. 컴프리헨션을 사용하면 코드가 더 간결하고 읽기 쉬워집니다.

### List Comprehension
```python
# 1부터 5까지의 제곱수를 구하는 리스트 컴프리헨션
squares = [x**2 for x in range(1, 6)]

print(squares)  # 출력: [1, 4, 9, 16, 25]
```

### Dictionary Comprehension
```python
# 1부터 5까지의 숫자를 키로, 제곱수를 값으로 가지는 딕셔너리
squared_dict = {x: x**2 for x in range(1, 6)}

print(squared_dict)  # 출력: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## Decorators and Closures

### Decorators
데코레이터는 함수를 수정하거나 확장할 수 있게 해주는 기능입니다. 데코레이터는 다른 함수를 인수로 받아, 그 함수의 실행을 수정하거나 확장합니다.

```python
# 함수 실행 전, 후에 메시지를 출력
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()
# 출력:
# Before the function call
# Hello!
# After the function call
```
데코레이터는 주로 함수나 메서드의 동작을 수정할 때 사용됩니다. `@decorator` 구문을 통해 함수에 적용할 수 있습니다.

### Closures
클로저는 함수 안에서 정의된 다른 함수로, 외부 함수의 변수를 기억하는 특성을 가집니다.

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

closure_func = outer(10)
print(closure_func(5))  # 출력: 15
```
위 예시에서 `inner` 함수는 `outer` 함수의 `x` 변수를 기억하고 있습니다. 이것이 바로 클로저의 특징입니다.

---

## Generators
제너레이터는 한 번에 하나씩 값을 반환하는 함수입니다. 제너레이터는 `yield` 키워드를 사용하여 값을 반환합니다. 제너레이터는 메모리 효율적이며, 대량의 데이터를 처리할 때 유용합니다.

```python
# 1부터 3까지의 숫자를 하나씩 반환
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(3)

for num in counter:
    print(num)
# 출력:
# 1
# 2
# 3
```
yield는 값을 반환하고 함수의 실행 상태를 중단하며, 나중에 다시 실행을 재개할 수 있습니다. 제너레이터는 데이터를 순차적으로 처리할 때 유용합니다.

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
