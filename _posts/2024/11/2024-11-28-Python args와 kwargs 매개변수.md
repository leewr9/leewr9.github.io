---
title: Python args와 kwargs 매개변수
category: Study
tag: [Education, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## `*args` (가변 위치 인수)
* `*args`는 함수에서 위치 인수를 가변적으로 받을 때 사용됩니다.
* `*args`는 튜플로 인수를 받습니다.

```python
def print_numbers(`*args`):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4, 5)

# 1
# 2
# 3
# 4
# 5
```

## `**kwargs` (가변 키워드 인수)
* `**kwargs`는 함수에서 키워드 인수를 가변적으로 받을 때 사용됩니다.
* `**kwargs`는 딕셔너리로 인수를 받습니다.
* `**kwargs`는 반드시 함수의 마지막에 와야 합니다.

```python
def print_info`(**kwargs`):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, job="Developer")

# name: John
# age: 30
# job: Developer
```

## `*args`와 `**kwargs`의 결합
* `*args`와 `**kwargs`는 함수에 함께 사용할 수 있습니다.
* `*args`는 위치 인수, `**kwargs`는 키워드 인수를 받습니다.
* `*args`는 `**kwargs`보다 먼저 나와야 하며, 그 뒤에 `**kwargs`를 사용할 수 있습니다.
* a와 b는 필수 위치 인수로 받으며, 그 후에 `*args`로 나머지 위치 인수들을 받고, 마지막으로 `**kwargs`로 키워드 인수들을 받습니다.

```python
def mixed_example(a, b, `*args`, `**kwargs`):
    print(a, b)
    print(args)
    print(kwargs)

mixed_example(1, 2, 3, 4, name="John", age=30)

1 2
(3, 4)
{'name': 'John', 'age': 30}
```

## `*args`와 `**kwargs`의 활용
> `*args`와 `**kwargs`를 사용하면 유연한 함수 설계가 가능합니다.
매개변수의 수가 동적으로 변화하는 경우에 유용하며, 기본값을 설정하거나 필수 인수를 요구할 때 효과적으로 사용됩니다.

```python
def flexible_func(a, b, `*args`, `**kwargs`):
    print(f"a: {a}, b: {b}")
    print(f"Additional args: {args}")
    print(f"Keyword args: {kwargs}")

flexible_func(1, 2, 3, 4, 5, name="John", age=30)

a: 1, b: 2
Additional args: (3, 4, 5)
Keyword args: {'name': 'John', 'age': 30}
```

{% endraw %}