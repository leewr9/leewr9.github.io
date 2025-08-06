---
title: Basic Command
category: Git
tag: [Git]
---

> Git은 분산 버전 관리 시스템(DVCS)으로, 코드의 변경 사항을 효과적으로 추적하고 협업을 원활하게 진행할 수 있도록 도와줍니다. Git을 사용하면 프로젝트의 변경 이력을 관리하고, 이전 버전으로 되돌릴 수도 있으며, 여러 개발자가 동시에 작업할 때 충돌을 최소화할 수 있습니다.

---

## Commands

### git init

로컬 저장소를 생성할 때 사용합니다.

```bash
git init
```

이 명령어를 실행하면 현재 디렉터리에 `.git` 폴더가 생성되며, Git 저장소로 초기화됩니다.

### git clone

원격 저장소를 로컬로 복제할 때 사용합니다.

```bash
git clone <repository_url>
```

이 명령어를 실행하면 지정된 저장소가 로컬로 다운로드됩니다.

### git add

변경된 파일을 스테이징 영역에 추가합니다.

```bash
git add <파일명>
```

모든 변경 사항을 추가하려면 `git add .`을 사용할 수 있습니다.

### git commit

스테이징된 변경 사항을 로컬 저장소에 기록합니다.

```bash
git commit -m "커밋 메시지"
```

커밋 메시지는 변경 내용을 간단히 설명하는 것이 좋습니다.

### git status

현재 저장소의 상태를 확인합니다.

```bash
git status
```

어떤 파일이 변경되었고, 스테이징되지 않았는지를 확인할 수 있습니다.

### git log

커밋 히스토리를 확인합니다.

```bash
git log
```

옵션을 추가하여 한 줄로 출력할 수도 있습니다.

```bash
git log --oneline
```

### git push

로컬 커밋을 원격 저장소로 업로드합니다.

```bash
git push origin main
```

### git pull

원격 저장소의 최신 변경 사항을 로컬로 가져옵니다.

```bash
git pull origin main
```

### git branch

현재 브랜치를 확인하거나 새로운 브랜치를 생성할 수 있습니다.

```bash
git branch          # 현재 브랜치 목록 확인
```

```bash
git branch <브랜치명>  # 새로운 브랜치 생성
```

### git checkout

브랜치를 전환할 때 사용합니다.

```bash
git checkout <브랜치명>
```

### git merge

다른 브랜치의 변경 사항을 현재 브랜치에 병합합니다.

```bash
git merge <브랜치명>
```

---

## Workflow

일반적인 Git 작업 흐름은 다음과 같습니다.

1. `git clone` 또는 `git init`을 사용하여 저장소를 준비합니다.
2. 변경 사항을 `git add`로 스테이징합니다.
3. `git commit`을 사용하여 변경 사항을 저장합니다.
4. `git push`를 사용하여 원격 저장소에 업로드합니다.
5. 협업 시 `git pull`로 최신 변경 사항을 가져옵니다.

---

## References

- [Git 공식 문서](https://git-scm.com/doc/)

<nav class="post-toc" markdown="1">
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>
