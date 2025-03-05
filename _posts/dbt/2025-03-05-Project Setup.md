---
title: Project Setup
category: dbt
tag: [dbt]
---

> dbt (Data Build Tool)는 데이터 변환 작업을 SQL로 처리하고, ETL 파이프라인에서 데이터를 변환하는 데 초점을 맞춘 도구입니다. dbt는 데이터를 변환하고 모델링하는 과정을 간소화하여 데이터 엔지니어링을 효율적으로 수행할 수 있게 해줍니다. 

---

## Setting
dbt를 설치하려면 먼저 Python 환경에서 `pip` 명령어로 dbt를 설치한 후, `dbt init` 명령어로 새로운 dbt 프로젝트를 생성해야 합니다. 

```bash
python install dbt-core dbt-postgres # PostgreSQL 환경 설치

# 새로운 dbt 프로젝트 생성
dbt init my_project   
```

이 과정에서 dbt의 기본적인 프로젝트 구조와 설정 파일들이 자동으로 구성됩니다.

---

## Project Structure
dbt 프로젝트는 특정 구조를 따릅니다. dbt 프로젝트의 기본 구조는 다음과 같습니다:

```plaintext
my_project/
├── models/               # SQL 변환 모델 파일들.
│   └── my_model.sql      # 모델 파일
├── analyses/             # 데이터 분석을 위한 SQL 쿼리 파일들.
├── macros/               # 재사용 가능한 SQL 함수들.
├── snapshots/            # 데이터 스냅샷 관리 파일들.
├── seeds/                # CSV 파일 기반의 정적 데이터 저장 폴더.
├── tests/                # 모델에 대한 테스트 파일들.
├── target/               # dbt 실행 후 생성된 파일들.
├── dbt_project.yml       # dbt 프로젝트 설정 파일.
└── profiles.yml          # 데이터베이스 연결 설정 파일.
```

- `models/`: SQL 모델 파일들이 저장되는 폴더
- `dbt_project.yml`: dbt 프로젝트의 기본 설정을 포함하는 파일
- `profiles.yml`: 데이터베이스 연결 정보가 포함된 파일
  ```yaml
  # %USERPROFILE%/.dbt/profiles.yml 기본 생성 경로

  my_project:
    target: dev
    outputs:
      dev:
        type: postgres
        host: localhost
        user: my_user
        password: my_password
        dbname: my_db
        schema: public
  ```

---

## Running Models
dbt 프로젝트를 설정한 후에는 실제로 데이터 모델을 실행할 수 있습니다. 
dbt 모델은 `.sql` 파일로 작성되며, 데이터베이스에서 실행되어 데이터를 변환합니다. 

{% raw %}
```sql
-- models/model_a.sql

WITH sales AS (
    SELECT * FROM raw_data.sales_data
)
SELECT
    product_id,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY product_id
```
{% endraw %}

{% raw %}
```sql
-- models/model_b.sql

WITH sales_data AS (
    SELECT * FROM {{ ref('model_a') }} -- model_a 쿼리 결과
)
SELECT
    product_id,
    total_sales
FROM sales_data
ORDER BY total_sales DESC
LIMIT 10
```
{% endraw %}

{% raw %}
 `{{ ref('model_a') }}` 구문은 dbt에게 `model_a` 모델을 먼저 실행하고 결과를 참조하라는 의미입니다. 
이렇게 하면 dbt가 의존성 순서대로 모델을 실행할 수 있습니다.
{% endraw %}

```bash
dbt run
```

위 명령어로 프로젝트에 정의된 모든 모델을 실행하고, dbt는 자동으로 `model_a`를 먼저 실행한 후, `model_b`를 실행하여 결과를 데이터베이스에 반영합니다.

```bash
Running with dbt=1.0.0
Found 2 models, 0 tests, 0 snapshots, 0 analyses, 205 macros, 0 operations, 0 seed files, 0 sources, 0 exposures

15:23:45 | Starting run with dbt=1.0.0
15:23:45 | Using profile "my_project" (dev)
15:23:45 | Connecting to the database...
15:23:45 | Found models:
  - model_a
  - model_b

15:23:46 | Executing model 'my_project.model_a'
15:23:47 | [INFO] model_a: Model successfully executed.
15:23:47 | Executing model 'my_project.model_b'
15:23:48 | [INFO] model_b: Model successfully executed.

15:23:48 | Run succeeded.

Completed successfully in 2.35s
```

---

## References
- [dbt 공식 문서](https://docs.getdbt.com/docs/introduction)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
