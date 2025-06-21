---
title: Analysis Tools
category: Python
tag: [Python]
---

> Python은 동적 언어이기 때문에 정적 분석의 효과가 더욱 중요합니다. 잘 활용하면 코드 품질과 유지보수성을 획기적으로 높일 수 있습니다. 정적 분석이란 프로그램을 실행하지 않고 소스 코드를 분석하여 잠재적인 오류, 스타일 위반, 타입 불일치 등을 사전에 검출하는 기법입니다.

---

## Type Checker 
타입 힌트를 기반으로 코드 내 타입 오류를 사전에 검출하는 도구입니다. 타입 안정성 확보에 집중하며, 코드의 안정성과 유지보수성을 높여줍니다. 

```python
# example.py

def greet(name: str) -> str:
    return "Hello, " + name

print(greet(123))
```

### Pyright
`Pyright`는 Microsoft가 개발한 빠르고 정확한 정적 타입 분석 도구로, VSCode 공식 타입 검사기인 Pylance의 핵심 엔진으로 사용됩니다. 대규모 프로젝트에 적합하며, `pyrightconfig.json`으로 세밀한 설정이 가능합니다.

- 빠르고 정밀한 타입 검사 (TypeScript 기반)
- VSCode 및 Pylance와 완벽 통합
- `pyrightconfig.json`을 통한 유연한 설정 가능

```bash
npm install -g pyright
pyright example.py

#   example.py:7:13 - error: Argument of type "Literal[123]" cannot be assigned to parameter "name" of type "str" in function "greet"      
#     "Literal[123]" is not assignable to "str" (reportArgumentType)
# 1 error, 0 warnings, 0 informations
```

### mypy
`mypy`는 `typing` 모듈 기반 정적 타입 검사기로, 점진적인 타입 적용과 엄격 모드를 지원합니다. 타입 안정성 확보에 중점을 두며, 대규모 프로젝트에서 코드 안전성을 높이는 데 유용합니다.

- `typing` 기반의 정적 타입 검사
- 점진적 타입 적용 및 `--strict` 지원
- `mypy.ini`, `pyproject.toml` 설정 지원

```bash
pip install mypy
mypy example.py

# example.py:7: error: Argument 1 to "greet" has incompatible type "int"; expected "str"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)
```

---

## Code Quality
코드 스타일 점검, 문법 오류 검출, 복잡도 분석 및 자동 코드 포맷팅을 담당합니다. 개발자의 코드 스타일을 통일하고, 코드 품질 향상을 돕습니다.

```python
# example.py

def add(a,b):
    return a+b


x = add(1,2)
print(x)

def unused_func():
    pass
```

### Pylint
`Pylint`는 코드 스타일, 구조, 버그를 포괄적으로 검사하는 도구로, 오랜 역사만큼 안정적이고 강력합니다. 코드 품질을 점수화해 제공하며, 다양한 커스터마이징 옵션과 플러그인을 지원합니다.

- PEP8 기반 스타일, 구조, 버그 검사
- 코드 품질 점수화 (10점 만점)
- `.pylintrc`를 통한 상세 규칙 설정

```bash
pip install pylint
pylint example.py

# ************* Module example
# example.py:11:0: C0304: Final newline missing (missing-final-newline)
# example.py:1:0: C0114: Missing module docstring (missing-module-docstring)        
# example.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
# example.py:7:0: C0103: Constant name "x" doesn't conform to UPPER_CASE naming style (invalid-name)
# example.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
# 
# ------------------------------------------------------------------
# Your code has been rated at 1.67/10 (previous run: 1.67/10, +0.00)
```


### flake8
`flake8`은 `pyflakes`, `pycodestyle`, `mccabe` 세 가지 도구를 통합한 경량 정적 분석기로, 빠른 스타일 검사와 문법 오류 탐지에 특화되어 있습니다. CI/CD와 pre-commit 훅에 자주 사용됩니다.

- PEP8 스타일 위반 및 문법 오류 검사
- `pyflakes`, `pycodestyle`, `mccabe` 통합
- 가볍고 빠르며 pre-commit에 적합

```bash
pip install flake8
flake8 example.py

# example.py:3:10: E231 missing whitespace after ','
# example.py:7:10: E231 missing whitespace after ','
# example.py:10:1: E302 expected 2 blank lines, found 1
# example.py:11:9: W292 no newline at end of file
```


### black
`black`은 설정이 거의 없는 자동 코드 포매터로, 일관된 스타일을 강제하여 코드 스타일 논쟁을 없애고 협업 효율을 극대화합니다. 최소한의 설정만 허용하며, 빠르고 안정적으로 코드를 포맷합니다.

- 설정이 거의 없는 자동 코드 포매터
- 스타일 논쟁 제거, 협업에 적합
- `pyproject.toml`을 통한 최소한의 설정 가능

```bash
pip install black
black example.py

# reformatted example.py
# 
# All done! ✨ 🍰 ✨
# 1 file reformatted.
```

```python
# example.py reformatted


def add(a, b):
    return a + b


x = add(1, 2)
print(x)


def unused_func():
    pass

```

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
