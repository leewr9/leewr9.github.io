---
title: Project Management
category: Python
tag: [Python]
---

> Python 프로젝트를 관리하는 데는 가상환경 설정, 의존성 관리, 코드 스타일 가이드 등의 중요한 측면이 있습니다. 이들 각각의 기법을 활용하면 프로젝트를 효율적으로 관리하고, 다른 개발자와 협업하며, 일관된 코드를 유지할 수 있습니다.

---

## Virtual Environment
`가상환경(Virtual Environment)`은 프로젝트마다 독립적인 Python 환경을 설정하여, 각 프로젝트가 서로 다른 라이브러리 버전을 사용할 수 있게 해줍니다. Python의 `venv`와 `virtualenv`는 가상환경을 생성하는 데 사용되는 도구입니다.

### venv 
Python 3.3 이상에서는 `venv`가 기본적으로 제공됩니다. 가상환경을 만들고 활성화하는 방법은 다음과 같습니다.

```bash
# 가상환경 생성
python -m venv myenv

# Windows에서 가상환경 활성화
myenv\Scripts\activate

# macOS/Linux에서 가상환경 활성화
source myenv/bin/activate

# 가상환경 비활성화
deactivate
```
가상환경을 활성화하면, 프로젝트에 필요한 라이브러리들을 설치하고, 시스템에 영향을 주지 않도록 독립된 환경에서 작업을 진행할 수 있습니다.

### virtualenv
`virtualenv`는 `venv`보다 이전에 사용되던 도구로, Python 2와 Python 3 모두에서 사용 가능합니다.

```bash
# virtualenv 설치
pip install virtualenv

# 가상환경 생성
virtualenv myenv

# 가상환경 활성화 (Windows)
myenv\Scripts\activate

# 가상환경 비활성화
deactivate
```

---

## Dependency Management
Python 프로젝트에서 의존성 관리는 필수적입니다. 프로젝트에 필요한 외부 라이브러리와 그 버전들을 관리하여, 다른 개발자와 협업할 때 동일한 환경을 유지할 수 있습니다. 대표적인 도구로는 `pip`, `pipenv`, `poetry` 등이 있습니다.

### pip
`pip`는 Python의 기본 패키지 관리자입니다. `requirements.txt` 파일을 사용하여 의존성을 관리할 수 있습니다.

```bash
# 패키지 설치
pip install requests

# 설치된 패키지 목록 확인
pip freeze

# requirements.txt 파일로 저장
pip freeze > requirements.txt

# requirements.txt에서 패키지 설치
pip install -r requirements.txt
```
`pip freeze`는 현재 가상환경에 설치된 패키지와 버전 정보를 출력합니다. 이를 `requirements.txt`로 저장하면, 다른 개발자가 동일한 패키지를 설치할 수 있습니다.

### pipenv 
`pipenv`는 `pip`과 `virtualenv`를 결합하여 의존성을 관리하는 도구입니다. `Pipfile`과 `Pipfile.lock`을 사용하여 의존성과 버전을 관리합니다.

```bash
# pipenv 설치
pip install pipenv

# 가상환경과 패키지 설치
pipenv install requests

# 패키지 목록 확인
pipenv graph

# 가상환경 활성화
pipenv shell
```
`pipenv`는 의존성을 자동으로 관리하고, `Pipfile`과 `Pipfile.lock`을 통해 정확한 버전의 패키지들을 기록합니다.

### poetry 
`poetry`는 의존성 관리와 빌드를 한 번에 처리할 수 있는 도구입니다. `pyproject.toml` 파일을 사용하여 의존성과 프로젝트 설정을 관리합니다.

```bash
# poetry 설치
pip install poetry

# 프로젝트 초기화
poetry init

# 패키지 설치
poetry add requests

# 가상환경 활성화
poetry shell
```
`poetry`는 더 발전된 의존성 관리 기능을 제공하며, 배포와 버전 관리도 함께 할 수 있습니다.

---

## Code Style Guide
`PEP 8`은 Python 코드 작성 시 따라야 할 표준 스타일 가이드입니다. PEP 8을 준수하면 코드가 더 일관되고, 가독성이 좋아지며, 다른 개발자와의 협업이 쉬워집니다.

### Guidelines
- 들여쓰기: 공백 4칸 사용
- 라인 길이: 79자 이하로 제한
- 함수 및 변수 이름: 소문자와 밑줄을 사용하여 작성 (예: `my_function`)
- 클래스 이름: 첫 글자를 대문자로 사용 (예: `MyClass`)
- 주석: 주석은 코드의 의도를 설명하는 데 사용하며, 코드가 변경되면 주석도 업데이트해야 합니다.

### Automation Tools

#### flake8 
`PEP 8` 스타일을 검사하는 도구입니다. 코드 스타일이 맞지 않으면 경고를 발생시킵니다.

```bash
pip install flake8

flake8 myscript.py
```

#### black
코드를 자동으로 `PEP 8` 스타일에 맞게 포매팅해주는 도구입니다.

```bash
pip install black

black myscript.py
```

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
