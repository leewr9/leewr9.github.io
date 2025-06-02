---
title: Query Syntax
category: MongoDB
tag: [Database, NoSQL, MongoDB]
---

> MongoDB는 유연한 스키마를 갖춘 문서 지향 데이터베이스로, 데이터를 JSON과 유사한 BSON 형식으로 저장합니다. 구조화된 SQL 대신 직관적인 쿼리 문법을 제공하며, 컬렉션 단위로 데이터를 관리합니다. 복잡한 조인이나 트랜잭션 없이도 빠르게 데이터를 저장하고 조회할 수 있어, 빠른 개발과 확장이 필요한 현대 웹 애플리케이션에 적합합니다. 

---

## find()
`find()`는 MongoDB에서 문서를 조회할 때 사용하는 기본 메서드입니다. 조건 없이 전체 문서를 조회하거나, 특정 조건을 추가하여 원하는 데이터를 필터링할 수 있습니다. 두 번째 인자로 조회할 필드만 선택할 수도 있습니다.

```javascript
db.users.find(); // 전체 users 컬렉션 조회
db.users.find(
  { age: { $gte: 20 } }, 
  { name: 1, age: 1 }
); // age가 20 이상인 문서 중에서 name과 age 필드만 조회
```

- **Operators**
  - `$eq`: 값이 같은 문서 검색 (equal)
  - `$ne`: 값이 같지 않은 문서 검색 (not equal)
  - `$gt`: 값이 크다 (greater than)
  - `$gte`: 값이 크거나 같다 (greater than or equal)
  - `$lt`: 값이 작다 (less than)
  - `$lte`: 값이 작거나 같다 (less than or equal)
  - `$in`: 값이 지정한 배열 내에 포함된 문서 검색
  - `$nin`: 값이 지정한 배열 내에 포함되지 않은 문서 검색
  - `$and`: 여러 조건을 모두 만족하는 문서 검색 (논리 AND)
  - `$or`: 여러 조건 중 하나 이상 만족하는 문서 검색 (논리 OR)
  - `$not`: 조건에 부합하지 않는 문서 검색 (논리 NOT)
  - `$exists`: 특정 필드의 존재 여부 확인 (true/false)
  - `$type`: 필드의 자료형으로 필터링
  - `$size`: 배열 필드의 크기가 특정 값인 문서 검색
  - `$all`: 배열 필드가 특정 모든 값들을 포함하는지 확인
  - `$elemMatch`: 배열 내 요소가 특정 조건을 만족하는 문서 검색
  - `$regex`: 필드 값이 정규식 패턴과 매칭되는 문서 검색
  - `$expr`: MongoDB 표현식을 사용해 필드 간 비교 및 복잡한 조건 적용
  - `$geoWithin`: 지리공간 쿼리로, 특정 영역 내에 위치하는 문서 검색
  - `$geoIntersects`: 지정한 지리공간과 교차하는 문서 검색
  - `$mod`: 필드 값이 특정 수로 나누었을 때 나머지가 특정 값인 문서 검색


### sort()
`sort()`는 MongoDB에서 조회한 결과를 정렬할 때 사용합니다. 1은 오름차순 정렬, -1은 내림차순 정렬을 의미하며, 여러 필드 기준 정렬도 가능합니다.

```javascript
db.users.find().sort({ age: -1 });  // age 기준 내림차순 정렬
```

### limit()
`limit()`는 MongoDB에서 조회 결과로 반환할 문서 수를 제한할 때 사용합니다. 데이터가 매우 많을 경우 필요한 개수만 조회하여 성능 최적화에 도움이 됩니다.

```javascript
db.users.find().limit(5);  // 5개 문서만 조회
```

### skip()
`skip()`은 조회 결과에서 지정한 수만큼 문서를 건너뛰고 이후 문서부터 반환할 때 사용합니다. 페이지네이션 기능 구현에 자주 활용됩니다.

```javascript
db.users.find().skip(10);  // 앞의 10개 건너뛰고 조회
```

---

## insert()
`insert()`는 MongoDB에서 새 문서를 컬렉션에 삽입할 때 사용합니다. 단일 문서 삽입은 `insertOne()`, 여러 문서 삽입은 `insertMany()`를 사용하며, 삽입 성공 여부와 삽입된 문서 정보를 반환합니다.

```javascript
db.collection.insertOne({ name: 'Alice', age: 25 });
db.collection.insertMany([
  { name: 'Bob', age: 30 },
  { name: 'Carol', age: 22 }
]);
```

---

## update()
`update()`는 기존 문서의 데이터를 변경할 때 사용합니다. 한 개 문서 수정은 `updateOne()`, 여러 문서 수정은 `updateMany()`를 사용하며, `$set` 연산자로 변경할 필드를 지정해 원하는 데이터만 갱신할 수 있습니다.

```javascript
db.collection.updateOne(
  { name: 'Alice' },
  { $set: { age: 26 } }
); // name이 Alice인 문서의 age를 26으로 수정
```

---

## delete() 
`delete()`는 조건에 맞는 문서를 삭제할 때 사용합니다. 한 개 문서 삭제는 `deleteOne()`, 여러 문서 삭제는 `deleteMany()`를 사용하며, 삭제 성공 여부와 삭제된 문서 개수를 반환합니다.

```javascript
db.collection.deleteOne({ name: 'Bob' }); // name이 Bob인 문서 삭제
db.collection.deleteMany({ status: 'inactive' }); // status가 inactive인 모든 문서 삭제
```

---

## distinct()
`distinct()`는 특정 필드에서 중복되지 않는 고유한 값들만 추출할 때 사용합니다. 컬렉션 내에서 해당 필드가 가지는 모든 고유 값 목록을 빠르게 조회할 수 있어 분석이나 필터링 시 유용합니다.

```javascript
db.users.distinct('country');
```

```javascript
[ 'Canada', 'Germany', 'UK', 'USA' ]
```

---

## countDocuments()
`countDocuments()`는 지정한 조건에 맞는 문서 개수를 정확히 셀 때 사용합니다. 조건을 생략하면 컬렉션 내 전체 문서 수를 반환하며, 필터링 후 남은 문서 개수 확인에 적합합니다.

```javascript
db.users.countDocuments(); // 전체 users 컬렉션 문서 개수 조회
db.users.countDocuments({ age: { $gte: 25 } }); // age가 25 이상인 users 문서 개수 조회
```

---

## References
- [MongoDB 공식 문서](https://www.mongodb.com/docs/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
