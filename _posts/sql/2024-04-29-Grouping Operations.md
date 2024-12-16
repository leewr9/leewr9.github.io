---
title: Grouping Operations
category: SQL
tag: [SQL]
---

> SQL에서는 데이터베이스의 작업을 하나의 논리적 단위로 묶어 실행 가능합니다. 여러 개의 SQL 명령을 하나로 묶어 실행하면서, 반복적으로 사용할 수 있는 작업을 정의하고 실행하는 기능으로, 데이터베이스에서 복잡한 작업을 처리하는 데 유용합니다.

---

## Transaction
트랜잭션은 `ACID(Atomicity, Consistency, Isolation, Durability)` 속성을 보장하는 데 중요한 역할을 하며, 데이터베이스의 무결성을 유지하고 오류 발생 시 데이터의 일관성을 지킬 수 있도록 합니다.

### COMMIT
`COMMIT`은 트랜잭션 내에서 실행된 모든 작업을 영구적으로 데이터베이스에 저장하는 명령어입니다. 트랜잭션이 성공적으로 완료된 후 변경 사항을 확정하고, 데이터베이스에 반영합니다.

```sql
BEGIN; -- 트랜잭션 시작
    UPDATE customers SET balance = balance - 100 WHERE customer_id = 1;
    UPDATE customers SET balance = balance + 100 WHERE customer_id = 2;
COMMIT; -- 트랜잭션 완료, 변경 사항 저장
```

```sql
BEGIN
UPDATE 1
UPDATE 1
COMMIT
```

### ROLLBACK
`ROLLBACK`은 트랜잭션이 완료되지 않고 오류가 발생했을 경우, 또는 의도적으로 변경 사항을 취소하고자 할 때 사용됩니다. 롤백을 실행하면 트랜잭션 내의 모든 변경 사항이 취소되고, 데이터는 트랜잭션이 시작되기 전 상태로 되돌아갑니다.

```sql
BEGIN; -- 트랜잭션 시작
    UPDATE customers SET balance = balance - 100 WHERE customer_id = 1;
    UPDATE customers SET balance = balance + 100 WHERE customer_id = 2;
    UPDATE customers SET balance = balance / 0 WHERE customer_id = 3; -- 오류 발생
ROLLBACK; -- 오류 발생 시 모든 변경 사항 취소
```

```sql
BEGIN
UPDATE 1
UPDATE 1
ERROR:  division by zero
ROLLBACK
```

---

## PROCEDURE
프로시저는 데이터베이스 내에서 일련의 SQL 명령을 수행하는 프로그램 블록입니다. 프로시저는 매개변수를 받을 수 있으며, 여러 SQL 명령을 포함하여 복잡한 작업을 처리할 수 있습니다. 저장 프로시저는 `CALL` 명령어로 실행됩니다.

예시:

```sql
CREATE OR REPLACE PROCEDURE transfer_funds(from_id INT, to_id INT, amount DECIMAL) -- 매개변수
AS $$
BEGIN
    UPDATE customers SET balance = balance - amount WHERE customer_id = from_id;
    UPDATE customers SET balance = balance + amount WHERE customer_id = to_id;
    COMMIT;
END;
$$ LANGUAGE plpgsql;
```

```sql
CALL transfer_funds(1, 2, 100); --  -- 고객 1에서 고객 2로 100 이체
```

---

## FUNCTION 
함수는 특정 작업을 처리하고 결과를 반환하는 SQL 코드 블록입니다. 함수는 값을 반환하는 것이 특징이며, `SELECT` 문이나 다른 SQL 명령에서 호출될 수 있습니다. 함수는 변수를 지정하거나 하나 이상의 매개변수를 받으며, 값을 반환합니다.

```sql
CREATE OR REPLACE FUNCTION get_balance(customer_id INT) -- 매개변수
RETURNS DECIMAL -- 반환 값
AS $$
DECLARE
    current_balance DECIMAL; -- 변수 지정
BEGIN
    SELECT balance INTO current_balance FROM customers WHERE customer_id = customer_id;
    RETURN current_balance;
END;
$$ LANGUAGE plpgsql;
```

```sql
SELECT get_balance(1); -- 고객 1의 잔액 조회

 get_balance 
--------------
        500.00
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
