---
title: Command Line Tool
category: GCP
tag: [GCS, BigQuery, GCP]
---

> GCP(Google Cloud Project)는 다양한 서비스를 CLI 명령어로 제어할 수 있도록 지원합니다. 그중에서 BigQuery, gsutil, gcloud 명령어는 데이터 처리 및 관리를 위해 자주 사용됩니다. 이 포스트에서는 Google Cloud CLI의 주요 명령어들과 함께 유용한 옵션을 소개합니다.

---

## Google Cloud Project
`gcloud` 명령어는 `Google Cloud`의 다양한 서비스와 리소스를 관리할 수 있는 가장 기본적인 명령어입니다. 주로 프로젝트 관리, IAM, API 사용 설정, 서비스 배포 등 다양한 작업을 처리합니다.

- `auth`: Google 계정이나 서비스 계정으로 인증 진행
```bash
gcloud auth login # Google 계정
gcloud auth activate-service-account --key-file=[KEY_FILE_PATH] # 서비스 계정
```
- `config`: 현재 작업할 계정이나 프로젝트 설정
```bash
gcloud config set account [ACCOUNT_EMAIL] # 계정 설정
gcloud config set project [PROJECT_ID] # 프로젝트 설정
```

### Project
- 프로젝트 목록 확인
```bash
gcloud projects list
```

### Compute Engine
- 인스턴스 목록 확인
```bash
gcloud compute instances list
```

### API Service
- 서비스 목록 확인
```bash
gcloud services list
```
- 서비스 활성화
```bash
gcloud services enable [SERVICE_NAME]
```
- 서비스 비활성화
```bash
gcloud services disable [SERVICE_NAME]
```

---

## BigQuery
`bq` 명령어는 Google Cloud의 빅데이터 분석 서비스인 `BigQuery`와 관련된 작업을 수행하는 데 사용됩니다. 데이터셋 관리, 테이블 쿼리, 로딩 및 추출 작업을 할 수 있습니다.

- `--project_id=[PROJECT_ID]`: 특정 프로젝트에서 작업을 실행할 때 사용
- `--dataset_id=[DATASET_ID]`: 특정 데이터셋을 지정할 때 사용

### Query
- 쿼리 실행
```bash
bq query 'SELECT * FROM `PROJECT_ID.DATASET_ID.TABLE_ID` LIMIT 100'
```

### Datasets
- 데이터셋 목록 확인
```bash
bq ls
```
- 데이터셋 생성
```bash
bq mk [DATASET_ID]
```

### Table
- 테이블 목록 확인
```bash
bq ls [DATASET_ID]
```
- 스토리지 데이터 기반 테이블 생성
```bash
bq load --source_format=[FORMAT] [DATASET_ID].[TABLE_ID] gs://[BUCKET_NAME]/[FILE]
```
- 테이블 데이터 스토리지 추출
```bash
bq extract --destination_format=[FORMAT] [DATASET_ID].[TABLE_ID] gs://[BUCKET_NAME]/[DESTINATION_PATH]
```

---

## Google Cloud Storage
`gsutil`은 `Google Cloud Storage`와 상호작용할 수 있는 명령어입니다. 이 명령어를 사용하면 클라우드 버킷을 생성하고, 데이터를 업로드하고 다운로드할 수 있습니다.

### Bucket
- 버킷 목록 확인
```bash
gsutil ls
```
- 버킷 생성
```bash
gsutil mb gs://[BUCKET_NAME]
```

### File
- 파일 목록 확인
```bash
gsutil ls gs://[BUCKET_NAME]
```
- 파일 업로드
```bash
gsutil cp [LOCAL_FILE] gs://[BUCKET_NAME]/[DESTINATION_PATH]
```
- 파일 다운로드
```bash
gsutil cp gs://[BUCKET_NAME]/[FILE] [LOCAL_PATH]
```
- 파일 삭제
```bash
gsutil rm gs://[BUCKET_NAME]/[FILE]
```

---

## References
- [GCP 공식 문서](https://cloud.google.com/docs)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
