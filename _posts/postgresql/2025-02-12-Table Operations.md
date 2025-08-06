---
title: Table Operations
category: PostgreSQL
tag: [Table, Database, SQL, PostgreSQL]
---

> PostgreSQL에서는 데이터를 효율적으로 처리하기 위해 테이블 형태의 구조를 생성하거나 결합하여 관리하는 방법이 중요합니다. 이 작업은 데이터 분석이나 보고서 작성 시 여러 테이블에 분산된 정보를 통합하고, 더 풍부하고 유용한 데이터를 제공하는 데 중요합니다.

---

## JOIN

`JOIN`은 여러 테이블을 결합하여 데이터를 조회하는 데 사용됩니다. SQL에서 테이블을 결합하는 방법에는 여러 가지가 있으며, 각 `JOIN`은 서로 다른 방식으로 데이터를 결합합니다.

### INNER JOIN

`INNER JOIN`은 두 테이블에서 일치하는 행만 반환합니다. 즉, 두 테이블에서 매칭되는 값이 있을 때만 그 값을 반환하고, 매칭되지 않으면 결과에 포함되지 않습니다.

```sql
SELECT customers.customer_id, customers.first_name, orders.order_id
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id;
```

```sql
 customer_id | first_name | order_id
-------------+------------+----------
           1 | John       |      1001
           1 | John       |      1002
           2 | Alice      |      1003
           3 | Bob        |      1004
(4 rows)
```

### LEFT JOIN

`LEFT OUTER JOIN`은 왼쪽 테이블의 모든 행을 반환하고, 오른쪽 테이블과 매칭되는 데이터가 있으면 그 데이터를 포함합니다. 만약 매칭되는 데이터가 없으면, 오른쪽 테이블의 값은 `NULL`로 반환됩니다.

```sql
SELECT customers.customer_id, customers.first_name, orders.order_id
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;
```

```sql
 customer_id | first_name | order_id
-------------+------------+----------
           1 | John       |      1001
           1 | John       |      1002
           2 | Alice      |      1003
           3 | Bob        |      1004
           4 | Charlie    |      NULL
(5 rows)
```

### RIGHT JOIN

`RIGHT OUTER JOIN`은 오른쪽 테이블의 모든 행을 반환하고, 왼쪽 테이블과 매칭되는 데이터를 포함합니다. 만약 왼쪽 테이블에 매칭되는 데이터가 없으면, 왼쪽 테이블의 값은 `NULL`로 반환됩니다.

```sql
SELECT customers.customer_id, customers.first_name, orders.order_id
FROM customers
RIGHT JOIN orders ON customers.customer_id = orders.customer_id;
```

```sql
 customer_id | first_name | order_id
-------------+------------+----------
           1 | John       |      1001
           1 | John       |      1002
           2 | Alice      |      1003
           3 | Bob        |      1004
        NULL | NULL       |      1005
(5 rows)
```

### FULL JOIN

`FULL OUTER JOIN`은 두 테이블의 모든 행을 반환하며, 일치하는 행은 결합하고, 일치하지 않는 행은 `NULL`로 채웁니다. 즉, 왼쪽 테이블과 오른쪽 테이블에서 매칭되는 값이 있으면 결합하고, 없으면 `NULL`을 반환합니다.

```sql
SELECT customers.customer_id, customers.first_name, orders.order_id
FROM customers
FULL JOIN orders ON customers.customer_id = orders.customer_id;
```

```sql
 customer_id | first_name | order_id
-------------+------------+----------
           1 | John       |      1001
           1 | John       |      1002
           2 | Alice      |      1003
           3 | Bob        |      1004
           4 | Charlie    |      NULL
        NULL | NULL       |      1005
(6 rows)
```

---

## CTE

`CTE (Common Table Expression)`는 쿼리에서 임시 테이블 역할을 하는 SQL 기능입니다.
쿼리 실행 중에만 존재하며, 데이터베이스에 저장되지 않습니다. 복잡한 서브쿼리를 간단히 작성하거나, 재귀 쿼리를 처리할 때 유용합니다.

```sql
WITH CustomerSales AS (
    SELECT customer_id, SUM(amount) AS total_sales
    FROM sales
    GROUP BY customer_id
)

SELECT * FROM CustomerSales
WHERE total_sales > 1000;
```

```sql
 customer_id | total_sales
-------------+-------------
           1 |         1500
           2 |         1200
(2 rows)
```

---

## CTAS

`CTAS (Create Table As Select)`는 데이터를 복사하거나 변환하여 새로운 영구 테이블을 생성하는 SQL 명령문입니다.
쿼리 결과를 기반으로 데이터를 영구적으로 저장하므로, 데이터 마이그레이션이나 데이터 변환 작업에 적합합니다.

```sql
CREATE TABLE HighValueCustomers AS
SELECT customer_id, SUM(amount) AS total_sales
FROM sales
GROUP BY customer_id
HAVING SUM(amount) > 1000;

SELECT * FROM HighValueCustomers;
```

```sql
 customer_id | total_sales
-------------+-------------
           1 |         1500
           2 |         1200
(2 rows)
```

---

## Subquery

서브쿼리는 쿼리 내에서 또 다른 쿼리를 사용하는 방법입니다. 서브쿼리는 보통 `SELECT`, `INSERT`, `UPDATE`, `DELETE`문 안에서 사용됩니다.

```sql
SELECT first_name, last_name
FROM customers
WHERE customer_id = (SELECT customer_id FROM orders WHERE order_id = 1001);
```

```sql
 first_name | last_name
------------+-----------
 John       | Doe
(1 row)
```

---

## References

- [PostgreSQL 공식 문서](https://www.postgresql.org/docs/current/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
