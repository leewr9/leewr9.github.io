---
title: Exception Handling
category: Python
tag: [Python]
---

> 예외 처리(Exception Handling)는 프로그램 실행 중 발생할 수 있는 오류를 안전하게 처리하는 방법입니다. Python에서는 try, except 블록을 사용하여 예외를 처리합니다. 또한, 사용자 정의 예외와 raise 키워드를 통해 예외를 발생시킬 수도 있습니다.

---

## Basic Exceptions
`try` 블록에서 예외가 발생하면 `except` 블록으로 처리하고, 예외가 발생하지 않으면 `else` 블록이 실행됩니다. `finally` 블록은 예외 발생 여부와 관계없이 항상 실행됩니다.

```python
try:
    number = int(input("Enter a number: ")) # 사용자 입력을 받음
    result = 10 / number
except ZeroDivisionError:
    print("Cannot divide by zero.") # 0으로 나눌 때 발생하는 예외 처리
except ValueError:
    print("Invalid input! Please enter a number.") # 숫자가 아닌 값을 입력했을 때 발생하는 예외 처리
else:
    print(f"Result: {result}") # 예외가 없을 경우 실행
finally:
    print("Execution complete.") # 항상 실행되는 블록
```

---

## Advanced Exceptions
### Custom  
사용자 정의 예외를 만들려면 `Exception` 클래스를 상속받은 새로운 예외 클래스를 정의해야 합니다.

```python
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative.") # 사용자 정의 예외 발생
    return age

try:
    check_age(-5)
except CustomError as e:
    print(f"Error: {e}") # Error: Age cannot be negative.
```

### Raising
`raise` 키워드를 사용하면 코드에서 명시적으로 예외를 발생시킬 수 있습니다. 예외 처리는 코드의 안정성을 높이고, 오류가 발생해도 프로그램이 비정상 종료되지 않도록 도와줍니다. 예외 처리를 적절히 활용하면 코드의 가독성도 향상됩니다.

```python
def check_number(number):
    if number < 0:
        raise ValueError("Number must be positive.") # 예외 발생
    return number

try:
    check_number(-10)
except ValueError as e:
    print(f"Error: {e}") # Error: Number must be positive.
```

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
