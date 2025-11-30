---
title: Automation Actions
category: GitHub
tag: [GitHub Actions, GitHub]
---

> GitHub에서는 코드 변경, 풀 리퀘스트, 이슈 생성 등 다양한 이벤트에 반응하여 자동으로 작업을 수행할 수 있는 GitHub Actions 기능을 제공합니다. 이를 통해 CI/CD 파이프라인 구축, 코드 빌드/테스트/배포 자동화, 워크플로우 관리 등을 손쉽게 구현할 수 있습니다.

---

## Workflow

`GitHub Actions` 워크플로우는 YAML 형식으로 정의되며, 저장소의 `.github/workflows` 디렉터리에 위치합니다. 워크플로우는 특정 이벤트에 반응하여 실행되며, 하나 이상의 작업으로 구성됩니다. 각 작업은 여러 단계로 이루어져 있습니다.

```yaml

### on

`on` 옵션은 워크플로우를 트리거하는 이벤트를 지정합니다.

```yaml
on:
  push:
    branches:
      - master # master 브랜치에 푸시될 때 실행
  pull_request:
    branches:
      - master # master 브랜치로의 PR 생성/업데이트 시 실행
  schedule:
    - cron: "0 0 * * *" # 매일 자정에 실행
```

- `push`: 특정 브랜치에 푸시될 때 실행
- `pull_request`: 풀 리퀘스트 생성/업데이트 시 실행
- `schedule`: 정기적으로 실행 (cron 형식)

### jobs

`jobs` 옵션은 워크플로우 내에서 실행할 작업(Job)들을 정의하는 블록입니다. 각 Job은 독립적으로 실행되며, 병렬 또는 순차적으로 구성할 수 있습니다.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3 # 코드 체크아웃
      - name: Set up Node.js
        uses: actions/setup-node@v3 # Node.js 설정
        with:
          node-version: "14"
      - name: Install dependencies
        run: npm install # 의존성 설치
      - name: Run tests
        run: npm test # 테스트 실행
```

#### runs-on

`runs-on` 옵션은 해당 Job이 실행될 러너 환경을 지정합니다. GitHub에서 제공하는 호스팅 러너를 사용할 수 있으며, 자체 호스팅 러너도 설정할 수 있습니다.

- `ubuntu-latest`: 최신 우분투 환경
- `windows-latest`: 최신 윈도우 환경
- `macos-latest`: 최신 macOS 환경
- `self-hosted`: 자체 호스팅 러너 사용

#### steps

`steps` 옵션은 Job 내에서 실행할 개별 명령이나 액션 목록을 정의합니다. 각 Step은 순차적으로 실행되며, 외부 액션을 불러오거나 셸 명령어를 직접 실행할 수 있습니다.

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v3 # 외부 액션 사용
  - name: Run a script
    run: echo "Hello, World!" # 명령어 실행
```

- `uses`: 외부 액션(공식/서드파티)을 불러와 실행
- `run`: 명령어 직접 실행

---

## Options

`GitHub Actions`는 다양한 추가 옵션을 제공하여 세부 동작을 제어할 수 있습니다. 이로 인해 복잡한 워크플로우도 유연하게 구성할 수 있습니다.

{% raw %}

```yaml
name: Example Additional Options
on:
  push:
    branches: [ master ]
env:
  GLOBAL_ENV: production
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10] # 여러 Python 버전에서 테스트
        os: [ubuntu-latest, windows-latest] # 여러 OS 환경에서 테스트
    timeout-minutes: 20 # 최대 실행 시간 20분
    continue-on-error: true # 실패해도 계속 실행
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }} # matrix에서 지정한 Python 버전 사용
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests (only on master branch)
        if: github.ref == 'refs/heads/master' # master 브랜치에서만 실행
        run: pytest
      - name: Use secret value
        run: echo "Secret: ${{ secrets.MY_SECRET }}" # 시크릿 값 사용

  deploy:
    runs-on: ubuntu-latest
    needs: test # test 작업 완료 후 실행
    steps:
      - name: Deploy
        run: echo "Deploying..."
```

{% endraw %}

- `env`: 환경 변수 지정
- `secrets`: 저장소에 등록된 시크릿 값 사용
- `if`: 조건부 실행
- `timeout-minutes`: 작업의 최대 실행 시간 제한
- `continue-on-error`: 실패해도 다음 작업 계속 실행
- `needs`: Job 간 실행 순서/의존성 지정
- `strategy`: 여러 환경/버전 반복 실행 (`matrix` 활용)
- `with`: 액션에 인자/옵션 전달

---

## References

- [GitHub Actions 공식 문서](https://docs.github.com/actions)
- [GitHub 공식 문서](https://docs.github.com/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
