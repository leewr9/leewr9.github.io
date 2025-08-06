---
title: Package Manager
category: Python
tag: [Poetry, uv, Python]
---

> Python 프로젝트에서는 의존성 관리, 가상환경 구성, 패키지 배포 등 반복적인 작업을 효과적으로 처리할 수 있는 패키지 매니저의 선택이 중요하다. 최근에는 속도와 단순함을 앞세우거나 안정성과 통합 기능을 갖춘 도구가 주목받고 있으며, 개발자의 워크플로우에 맞춰 다양한 방식으로 활용되고 있다.

---

## uv

`uv`는 가볍고 직관적인 파이썬 패키지 및 프로젝트 관리 도구입니다. `pyproject.toml` 파일을 기반으로 프로젝트 의존성을 관리하고, 빠르고 간단한 명령어로 개발 워크플로우를 지원합니다.

- Rust 기반으로 매우 빠르고 가벼움
- `uv add`, `uv sync` 등 직관적인 명령어
- `pyproject.toml` 기반의 표준 프로젝트 관리
- 가상환경, Python 설치, 빌드 기능 내장

### Commands

```bash
pip install uv

# 프로젝트 초기화
uv init uv_project
cd uv_project

# 패키지 추가
uv add requests

# 의존성 설치
uv sync

# Python 실행
uv run python

# 패키지 빌드
uv build

# PyPI 배포
uv publish
```

`uv`를 설치하고 프로젝트를 초기화한 뒤, 패키지를 추가하고 빌드 및 배포까지 진행하는 기본 흐름입니다.

### Structure

```plaintext
uv_project
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
└── README.md
```

`uv init`으로 생성된 프로젝트 기본 구조입니다. `main.py`는 진입점 스크립트로 자동 생성되며, .`python-version`은 uv가 사용하는 Python 버전을 명시합니다.

---

## Poetry

`Poetry`는 강력하고 통합적인 파이썬 의존성 및 패키지 관리 도구입니다. 특히 의존성 충돌 해결, 패키지 배포, 가상환경 관리 등 다양한 기능을 공식적으로 지원합니다.

- 의존성 관리, 빌드, 배포까지 통합 지원
- `poetry.lock`으로 안정적인 환경 보장
- 자동 가상환경 생성 및 `poetry run` 실행
- PyPI 배포 및 프로젝트 초기화 기능 내장

### Commands

```bash
pip install poetry

# 프로젝트 초기화
poetry new poetry_project
cd poetry_project

# 패키지 추가
poetry add requests

# 의존성 설치
poetry install

# Python 실행
poetry run python

# 패키지 빌드
poetry build

# PyPI 배포
poetry publish
```

`poetry`를 설치하고 프로젝트를 초기화한 뒤, 패키지를 추가하고 빌드 및 배포까지 진행하는 기본 흐름입니다.

### Structure

```plaintext
poetry_project
├── pyproject.toml
├── README.md
├── src
│   └── poetry_project
│       └── __init__.py
└── tests
    └── __init__.py
```

`poetry new`로 생성된 프로젝트 기본 구조입니다. `src/` 폴더 아래에 실제 패키지 소스가 위치하며, `tests/` 폴더에는 테스트 코드가 들어갑니다.

## pyproject.toml

`pyproject.toml`은 프로젝트의 메타데이터와 의존성, 빌드 설정 등을 정의하는 중앙 설정 파일로, 패키지 추가, 설치, 빌드, 배포 시 참조됩니다.

- uv
  ```toml
  [project]
  name = "uv-project"
  version = "0.1.0"
  description = "Add your description here"
  readme = "README.md"
  requires-python = ">=3.11"
  dependencies = [
      "requests>=2.32.4",
  ]
  ```
- Poetry

  ```toml
  [project]
  name = "poetry-project"
  version = "0.1.0"
  description = ""
  authors = [
      {name = "User Name",email = "User Email"}
  ]
  readme = "README.md"
  requires-python = ">=3.12"
  dependencies = [
      "requests (>=2.32.4,<3.0.0)"
  ]

  [tool.poetry]
  packages = [{include = "poetry_project", from = "src"}]


  [build-system]
  requires = ["poetry-core>=2.0.0,<3.0.0"]
  build-backend = "poetry.core.masonry.api"
  ```

---

## References

- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
