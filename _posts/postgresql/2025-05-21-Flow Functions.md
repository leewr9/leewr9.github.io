---
title: Flow Functions
category: PostgreSQL
tag: [Trigger, Procedure, Database, SQL, PostgreSQL]
---

> PostgreSQL은 단순한 RDBMS를 넘어, 데이터의 흐름과 동작을 스스로 제어할 수 있는 강력한 기능을 제공합니다. 이 기능들은 주로 데이터 무결성 유지, 비즈니스 로직 자동화, 반복 작업 단순화 등에 활용되며, 기존 애플리케이션 레이어에서 처리하던 로직을 데이터베이스 내부로 옮김으로써 더 높은 일관성과 성능, 그리고 유지보수성을 얻을 수 있다는 점에서 매우 유용합니다

---

## Function
`Function`은 입력값을 받아 계산 후 값을 반환하는 함수입니다. 주로 `SELECT` 구문 안에서 사용되며, 데이터 처리, 포맷팅, 계산 등에 활용됩니다. `RETURNS`를 통해 반환 타입을 지정하고, `RETURN` 구문으로 값을 반환합니다.

```sql
CREATE OR REPLACE FUNCTION add_numbers(a INTEGER, b INTEGER)
RETURNS INTEGER AS $$
BEGIN
    RETURN a + b;
END;
$$ LANGUAGE plpgsql;

SELECT add_numbers(10, 20);
```

```bash
 add_numbers
-------------
          30
(1 rows)
```

---

## Procedure
`Procedure`는 값을 반환하지 않고 여러 SQL 작업을 수행하는 데 사용됩니다. 트랜잭션 단위의 일괄 작업 처리나 로깅 등에 활용되며, `CALL` 구문으로 실행합니다.

```sql
CREATE OR REPLACE PROCEDURE insert_log(p_message TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO action_logs(msg) VALUES (p_message);
END;
$$;

CALL insert_log('Call Procedure');  
SELECT * FROM action_logs;
```

```sql
      msg
----------------
 Call Procedure
(1 rows)
```

---

## Trigger
`Trigger`는 테이블에 `INSERT`, `UPDATE`, `DELETE` 같은 이벤트가 발생했을 때 자동으로 실행되는 동작입니다. 트리거 자체는 시점과 이벤트를 지정하고, 실행할 트리거 함수를 연결합니다. 트리거 함수는 트리거가 실행할 실제 로직을 담은 함수로, `RETURNS TRIGGER`를 반드시 포함해야 합니다. `NEW`, `OLD` 객체를 통해 삽입/수정된 행 데이터에 접근할 수 있습니다.

### INSERT

```sql
CREATE OR REPLACE FUNCTION user_insert()  -- 트리거 함수 생성
RETURNS TRIGGER AS $$
BEGIN
    NEW.name := upper(NEW.name);  -- 대문자로 변경
    INSERT INTO user_insert(name, action)
    VALUES (NEW.name, TG_OP);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_user_insert  -- 트리거 생성
BEFORE INSERT ON users  -- INSERT가 실행되기 전에 실행
FOR EACH ROW  -- 행마다 트리거 함수 실행
EXECUTE FUNCTION user_insert();

INSERT INTO users(name) VALUES ('John'), ('Alice'), ('Bob');
SELECT * FROM users;
SELECT * FROM user_insert;
```

```bash
 id | name
----+-------
  1 | JOHN
  2 | ALICE
  3 | BOB
(3 rows)

 id | name  | action |          log_time
----+-------+--------+----------------------------
  1 | JOHN  | INSERT | 2025-05-21 12:05:22.518282
  2 | ALICE | INSERT | 2025-05-21 12:05:22.518282
  3 | BOB   | INSERT | 2025-05-21 12:05:22.518282
(3 rows)
```

### DELETE 

```sql
CREATE OR REPLACE FUNCTION user_delete()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO user_delete(name, action)
    VALUES (OLD.name, TG_OP);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_user_delete
AFTER DELETE ON users
FOR EACH ROW
EXECUTE FUNCTION user_delete();


DELETE FROM users WHERE name = 'JOHN';
SELECT * FROM users;
SELECT * FROM user_delete;
```

```bash
 id | name
----+-------
  2 | ALICE
  3 | BOB
(2 rows)

 id | name | action |          log_time
----+------+--------+----------------------------
  1 | JOHN | DELETE | 2025-05-21 12:10:17.063359
(1 rows)
```

### UPDATE 

```sql
CREATE OR REPLACE FUNCTION user_update()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO user_update(before, after, action)
    VALUES (OLD.name, NEW.name, TG_OP);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_user_update
AFTER UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION user_update();

UPDATE users SET name = 'Charlie' WHERE name = 'Alice';
SELECT * FROM users;
SELECT * FROM user_update;
```

```bash
 id | name
----+-------
  2 | Charlie
  3 | BOB
(2 rows)
  
 id | before  | after | action |          log_time
----+---------+-------+--------+----------------------------
  1 | Charlie | ALICE | UPDATE | 2025-05-21 12:11:07.846997
(1 rows)
```

### FOR EACH
`FOR EACH`는 트리거가 어떤 단위로 실행될지를 지정하는 옵션입니다. 트리거 함수가 실행되는 횟수와 `NEW`, `OLD` 객체 사용 여부에 영향을 줍니다.

- `ROW`: 영향을 받는 각 행마다 트리거가 실행되며, `NEW`, `OLD` 객체 사용 가능
- `STATEMENT`: SQL 문장 전체에 대해 한 번만 실행되며, `NEW`, `OLD` 객체 사용 불가

```sql
CREATE TRIGGER trg_user_statement_insert
AFTER INSERT ON users
FOR EACH STATEMENT
EXECUTE FUNCTION user_insert();

INSERT INTO users(name) VALUES ('David'), ('Eve'), ('Frank');
SELECT * FROM user_insert;
```

```bash
 id | name    | action |          log_time
----+---------+--------+----------------------------
  2 | Charlie | INSERT | 2025-05-21 12:06:49.503228  # trg_user_insert
  3 | BOB     | INSERT | 2025-05-21 12:06:49.503228  # trg_user_insert
  4 | DAVID   | INSERT | 2025-05-21 12:18:37.375523  # trg_user_insert
  5 | EVE     | INSERT | 2025-05-21 12:18:37.375523  # trg_user_insert
  6 | FRANK   | INSERT | 2025-05-21 12:18:37.375523  # trg_user_insert
  7 |         | INSERT | 2025-05-21 12:18:37.375523  # trg_user_statement_insert
(6 rows)
```

---

## References
- [PostgreSQL 공식 문서](https://www.postgresql.org/docs/current/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
