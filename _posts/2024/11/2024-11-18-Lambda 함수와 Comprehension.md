---
title: Lambda 함수와 Comprehension
category: Study
tag: [Education, Python]
---

<nav class="post-toc" markdown="1">
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

## 람다 함수 (Lambda Function)
> 람다 함수는 익명 함수를 생성하는 방식으로, 한 줄로 짧고 간결한 함수를 정의할 수 있게 해줍니다. lambda 키워드를 사용하여 정의합니다.

### 1. 기본 문법
```python
lambda arguments: expression

# arguments: 함수에 전달될 인자
# expression: 반환되는 값
```

```python
add = lambda x, y: x + y
print(add(3, 5))  # 8

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x * y, list1, list2))
print(result)  # [4, 10, 18]
```

## 컴프리헨션 (Comprehension)
> 컴프리헨션은 반복문을 사용하여 새 리스트, 집합, 딕셔너리 등을 생성할 때 유용한 Python의 구문입니다. 
주로 리스트 컴프리헨션을 많이 사용하지만, 셋 컴프리헨션과 딕셔너리 컴프리헨션도 존재합니다.

### 1. 리스트 컴프리헨션 (List Comprehension)
리스트 컴프리헨션을 사용하면 for 루프를 한 줄로 표현할 수 있습니다.

#### 기본 문법
```python
[expression for item in iterable if condition]

# expression: 각 아이템에 대해 수행할 작업
# item: 순회하는 각 요소
# iterable: 순회할 수 있는 객체 (리스트, 튜플 등)
# condition: 선택적인 조건 (선택적)
```

```python
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]

squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

words = ["apple", "Banana", "cherry", "Date"]
uppercase_words = [word for word in words if word[0].isupper()]
print(uppercase_words)  # ['Banana', 'Date']
```

### 2. 셋 컴프리헨션 (Set Comprehension)
> 셋 컴프리헨션은 리스트 컴프리헨션과 유사하지만, 중복이 없는 **셋(set)**을 생성합니다.

```python
even_numbers_set = {x for x in range(1, 11) if x % 2 == 0}
print(even_numbers_set)  # {2, 4, 6, 8, 10}
```

### 3. 딕셔너리 컴프리헨션 (Dictionary Comprehension)
> 딕셔너리 컴프리헨션을 사용하면 키와 값을 간결하게 생성할 수 있습니다.

```python
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## 람다 함수와 컴프리헨션 결합
> 람다 함수와 컴프리헨션을 결합하면, 더욱 효율적으로 데이터를 처리할 수 있습니다.

```python
numbers = [1, 2, 3, 4, 5, 6]
squares_of_even = [lambda x: x**2 for x in numbers if x % 2 == 0]
result = [f(2) for f in squares_of_even]  # [4, 16, 36]
```
