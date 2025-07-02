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

```plaintext
uv_project
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
└── README.md
```

---

## Poetry
`Poetry`는 강력하고 통합적인 파이썬 의존성 및 패키지 관리 도구입니다. 특히 의존성 충돌 해결, 패키지 배포, 가상환경 관리 등 다양한 기능을 공식적으로 지원합니다.

- 의존성 관리, 빌드, 배포까지 통합 지원
- `poetry.lock`으로 안정적인 환경 보장
- 자동 가상환경 생성 및 `poetry run` 실행
- PyPI 배포 및 프로젝트 초기화 기능 내장

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

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
