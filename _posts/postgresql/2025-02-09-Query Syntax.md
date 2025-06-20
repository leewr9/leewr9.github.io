---
title: Query Syntax
category: PostgreSQL
tag: [Syntax, Database, SQL, PostgreSQL]
---

> PostgreSQL는 객체 지향적 특징을 결합한 관계형 데이터베이스 관리 시스템으로, 데이터를 효율적으로 저장하고 처리하기 위해 표준 SQL 문법을 기반으로 합니다. 구조화된 쿼리를 통해 데이터 조회, 삽입, 수정, 삭제 등의 작업을 수행할 수 있으며, 복잡한 트랜잭션 처리와 고급 분석 기능도 지원합니다.

---

## SELECT
`SELECT` 문은 데이터베이스에서 데이터를 조회할 때 사용됩니다.
데이터베이스 테이블의 특정 컬럼이나 전체 데이터를 조회할 수 있습니다.

```sql
SELECT column1, column2
FROM table_name;
```
- `column1`, `column2`는 조회할 컬럼을 지정합니다.
- `table_name`은 데이터를 조회할 테이블의 이름입니다.

```sql
SELECT * FROM table_name;
```
`*`는 모든 컬럼을 조회할 때 사용합니다.

---

## INSERT 
`INSERT` 문은 테이블에 새로운 데이터를 추가할 때 사용합니다.

```sql
INSERT INTO table_name (column1, column2)
VALUES (value1, value2);
```
- `table_name`: 데이터를 삽입할 테이블 이름.
- `column1`, `column2`: 삽입할 데이터의 컬럼.
- `value1`, `value2`: 삽입할 값들.

```sql
INSERT INTO employees 
VALUES (1, 'John', 'Doe', 'johndoe@example.com');
```
- `VALUES` 절에 모든 컬럼에 대해 삽입할 값을 나열할 수 있습니다.

---

## UPDATE
`UPDATE` 문은 기존의 데이터를 수정할 때 사용됩니다.

```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```
- `SET` 절을 사용하여 수정할 컬럼과 값을 지정합니다.
- `WHERE` 절을 사용하여 수정할 조건을 지정합니다.

---

## DELETE 
`DELETE` 문은 테이블에서 특정 데이터를 삭제할 때 사용됩니다.

```sql
DELETE FROM table_name
WHERE condition;
```
- `WHERE` 절을 사용하여 삭제할 조건을 지정합니다. 이 조건이 없으면 모든 데이터가 삭제됩니다.

---

## WHERE
`WHERE` 절은 쿼리에서 특정 조건에 맞는 데이터를 필터링하는 데 사용됩니다.

```sql
SELECT customer_id, first_name, last_name
FROM customers
WHERE age >= 30;
```

```sql
 customer_id | first_name | last_name | age 
-------------+------------+-----------+-----
           2 | Jane       | Smith     |  34
           3 | Alice      | Johnson   |  45
           4 | Bob        | Brown     |  32
(3 rows)
```

---

## ORDER BY
`ORDER BY` 절은 결과 데이터를 `오름차순(ASC)` 또는 `내림차순(DESC)`으로 정렬할 때 사용됩니다.

```sql
SELECT customer_id, first_name, last_name, age
FROM customers
ORDER BY age ASC;
```

```sql
 customer_id | first_name | last_name | age 
-------------+------------+-----------+-----
           5 | Charlie    | Davis     |  26
           1 | John       | Doe       |  28
           4 | Bob        | Brown     |  32
           2 | Jane       | Smith     |  34
           3 | Alice      | Johnson   |  45
(5 rows)
```

```sql
SELECT customer_id, first_name, last_name
FROM customers
ORDER BY first_name DESC;
```

```sql
 customer_id | first_name | last_name | age 
-------------+------------+-----------+-----
           3 | Alice      | Johnson   |  45
           2 | Jane       | Smith     |  34
           4 | Bob        | Brown     |  32
           1 | John       | Doe       |  28
           5 | Charlie    | Davis     |  26
(5 rows)
```

---

## GROUP BY 
`GROUP BY` 절은 데이터를 그룹으로 묶어서 `SUM`, `AVG`, `COUNT` 등과 함께 사용할 때 사용됩니다.

```sql
SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city;
```

```sql
     city      | customer_count 
---------------+----------------
 New York      |             12
 Los Angeles   |              8
 Chicago       |              6
 Miami         |              4
 Houston       |              3
(5 rows)
```

### HAVING
`HAVING` 절은 `GROUP BY`로 그룹화된 데이터를 필터링하는 데 사용됩니다. `WHERE` 절은 개별 행을 필터링하는 데 사용되고, `HAVING`은 그룹화된 데이터를 필터링합니다.

```sql
SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city
HAVING COUNT(*) >= 5;
```

```sql
     city      | customer_count 
---------------+----------------
 New York      |             12
 Los Angeles   |              8
 Chicago       |              6
(3 rows)
```

---

## CASE WHEN
`CASE WHEN` 구문은 SQL에서 조건문을 처리할 때 사용되는 일반적인 제어 흐름 구문입니다. 주로 조건에 따라 다른 값을 반환하도록 하는 데 사용됩니다.

```sql
SELECT 
    customer_id,
    total_sales,
    CASE
        WHEN total_sales > 1000 THEN 'High'
        WHEN total_sales BETWEEN 500 AND 1000 THEN 'Medium'
        ELSE 'Low'
    END AS sales_category
FROM sales;
```

```sql
 customer_id | total_sales | sales_category
-------------+-------------+---------------
           1 |        1100 | High
           2 |         900 | Medium
           3 |         100 | Low
(3 rows)
```

---

## DISTINCT
`DISTINCT`와 `DISTINCT ON`은 SQL에서 중복된 행을 제거할 때 사용하는 구문입니다. `DISTINCT`는 전체 행이 동일한 경우 중복을 제거하고, `DISTINCT ON`은 특정 컬럼 기준으로 중복을 제거합니다.

```sql
 customer_id | total_sales | sales_category
-------------+-------------+---------------
           1 |        1100 | High
           1 |        1100 | High
           1 |         100 | Low
           2 |        1100 | Low
           2 |         900 | Medium
           2 |        1100 | Low
           3 |         900 | Medium
           3 |         900 | Medium
           3 |         100 | Low
(7 rows)
```

```sql
SELECT DISTINCT customer_id, total_sales
FROM sales;

SELECT DISTINCT ON (customer_id) customer_id, total_sales
FROM sales
ORDER BY customer_id, total_sales DESC;
```

```sql
 customer_id | total_sales | sales_category
-------------+-------------+---------------
           1 |        1100 | High
           1 |         100 | Low
           2 |        1100 | Low
           2 |         900 | Medium
           3 |         900 | Medium
           3 |         100 | Low
(6 rows)

 customer_id | total_sales | sales_category
-------------+-------------+---------------
           1 |        1100 | High
           2 |        1100 | Low
           3 |         900 | Medium
(3 rows)
```

---

## References
- [PostgreSQL 공식 문서](https://www.postgresql.org/docs/current/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
