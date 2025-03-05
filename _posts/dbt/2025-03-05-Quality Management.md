---
title: Quality Management
category: dbt
tag: [dbt]
---

> dbt (Data Build Tool)는 데이터 파이프라인을 효율적으로 구축하고 관리할 수 있도록 돕는 도구입니다. 데이터 모델을 생성하고, 테스트하며, 이를 문서화하고 추적할 수 있는 다양한 기능을 제공합니다. 또한, 성능 최적화를 위한 여러 옵션을 제공하여 데이터 엔지니어링 워크플로우를 개선할 수 있습니다.

---

## Model
dbt는 데이터 모델링을 지원합니다. 이를 통해 데이터 변환을 체계적으로 관리할 수 있으며, 재사용 가능하고 일관된 모델을 구축할 수 있습니다.

{% raw %}
```sql
-- models/my_model.sql

{{
    config(
      materialized = 'incremental',  -- 증분 방식으로 모델 처리
      on_schema_change = 'fail'      -- 스키마 변경 시 실패하도록 설정
    )
}}

WITH sales AS (
    SELECT * FROM {{ source('raw', 'sales') }}  -- sources.yml 테이블 정의
)
SELECT
    product_id,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY product_id
{% if is_incremental() %} -- incremental 방식일 경우 처리
WHERE sales_amount > 0
{% endif %}
```
{% endraw %}

### materialized
`materialized`는 dbt 모델이 어떻게 저장되고 처리될지를 결정하는 중요한 설정입니다. dbt는 여러 가지 방식으로 모델을 처리할 수 있으며, 각각의 방식은 모델을 효율적으로 관리하고 성능을 최적화하는 데 도움이 됩니다.

- `table`: 모델을 테이블로 설정합니다. 
- `view`: 모델을 뷰(View)로 설정합니다. 
- `incremental`: 모델을 증분 방식으로 설정합니다. 
- `ephemeral`: 모델을 임시 테이블로 설정합니다. 

dbt 프로젝트 내에서 기본 `materialized` 값을 설정하려면 `dbt_project.yml `파일을 수정합니다.

```yaml
models:
    +materialized: incremental   # 모든 모델의 기본 materialized 방식을 'incremental'로 설정
    analytics:   # models 폴더 이름
      +materialized: table # analytics모델의 materialized 방식을 'table'로 설정
```

### on_schema_change
`on_schema_change`는 dbt 모델의 스키마 변경에 대한 처리 방법을 정의하는 설정입니다. dbt에서 모델을 실행할 때, 테이블의 스키마가 변경될 경우 어떤 처리를 할지 결정할 수 있습니다. 

- `fail`: 스키마 변경이 발생하면 모델 실행을 실패하도록 처리합니다.
- `ignore`: 스키마 변경을 무시하고 계속 실행합니다.
- `warn`: 스키마 변경이 발생하면 경고를 발생시키고 계속 실행합니다.


### sources.yml
`sources.yml`은 데이터 웨어하우스의 원본 테이블을 정의하는 파일입니다. 이를 통해 `dbt`가 데이터베이스의 특정 테이블을 인식하고 사용할 수 있도록 설정할 수 있으며, `freshness` 설정을 통해 데이터의 최신성을 모니터링할 수도 있습니다.

```yaml
# models/sources.yml

version: 2

sources:
  - name: raw
    schema: raw_data
    tables:
      - name: sales  # dbt에서 사용할 이름
        identifier: sales_data  # 실제 데이터베이스 테이블명
        description: 'Contains transactional sales data'  # 데이터 용도 설명
        loaded_at_field: 'updated_at' # 데이터 최신성을 체크할 기준 컬럼
        freshness:
          warn_after: {count: 12, period: hour}  # 12시간 이상 업데이트 없으면 경고
          error_after: {count: 24, period: hour} # 24시간 이상 업데이트 없으면 오류 발생
```

`dbt source freshness` 명령어는 데이터의 최신성을 확인하는 데 사용됩니다. 이 명령어를 실행하면, 설정된 `freshness` 기준에 따라 데이터가 얼마나 최신 상태인지 확인할 수 있습니다. 

```bash
dbt source freshness
```

---

## Test
dbt는 데이터 테스트를 지원합니다. 이를 통해 데이터의 품질을 자동으로 검증할 수 있으며, 정합성과 유효성을 유지할 수 있습니다. 

{% raw %}
```sql
-- tests/my_test.sql

SELECT * 
FROM {{ ref('dim_sales') }}
WHERE product_id IS NULL -- null 값이 없음을 테스트
```
{% endraw %}

### schema.yml
`schema.yml`은 dbt에서 생성하는 모델을 문서화하고 데이터 테스트를 정의하는 파일입니다. 이 파일을 통해 테이블과 컬럼에 대한 설명을 추가할 수 있으며, 데이터 무결성을 검증할 수 있는 테스트도 정의할 수 있습니다.

```yaml
# models/schema.yml

version: 2

models:
  - name: dim_sales
    description: 'Refined sales data model'   # 모델 설명
    columns:
      - name: product_id
        description: 'Unique product ID'   # 컬럼 설명
        tests:
          - unique   # 고유성 테스트
          - not_null # null 값이 없음을 테스트
      - name: total_sales
        description: 'Total sales for the product'  # 컬럼 설명
```

- `unique`: 특정 컬럼의 값이 고유한지 검사합니다.
- `not_null`: 컬럼의 값이 null이 아닌지 검사합니다.
- `accepted_values`: 컬럼의 값이 지정된 값 목록에 포함되는지 검사합니다.
- `relationships`: 다른 테이블과의 외래키 관계가 올바른지 검사합니다.
- `distinct`: 컬럼 값이 중복 없이 구분되는지 검사합니다.

`dbt test` 명령어는 모델 내에서 정의된 다양한 데이터 테스트(예: 유일성, null 값 체크, 관계 테스트 등)를 실행하는 데 사용됩니다. 이 명령어를 실행하여 모델의 데이터가 정의된 조건을 만족하는지 확인할 수 있습니다.

```bash
dbt test
```

---

## Docs
`dbt Docs`는 dbt 프로젝트에서 `schema.yml`과 `sources.yml` 파일을 기준으로 자동으로 생성되는 문서화 도구입니다. 이 문서화 도구는 모델, 컬럼, 데이터 소스 및 그들 간의 관계를 시각적으로 확인할 수 있도록 도와줍니다

### generate
Docs를 사용하려면 `dbt docs generate` 명령어로 문서를 먼저 생성해야 합니다. 이 명령어는 프로젝트 내의 `schema.yml`과 `sources.yml` 파일을 기반으로 메타데이터를 읽고, 이를 HTML 형식으로 문서화합니다.

```bash
dbt docs generate
```

### serve
문서를 생성한 후, `dbt docs serve` 명령어를 사용하여 로컬 서버에서 시각화된 문서를 확인할 수 있습니다. 이 명령어는 로컬 서버를 실행하고, 웹 브라우저에서 HTML 문서를 탐색할 수 있도록 합니다.

```bash
dbt docs serve
```

서버가 실행되면, 기본적으로 http://localhost:8080에서 DBT Docs를 확인할 수 있습니다.

[![](\assets\posts\{{ page.name }}\docs.png)](\assets\posts\{{ page.name }}\docs.png)

---

## References
- [dbt 공식 문서](https://docs.getdbt.com/docs/introduction)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
