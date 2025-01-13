---
title: Window Functions
category: PostgreSQL
tag: [Database, SQL, PostgreSQL]
---

> 윈도우 함수는 PostgreSQL에서 그룹화된 데이터를 처리할 때 각 행에 대해 계산을 수행할 수 있게 해주는 강력한 도구입니다. 이를 통해 데이터의 흐름을 추적하거나 집계 작업을 효율적으로 수행할 수 있습니다.

---

## OVER
`OVER` 절은 윈도우 함수와 함께 사용되어 특정 범위 내에서 계산을 수행하도록 합니다. 데이터 집합 내에서 특정 조건을 기준으로 데이터를 그룹화하고, 그 그룹 내에서 계산을 할 수 있습니다.

```sql
SELECT customer_id, total_spent,
       SUM(total_spent) OVER (PARTITION BY region ORDER BY sale_date) AS regional_total
FROM sales;
```

```sql
 customer_id | total_spent | regional_total 
-------------+-------------+----------------
           1 |         100 |           300 
           2 |         200 |           500
           3 |         150 |           650
           4 |         300 |           950
           5 |         250 |          1200 
(5 rows)
```
`PARTITION BY`는 특정 범위(`region` 기준) 내에서 값을 집계하며, `ORDER BY`는 순서대로 정렬하여 집계합니다.

---

## Ranking 
`RANK`와 `ROW_NUMBER`는 데이터 집합 내에서 각 행에 대해 순위를 부여하거나 순서를 지정하는 데 사용됩니다. 이를 통해 데이터를 순차적으로 정렬하고, 특정 기준에 따라 순위나 번호를 매기는 작업을 할 수 있습니다.

### RANK
`RANK`는 데이터를 순위별로 정렬할 때 사용되는 함수입니다. 같은 순위의 값이 있으면 그 다음 순위를 건너뛰고 숫자를 매깁니다. 

```sql
SELECT customer_id, total_spent,
       RANK() OVER (ORDER BY total_spent DESC) AS rank
FROM sales;
```

```sql
 customer_id | total_spent | rank 
-------------+-------------+------
           4 |         300 |    1
           2 |         250 |    2
           5 |         250 |    2
           3 |         150 |    3
           1 |         100 |    4
(5 rows)
```

### ROW_NUMBER
``ROW_NUMBER``는 데이터에 대해 고유한 순서를 부여합니다. 순위가 같더라도 각 행에는 고유한 번호가 할당됩니다.

```sql
SELECT customer_id, total_spent,
       ROW_NUMBER() OVER (ORDER BY total_spent DESC) AS row_number
FROM sales;
```

```sql
 customer_id | total_spent | row_number 
-------------+-------------+------
           4 |         300 |    1
           2 |         250 |    2
           5 |         250 |    3
           3 |         150 |    4
           1 |         100 |    5
(5 rows)
```

---

## Aggregation
`FIRST_VALUE`/`LAST_VALUE`와 `LAG`/`LEAD` 함수는 데이터 집합에서 값을 집계하거나 요약하는 데 사용됩니다. 주로 데이터를 그룹화하고, 그룹 내에서 총합, 평균, 최댓값, 최솟값 등을 계산하는 데 쓰입니다.

### FIRST_VALUE
`FIRST_VALUE`는 지정된 순서에서 첫 번째 값을 반환합니다.

```sql
SELECT customer_id, total_spent,
       FIRST_VALUE(total_spent) OVER (ORDER BY sale_date) AS first_spent
FROM sales;
```

```sql
 customer_id | sale_date  | total_spent | first_spent 
-------------+------------+-------------+-------------
           1 | 2024-01-01 |         100 |         100
           2 | 2024-01-02 |         200 |         100
           3 | 2024-01-03 |         150 |         100
           4 | 2024-01-04 |         300 |         100
           5 | 2024-01-05 |         250 |         100
(5 rows)
```

### LAST_VALUE
`LAST_VALUE`는 지정된 순서에서 마지막 값을 반환합니다.

```sql
SELECT customer_id, total_spent,
       LAST_VALUE(total_spent) OVER (ORDER BY sale_date 
       ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_spent
FROM sales;
```

```sql
 customer_id | sale_date  | total_spent | last_spent 
-------------+------------+-------------+-------------
           1 | 2024-01-01 |         100 |         250
           2 | 2024-01-02 |         200 |         250
           3 | 2024-01-03 |         150 |         250
           4 | 2024-01-04 |         300 |         250
           5 | 2024-01-05 |         250 |         250
(5 rows)
```

`ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`은 윈도우 함수에서 윈도우 범위를 설정할 때 사용됩니다. 이 범위는 첫 번째 행부터 마지막 행까지의 모든 데이터를 포함합니다.

### LAG
`LAG`는 이전 행의 값을 반환합니다. 

```sql
SELECT customer_id, total_spent,
       LAG(total_spent) OVER (ORDER BY sale_date) AS previous_spent
FROM sales;
```

```sql
 customer_id | total_spent | previous_spent 
-------------+-------------+----------------
           1 |         100 |           NULL
           2 |         200 |            100
           3 |         150 |            200
           4 |         300 |            150
           5 |         250 |            300
(5 rows)
```

### LEAD
`LEAD`는 다음 행의 값을 반환합니다. 

```sql
SELECT customer_id, total_spent,
       LEAD(total_spent) OVER (ORDER BY sale_date) AS next_spent
FROM sales;
```

```sql
 customer_id | total_spent | next_spent 
-------------+-------------+------------
           1 |         100 |        200
           2 |         200 |        150
           3 |         150 |        300
           4 |         300 |        250
           5 |         250 |       NULL
(5 rows)
```

---

## NULL Handling
`NULLIF`와 `COALESCE`는 데이터베이스에서 `NULL` 값을 처리하는 데 사용되는 함수들입니다. `NULL`은 데이터베이스에서 값이 없거나 정의되지 않은 상태를 나타냅니다.

### NULLIF
`NULLIF`는 두 값이 같으면 `NULL`을 반환하고, 다르면 첫 번째 값을 반환합니다.

```sql
SELECT customer_id, discount_price, regular_price,
       NULLIF(discount_price, regular_price) AS price_difference
FROM products;
```

```sql
 customer_id | discount_price | regular_price | price_difference 
-------------+----------------+---------------+------------------
           1 |            100 |          100  |            NULL
           2 |            150 |          250  |             150
           3 |            200 |          200  |            NULL
(3 rows)
```

### COALESCE
`COALESCE`는 첫 번째 `NULL`이 아닌 값을 반환합니다. 여러 값을 인자로 받아, 첫 번째 `NULL`이 아닌 값을 찾아 반환합니다.

```sql
SELECT customer_id, COALESCE(phone_number, 'N/A') AS contact_number
FROM customers;
```

```sql
 customer_id | phone_number | contact_number 
-------------+--------------+----------------
           1 |         NULL |          NULL 
           2 |     010-1234 |      010-1234 
           3 |         NULL |          NULL 
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
