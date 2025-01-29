---
title: History Managing
category: Git
tag: [Git]
---

> Git은 프로젝트의 변경 이력을 효율적으로 관리하는 도구로, 커밋 히스토리를 통해 코드의 모든 변화를 추적할 수 있습니다. Git의 히스토리 관리 기능을 사용하면, 이전 커밋으로 되돌리거나, 불필요한 변경 사항을 제거하며, 협업 중 발생할 수 있는 충돌을 예방하고 코드의 일관성을 유지할 수 있습니다.

---

## Commands

### git reset
커밋을 취소하거나 되돌릴 때 사용합니다.
```bash
git reset --soft HEAD~1  # 최근 커밋 취소 (변경 사항 유지)
git reset --hard HEAD~1  # 최근 커밋 취소 (변경 사항 삭제)
```

### git rebase
브랜치를 다른 브랜치 위로 이동시켜 변경 내역을 정리할 수 있습니다.
```bash
git rebase <브랜치명>
```

#### Interactive
`git rebase -i` 명령을 사용하면 여러 개의 커밋을 수정, 삭제, 병합할 수 있습니다.
```bash
git rebase -i HEAD~3
```
이 명령어를 실행하면 편집 모드로 전환되며, 각 커밋을 `pick`, `squash`, `edit` 등의 옵션으로 수정할 수 있습니다.

#### Conflict
Rebase 중 충돌이 발생하면, 수동으로 충돌을 해결한 후 다음 명령어를 실행해야 합니다.
```bash
git rebase --continue
```
만약 rebase를 취소하려면 다음 명령어를 사용합니다.
```bash
git rebase --abort
```

### git revert
기존 커밋 기록을 유지하면서도 변경 사항을 취소할 수 있어 협업 환경에서 안전하게 사용할 수 있습니다.
```bash
git revert <커밋 해시>
```

#### Conflict
Revert 중 충돌이 발생하면, 충돌을 해결한 후 다음 명령어를 실행합니다.
```bash
git revert --continue
```
Revert를 취소하려면 다음 명령어를 사용합니다.

```bash
git revert --abort
```

### git cherry-pick
특정 커밋만 선택하여 현재 브랜치에 적용할 수 있습니다.
```bash
git cherry-pick <커밋 해시>
```

#### Conflict
충돌이 발생하면, 수동으로 충돌을 해결한 후 다음 명령어를 실행합니다.
```bash
git cherry-pick --continue
```
취소하려면 다음 명령어를 사용합니다.
```bash
git cherry-pick --abort
```

---

## References
- [Git 공식 문서](https://git-scm.com/doc/)

<nav class="post-toc" markdown="1">
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>