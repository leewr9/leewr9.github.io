---
title: Query Optimization
category: PostgreSQL
tag: [Materialized View, Partition, Index, Database, SQL, PostgreSQL]
---

> PostgreSQL은 단순한 데이터 저장소를 넘어, 쿼리 성능 최적화를 위한 다양한 기능을 내장하고 있습니다. 이러한 기능들은 대용량 데이터 처리와 복잡한 질의에서도 빠르고 효율적인 응답을 가능하게 하며, 데이터베이스 내부에서 최적화 로직을 수행함으로써 애플리케이션의 부담을 줄여줍니다.

---

## Indexing
`Indexing`는 테이블에서 특정 컬럼의 검색을 빠르게 하기 위해 사용되는 기능입니다. 인덱스를 사용하면 테이블 전체를 스캔하는 대신 인덱스를 통해 원하는 데이터를 빠르게 찾을 수 있습니다. 기본적으로 `B-Tree` 기반 인덱스를 사용하며, 이는 정렬된 데이터 구조에서 이진 탐색으로 빠르게 원하는 값을 찾아가는 방식입니다.

```sql
CREATE INDEX idx_employees_salary ON employees(salary);

EXPLAIN ANALYZE SELECT * FROM employees WHERE salary > 6000 ORDER BY salary DESC;
```

```sql
 Sort  (cost=29.84..30.49 rows=260 width=76) (actual time=0.025..0.026 rows=0 loops=1)
   Sort Key: salary DESC
   Sort Method: quicksort  Memory: 25kB
   ->  Bitmap Heap Scan on employees  (cost=6.17..19.41 rows=260 width=76) (actual time=0.021..0.021 rows=0 loops=1)
         Recheck Cond: (salary > 6000)
         ->  Bitmap Index Scan on idx_employees_salary  (cost=0.00..6.10 rows=260 width=0) (actual time=0.002..0.003 rows=0 loops=1)
               Index Cond: (salary > 6000)
 Planning Time: 1.486 ms
 Execution Time: 0.055 ms
 ```

- `Hash`: 동등 비교에만 최적화, 범위 검색 불가 (PostgreSQL 10 이상부터 WAL 지원)
```sql
CREATE INDEX idx_employees_name_hash ON employees USING hash(name);
```
- `GIN`: 배열, JSON, 텍스트 검색에 특화된 다중 값 인덱스
```sql
CREATE INDEX idx_employees_tags ON employees USING GIN(tags); -- Generalized Inverted Index
```
- `GiST`: 공간 데이터 및 범위 검색에 사용되는 인덱스
```sql
CREATE INDEX idx_employees_location ON employees USING GiST(location); -- Generalized Search Tree
```
- `BRIN`: 대용량 테이블에서 연속된 값 컬럼에 적합, 매우 작은 크기
```sql
CREATE INDEX idx_employees_hiredate_brin ON employees USING BRIN(hire_date); -- Block Range Index
```

---

## Partitioning
`Partitioning`은 큰 테이블을 파티션 키 기준으로 여러 작은 테이블으로 나누어 관리하는 기능입니다. 특정 파티션만 스캔함으로써 성능을 높이고, 데이터 관리가 용이해집니다.

### Range Partitioning
`Range Partitioning`은 연속된 값을 기준으로 데이터를 분할합니다. 쿼리에서 `BETWEEN`, `>=`, `<=` 조건이 자주 사용되는 컬럼에 적합하며, 조회 시 자동으로 해당 범위의 파티션만 스캔하게 되어 성능이 향상됩니다.

````sql
CREATE TABLE range_partitioned (
    id INT,
    name TEXT,
    created_at DATE
) PARTITION BY RANGE (created_at);

CREATE TABLE range_partitioned_2023 PARTITION OF range_partitioned
    FOR VALUES FROM ('2023-01-01') TO ('2024-01-01');

CREATE TABLE range_partitioned_2024 PARTITION OF range_partitioned
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
    
EXPLAIN SELECT * FROM range_partitioned
WHERE created_at BETWEEN '2023-06-01' AND '2023-06-30';
````

```sql
 Seq Scan on range_partitioned_2023 range_partitioned  (cost=0.00..28.00 rows=6 width=40)
   Filter: ((created_at >= '2023-06-01'::date) AND (created_at <= '2023-06-30'::date))
```

### List Partitioning
`List Partitioning`은 컬럼 값의 명시된 리스트에 따라 데이터를 분할합니다. 주로 범주형 데이터를 분리할 때 유용하며, 제한된 값을 가진 컬럼에 적합합니다. 각 파티션은 특정 값 목록에 대해 정의되고, 해당 값이 입력되면 자동으로 그 파티션에 저장됩니다.

```sql
CREATE TABLE list_partitioned (
    id INT,
    name TEXT,
    country TEXT
) PARTITION BY LIST (country);

CREATE TABLE list_partitioned_kr PARTITION OF list_partitioned
    FOR VALUES IN ('KR');

CREATE TABLE list_partitioned_us PARTITION OF list_partitioned
    FOR VALUES IN ('US');
    
EXPLAIN SELECT * FROM list_partitioned WHERE country = 'KR';
```

