---
title: Testing and Debugging
category: Python
tag: [Python]
---

> Python에서 테스트와 디버깅은 코드의 품질을 보장하고, 버그를 최소화하며, 프로그램의 안정성을 높이는 데 중요한 역할을 합니다. Python은 로깅, 디버깅 툴, 단위 테스트 등의 다양한 방법을 제공합니다. 

---

## Logging
`로깅(Logging)`은 프로그램 실행 중에 발생하는 이벤트를 기록하는 기법입니다. 로깅을 사용하면 코드가 실행되는 동안 발생하는 오류, 경고, 정보 메시지 등을 추적할 수 있습니다. `logging` 모듈은 다양한 로그 레벨을 지원하여 상황에 맞게 로그 메시지를 기록할 수 있습니다.

```python
import logging

# 로그 레벨 설정
logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
# 각 로그 레벨에 맞는 메시지가 콘솔에 출력됨.
```
`logging` 모듈은 다양한 로그 레벨을 제공하며, `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` 순으로 로그의 중요도를 설정할 수 있습니다. 기본적으로 `logging.basicConfig`를 사용하여 로그의 레벨과 출력 형식을 지정할 수 있습니다.

---

## Debugging
디버깅 툴은 프로그램 실행 중 오류를 추적하고 수정하는 데 사용됩니다. Python에서 가장 많이 사용되는 디버깅 툴은 `PDB(Python Debugger)`입니다. PDB를 사용하면 코드 실행을 단계별로 추적하고, 변수 값을 확인하며, 중단점을 설정할 수 있습니다.

```python
import pdb

def test_function():
    x = 10
    y = 20
    pdb.set_trace() # 여기서 디버깅 시작
    z = x + y
    print(z)

test_function()
# 코드 실행을 중단하고 PDB 대화식 디버깅 환경이 시작됩니다.
```
`pdb.set_trace()`는 코드 실행을 멈추고 대화식 디버깅 환경을 시작하는 역할을 합니다. 이때 변수 값을 확인하거나, 실행 흐름을 제어할 수 있습니다.

---

## Unit Testing 
단위 테스트(Unit Testing)는 코드의 작은 단위인 함수나 메서드가 예상대로 작동하는지 확인하는 작업입니다. Python에서 단위 테스트를 작성하는 데 가장 많이 사용되는 라이브러리는 `unittest`와 `pytest`입니다.

### Unittest
`unittest`는 Python의 표준 라이브러리로, 단위 테스트를 작성하고 실행하는 데 사용됩니다.

```python
import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
# 테스트가 통과되면 아무 메시지 없이 종료됨.
```
`unittest` 모듈을 사용하면 `assertEqual`, `assertTrue` 등의 메서드를 사용하여 예상 결과와 실제 결과를 비교할 수 있습니다.

### Pytest
`pytest`는 더 간결하고 직관적인 테스트를 작성할 수 있게 해주는 라이브러리입니다. `pytest`는 `unittest`와 호환되지만, 더 많은 기능과 유연성을 제공합니다.

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

# pytest로 실행하면 자동으로 test_add 함수가 테스트됩니다.
```
`pytest`는 `assert` 문을 사용하여 조건을 검사합니다. `pytest`를 사용하면 테스트 실행이 더 간단하고, 다양한 옵션을 통해 테스트 결과를 확인할 수 있습니다.

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
