---
title: Basic Syntax
category: Python
tag: [Syntax, Python]
---

> Python은 간결하고 직관적인 문법을 제공합니다. Python의 기본적인 문법을 이해하는 것은 더 효율적인 코드를 작성하는 데 중요합니다.

---

## Variables and Data Types
Python은 동적 타입 언어로, 변수에 값을 할당할 때 그 타입이 자동으로 결정됩니다. 주요 데이터 타입에는 정수(int), 실수(float), 문자열(str), 불리언(bool) 등이 있습니다.

```python
# 변수 선언과 데이터 타입
x = 42          # int
y = 3.14        # float
name = "Bob"    # str
is_active = True # bool

print(x)         # 출력: 42
print(y)         # 출력: 3.14
print(name)      # 출력: Bob
print(is_active) # 출력: True
```

---

## Operators
Python에서는 다양한 연산자를 사용하여 값을 계산하거나 비교할 수 있습니다. 주요 연산자에는 산술 연산자, 비교 연산자, 논리 연산자 등이 있습니다.

```python
# 산술 연산자
a = 10
b = 3
print(a + b)  # 출력: 13
print(a - b)  # 출력: 7
print(a * b)  # 출력: 30
print(a ** b) # 출력: 1000 (제곱)
print(a / b)  # 출력: 3.333...
print(a // b)  # 출력: 3 (정수 몫만 반환)

# 비교 연산자
print(a > b)  # 출력: True
print(a == b) # 출력: False

# 논리 연산자
print(a > b and b < 5)  # 출력: True
print(a > b or b == 5)  # 출력: True
```

---

## Conditionals 
Python에서 조건문은 `if`, `elif`, `else` 키워드를 사용하여 조건에 따라 코드 블록을 실행할 수 있습니다.

```python
age = 18

if age < 18:
    print("Minor")
elif age >= 18 and age < 65:
    print("Adult")
else:
    print("Senior")
# 출력: Adult
```

---

## Loops
반복문은 일정한 조건을 만족하는 동안 코드를 반복적으로 실행하는 데 사용됩니다. `for`문과 `while`문이 있습니다.

### for Loop
```python
# for문: 범위 내에서 반복
for i in range(3):
    print(i)
# 출력:
# 0
# 1
# 2
```

### while Loop
```python
# while문: 조건이 참인 동안 반복
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
# 출력:
# Count: 0
# Count: 1
# Count: 2
```

---

## Function Definition and Call
함수는 특정 작업을 수행하는 코드 블록입니다. def 키워드를 사용하여 함수를 정의하고, 이를 호출하여 사용할 수 있습니다.

```python
# 함수 정의
def greet(name):
    return f"Hello, {name}!"

# 함수 호출
print(greet("Alice"))  # 출력: Hello, Alice!
```

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
