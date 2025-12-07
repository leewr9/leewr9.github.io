---
title: Automation Markets
category: GitHub
tag: [Marketplace, GitHub Actions, GitHub]
---

> GitHub Actions에서는 자동화 마켓플레이스를 통해 다양한 커뮤니티 제작 액션과 워크플로우 템플릿을 쉽게 찾아 설치할 수 있습니다. 이를 활용하면 복잡한 CI/CD 파이프라인 구축과 워크플로우 자동화를 간편하게 구현할 수 있습니다.

---

## Marketplace

`Marketplace`는 개발자들이 자신들의 워크플로우에 통합할 수 있는 다양한 액션과 애플리케이션을 제공하는 플랫폼입니다. `GitHub`에서 공식적으로 지원하는 액션부터 커뮤니티가 제작한 다양한 도구까지 폭넓게 제공됩니다.

### checkout

`checkout` 액션은 워크플로우 실행 시 저장소의 코드를 체크아웃하는 데 사용됩니다. 이를 통해 이후 단계에서 코드에 접근하고 빌드, 테스트, 배포 작업을 수행할 수 있습니다.

```yaml
- name: Checkout code
  uses: actions/checkout@v5
```

- [`actions/checkout`](https://github.com/marketplace/actions/checkout)

### setup

`setup` 액션은 특정 프로그래밍 언어나 도구의 환경을 설정하는 데 사용됩니다.

- `setup-python`: 파이썬 환경 설정
- `setup-node`: Node.js 환경 설정

```yaml
- name: Set up Python
  uses: actions/setup-python@v6
  with:
    python-version: "3.10" # Python 3.10 설정
- name: Set up Node.js
  uses: actions/setup-node@v6
  with:
    node-version: "14" # Node.js 14 설정
```

- [`actions/setup-python`](https://github.com/marketplace/actions/setup-python)
- [`actions/setup-node`](https://github.com/marketplace/actions/setup-node-js-environment)

### cache

`cache` 액션은 의존성 파일이나 빌드 결과물을 캐싱하여 워크플로우 실행 속도를 향상시키는 데 사용됩니다. 동일한 작업이 반복될 때 실행 시간을 단축할 수 있습니다.

```yaml
- name: Cache dependencies
  id: cache-dependencies
  uses: actions/cache@v4
  with:
    path: ~/.cache/pip # 캐시할 경로
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }} # 캐시 키
- if: steps.cache-dependencies.outputs.cache-hit != 'true' # 캐시가 없을 때만 실행
  name: Install dependencies
  run: pip install -r requirements.txt # 의존성 설치
```

- [`actions/cache`](https://github.com/marketplace/actions/cache)

### artifact

`artifact` 액션은 빌드 결과물이나 테스트 결과를 업로드 및 다운로드하는 데 사용됩니다. 빌드 아티팩트를 저장하고 공유할 수 있습니다.

```yaml
- name: Upload Artifact
  uses: actions/upload-artifact@v4
  with:
    name: test-results
    path: ./upload-results/ # 업로드할 파일 경로
- name: Download Artifact
  uses: actions/download-artifact@v5
  with:
    name: test-results
    path: ./downloaded-results/ # 다운로드할 파일 경로
```

- [`actions/upload-artifact`](https://github.com/marketplace/actions/upload-a-build-artifact)
- [`actions/download-artifact`](https://github.com/marketplace/actions/download-a-build-artifact)

### release

`release` 액션은 저장소에서 릴리즈를 생성하고 관리하는 데 사용됩니다. 버전 태그를 기준으로 릴리즈 노트를 자동 생성하고, 릴리즈를 배포할 수 있습니다.

```yaml
- name: Create Release
  uses: actions/create-release@v1
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  with:
    tag_name: ${{ github.ref }}
    release_name: Release ${{ github.ref }}
    draft: false # 초안 여부
    prerelease: false # 사전 릴리즈 여부
- name: Upload Release Asset
  uses: actions/upload-release-asset@v1
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  with:
    upload_url: ${{ steps.create_release.outputs.upload_url }} # 릴리즈 업로드 URL
    asset_path: ./path/to/asset.zip # 업로드할 파일 경로
    asset_name: asset.zip # 업로드할 파일 이름
    asset_content_type: application/zip # 업로드할 파일 콘텐츠 타입
```

- [`actions/create-release`](https://github.com/actions/create-release)
- [`actions/upload-release-asset`](https://github.com/actions/upload-release-asset)

---

## References

- [GitHub Actions 공식 문서](https://docs.github.com/actions)
- [GitHub 공식 문서](https://docs.github.com/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