```sql
 Seq Scan on list_partitioned_kr list_partitioned  (cost=0.00..20.62 rows=4 width=68)
   Filter: (country = 'KR'::text)
```

### Hash Partitioning
`Hash Partitioning`은 특정 컬럼의 해시값을 기반으로 데이터를 균등하게 분산합니다. 이는 데이터 값 자체에 연속성이나 범주성이 없을 때 유용하며, 보통 고르게 분산된 파티션 구조를 만들고 싶을 때 사용합니다.


```sql
CREATE TABLE hash_partitioned (
    id INT,
    name TEXT
) PARTITION BY HASH (id);

CREATE TABLE hash_partitioned_0 PARTITION OF hash_partitioned
    FOR VALUES WITH (MODULUS 4, REMAINDER 0);

CREATE TABLE hash_partitioned_1 PARTITION OF hash_partitioned
    FOR VALUES WITH (MODULUS 4, REMAINDER 1);

CREATE TABLE hash_partitioned_2 PARTITION OF hash_partitioned
    FOR VALUES WITH (MODULUS 4, REMAINDER 2);

CREATE TABLE hash_partitioned_3 PARTITION OF hash_partitioned
    FOR VALUES WITH (MODULUS 4, REMAINDER 3);

INSERT INTO hash_partitioned (id, name) VALUES (15, 'John'); -- id(15) % 4 => hash_partitioned_3
```
- `MODULUS`: 전체 파티션 개수
- `REMAINDER`: 현재 파티션이 담당할 나머지 값

---

## Materialized View
`Materialized View`는 일반적인 `View`와 달리 쿼리 결과를 실제 디스크에 저장해두는 객체입니다. 복잡하고 비용이 큰 쿼리 결과를 미리 계산해서 저장해 두었다가, 이후 동일한 요청이 들어오면 저장된 결과를 빠르게 반환합니다.

```sql
CREATE MATERIALIZED VIEW mv_salary_summary AS
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

`Materialized View`는 기본적으로 정적이므로, 원본 테이블의 데이터가 바뀌더라도 자동으로 갱신되지 않습니다. 최신 데이터를 반영하려면 `REFRESH` 명령어를 사용해야 합니다.

```sql
REFRESH MATERIALIZED VIEW mv_salary_summary;
```

| 특성 | View	| Materialized View |
|-|-|-|
| **저장 방식**	| 쿼리 정의만 저장 | 쿼리 결과를 저장 |
| **실시간성** | 항상 최신 데이터 조회 | `REFRESH` 시점의 데이터만 유지 |
| **조회 속도**	| 느릴 수 있음 | 빠름 (미리 계산된 결과 조회) |
| **저장공간 필요 여부** | 필요 없음 | 필요함 |
| **쓰기 가능 여부** | 일반적으로 불가 | 직접 쓰기 불가 (`REFRESH`만 가능) |

---

## Execution Plan

- `Seq Scan`: 테이블을 처음부터 끝까지 순차적으로 읽음. 인덱스가 없거나 조건에 맞는 행이 많을 때 사용됨.
- `Index Scan`: 인덱스를 통해 원하는 행만 찾아 힙(테이블)에서 읽음. 특정 값 조회 시 효율적.
- `Index Only Scan`: 인덱스 내에 필요한 모든 컬럼 데이터가 있어 힙 접근 없이 인덱스만으로 결과 반환 가능.
- `Bitmap Index Scan`: 여러 조건에 맞는 행 후보를 비트맵으로 만들어 효율적인 후속 힙 조회 준비.
- `Bitmap Heap Scan`: 비트맵을 사용해 실제 힙에서 데이터를 읽음. 복합 조건이나 대량 조회 시 효과적.

### EXPLAIN
`EXPLAIN`는 쿼리를 실제 실행하지 않고, 쿼리를 어떻게 수행할지에 대한 실행 계획 을 보여주는 명령어입니다. 쿼리가 어떤 인덱스를 사용하는지, 테이블은 어떻게 읽는지, 조인은 어떤 방식으로 하는지 등 상세한 처리 방식을 미리 분석할 수 있습니다.

```sql
EXPLAIN SELECT * FROM employees WHERE id = 1;
```

```sql
 Index Scan using employees_pkey on employees  (cost=0.29..8.30 rows=1 width=30)
   Index Cond: (id = 123)
```

### EXPLAIN ANALYZE
`EXPLAIN ANALYZE`는 `EXPLAIN`과 다르게 쿼리를 실제 실행한 뒤, 실행 계획과 함께 각 단계별 실제 실행 시간, 실제 반환된 행 수, 반복 실행 횟수 등을 상세히 보여줍니다. 실제 실행 결과를 토대로 쿼리 최적화 방향을 잡기에 가장 정확한 도구입니다.

```sql
EXPLAIN ANALYZE SELECT * FROM employees WHERE name = 'John';
```

```sql
 Seq Scan on employees  (cost=0.00..204.00 rows=2 width=30) (actual time=0.473..0.473 rows=0 loops=1)
   Filter: (name = 'John'::text)
   Rows Removed by Filter: 10000
 Planning Time: 0.062 ms
 Execution Time: 0.482 ms
```

---

## References
- [PostgreSQL 공식 문서](https://www.postgresql.org/docs/current/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
