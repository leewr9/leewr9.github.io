---
title: Format Handling
category: PostgreSQL
tag: [Database, SQL, PostgreSQL]
---

> PostgreSQL에서 형변환 함수와 날짜/시간 함수는 데이터 타입을 변환하거나 날짜 및 시간 값을 추출하고 조작하는 데 중요한 역할을 합니다. 이를 통해 다양한 형식으로 데이터를 처리하고 날짜와 시간을 필요한 방식으로 변환할 수 있습니다.

---

## Type Conversion
형변환 함수는 SQL에서 한 데이터 타입을 다른 데이터 타입으로 변환하는 데 사용됩니다. 주로 데이터 간의 호환성을 맞추거나 출력 형식을 변경할 때 사용됩니다.

### TO_CHAR()
`TO_CHAR()` 함수는 숫자나 날짜 데이터를 지정된 형식으로 문자열로 변환합니다. 주로 날짜나 숫자를 특정 형식으로 표시할 때 사용됩니다.

```sql
SELECT TO_CHAR('2024-04-30'::DATE, 'YYYY-MM-DD'); -- 날짜를 문자열 형식으로 변환
```

### TO_TIMESTAMP()
`TO_TIMESTAMP()` 함수는 문자열로 입력된 날짜와 시간을 지정된 형식에 맞게 `TIMESTAMP` 타입으로 변환합니다.

```sql
SELECT TO_TIMESTAMP('2024-04-30 15:30:00', 'YYYY-MM-DD HH24:MI:SS'); -- 문자열을 날짜 형식으로 변환
```

### CAST()
`CAST()` 함수는 한 데이터 타입을 다른 타입으로 변환하는 데 사용됩니다. `TO_CHAR()`와 유사하지만, `CAST()`는 주로 SQL 표준에 따라 타입을 변환합니다. `::` 연산자로도 사용 가능합니다.

```sql
SELECT CAST('123' AS INTEGER); -- 문자열을 정수로 변환
SELECT '123'::INTEGER; -- 문자열을 정수로 변환
```

---

## Date and Time
날짜 및 시간 함수는 날짜나 시간을 계산하고 추출하는 데 사용됩니다. 주로 날짜 차이 계산, 날짜 형식 변환, 현재 시간 및 날짜 조회 등에 사용됩니다.

### CURRENT_DATE
`CURRENT_DATE`는 현재 날짜만 반환합니다. 시간은 제외하고 날짜만 필요할 때 사용됩니다.

```sql
SELECT CURRENT_DATE; -- 현재 날짜만 반환

-- 2024-04-30
```

### NOW()
`NOW()` 함수는 현재 날짜와 시간을 반환합니다. 일반적으로 현재 시간을 기준으로 데이터를 처리하거나 기록할 때 사용됩니다.

```sql
SELECT NOW(); -- 현재 날짜와 시간 반환

-- 2024-04-30 15:30:00
```

### EXTRACT()
`EXTRACT()` 함수는 날짜에서 특정 부분을 추출하는 데 사용됩니다. 예를 들어, 년, 월, 일 등을 추출할 수 있습니다.

```sql
SELECT EXTRACT(YEAR FROM '2024-04-30'::DATE); -- 연도 추출

-- 2024
```

### DATE_TRUNC()
`DATE_TRUNC()`는 주어진 날짜 값을 원하는 단위(예: 연도, 월, 일 등)로 자르는 데 사용됩니다.

사용 예시:
```sql
SELECT DATE_TRUNC('year', '2024-04-30'::DATE); -- 연도 단위로 자르기
SELECT DATE_TRUNC('month', '2024-04-30'::DATE); -- 월 단위로 자르기

-- 2024-01-01 00:00:00
-- 2024-04-01 00:00:00
```

---

## References
- [PostgreSQL 공식 문서](https://www.postgresql.org/docs/current/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
