---
title: Aggregate Pipeline
category: MongoDB
tag: [Database, NoSQL, MongoDB]
---

> MongoDB는 데이터를 처리하기 위한 집계 파이프라인 구조를 제공합니다. 각 파이프라인 단계는 입력 문서를 받아 가공한 후 다음 단계로 전달하며, 다양한 연산자를 조합해 복잡한 데이터 집계와 변환이 가능합니다. 이러한 구조는 대량의 데이터를 효율적으로 처리하거나, 다차원적인 리포트를 생성하고자 할 때 강력한 성능을 발휘합니다.

---

## aggregate()
`aggregate()`는 MongoDB에서 데이터를 변형하거나 통계처리할 수 있는 강력한 집계 프레임워크입니다. SQL의 `GROUP BY`, `JOIN`, `HAVING`, `ORDER BY`, `SELECT CASE` 같은 복잡한 쿼리를 MongoDB에서도 처리할 수 있도록 해줍니다.

```javascript
db.collection.aggregate([
  { stage1 },
  { stage2 },
  { stage3 }
]);
```

### Filter 

#### $match
`$match`는 조건에 부합하는 문서만 필터링해 다음 단계로 넘깁니다. 보통 파이프라인 초기에 데이터를 걸러내어 불필요한 연산을 줄일 때 가장 많이 사용합니다.

```javascript
db.users.aggregate([
  { $match: { age: { $gte: 20 } } }
])
```

#### $sort
`$sort`는 특정 필드를 기준으로 문서를 오름차순(1) 또는 내림차순(-1)으로 정렬합니다. 결과 출력 순서를 명확히 제어할 때 사용됩니다.

```javascript
db.users.aggregate([
  { $sort: { age: -1 } }
])
```

#### $limit
`$limit`은 집계 결과에서 상위 N개의 문서만 남겨 반환합니다. 대량 데이터 중 일부만 확인하거나 결과 크기를 제한할 때 유용합니다.

```javascript
db.users.aggregate([
  { $limit: 5 } // 상위 5명만 출력
])
```

#### $skip
`$skip`은 결과에서 지정한 개수만큼 문서를 건너뛰고, 그 다음 문서부터 반환합니다. 보통 페이징 처리 시 주로 활용됩니다.

```javascript
db.users.aggregate([
  { $skip: 10 } // 처음 10개 문서를 건너뛰고 이후 결과 반환
])
```

### Transform

#### $project
`$project`는 출력 문서에서 원하는 필드만 선택하거나 새로 계산한 필드를 추가해 문서 구조를 변경하는 데 사용합니다. 기존 필드를 삭제하거나 변형할 수 있습니다.

```javascript
db.users.aggregate([
  {
    $project: {
      name: 1,
      birthYear: { $subtract: [2025, "$age"] },
      isAdult: { $cond: [{ $gte: ["$age", 18] }, true, false] }
    }
  }
])
```

```javascript
[
  {
    _id: ObjectId('683d195d172a0eb2876c4bd0'),
    name: 'Alice',
    birthYear: 2000,
    isAdult: true
  },
  ...
]
```

#### $addFields
`$addFields`는 기존 문서의 필드를 그대로 유지하면서 새 필드를 추가하거나 기존 필드 값을 덮어써서 확장할 때 쓰입니다.

```javascript
db.users.aggregate([
  {
    $addFields: {
      category: {
        $cond: [{ $gte: ["$age", 60] }, "Senior", "General"]
      }
    }
  }
])
```

```javascript
[
  {
    _id: ObjectId('683d195d172a0eb2876c4bd0'),
    name: 'Alice',
    age: 25,
    country: 'USA',
    active: true,
    location: [ 'New York', 'Boston' ],
    category: 'General'
  },
  {
    _id: ObjectId('683d195d172a0eb2876c4bd9'),
    name: 'Jack',
    age: 60,
    country: 'USA',
    active: false,
    location: [ 'Seattle' ],
    category: 'Senior'
  },
  ...
]
```

#### $set
`$set`은 `$addFields`와 같은 역할을 하며, 문서에 새 필드를 추가하거나 기존 필드 값을 변경하는 데 사용합니다. 둘은 거의 동일합니다.

```javascript
db.users.aggregate([
  {
    $set: {
      continent: {
        $switch: {
          branches: [
            { case: { $in: ["$country", ["USA", "Canada"]] }, then: "America" },
            { case: { $in: ["$country", ["UK", "Germany"]] }, then: "Europe" }
          ],
          default: "Earth"
        }
      }
    }
  }
])
```

```javascript
[
  {
    _id: ObjectId('683d195d172a0eb2876c4bd0'),
    name: 'Alice',
    age: 25,
    country: 'USA',
    active: true,
    location: [ 'New York', 'Boston' ],
    continent: 'America'
  },
  {
    _id: ObjectId('683d195d172a0eb2876c4bd3'),
    name: 'Diana',
    age: 28,
    country: 'UK',
    active: true,
    location: [ 'London' ],
    continent: 'Europe'
  },
  ...
]
```

- `$subtract`: 두 숫자나 날짜의 차이를 계산해 반환
  ```javascript
  $subtract: [2025, "$age"] // 2025년 기준 태어난 연도 계산
  ```
- `$cond`: 조건에 따라 두 가지 결과 중 하나를 반환
  ```javascript
  $cond: [{ $gte: ["$age", 60] }, "Senior", "General"] // age가 60 이상일 경우는 Senior, 아니면 General
  ```
- `$switch`: 여러 조건 중 처음 참인 결과를 반환
  ```javascript
  $switch: {
    branches: [
      { case: { $in: ["$country", ["USA", "Canada"]] }, then: "America" },
      { case: { $in: ["$country", ["UK", "Germany"]] }, then: "Europe" }
    ],
    default: "Earth"
  }
  ```

### Aggregate

#### $group
`$group`은 `_id` 기준으로 문서를 그룹화하여, 그룹별 합계, 평균, 최대값 등 다양한 집계 값을 계산할 때 사용됩니다

```javascript
db.users.aggregate([
  {
    $group: {
      _id: "$country",
      totalUsers: { $sum: 1 },
      avgAge: { $avg: "$age" }
    }
  }
])
```

```javascript
[
  { _id: 'UK', totalUsers: 2, avgAge: 30.5 },
  { _id: 'USA', totalUsers: 4, avgAge: 31 },
  { _id: 'Canada', totalUsers: 2, avgAge: 26 },
  { _id: 'Germany', totalUsers: 2, avgAge: 33.5 }
]
```

#### $unwind
`$unwind`는 배열 필드를 분해해 배열 내 각 요소를 별도의 문서로 만듭니다. 배열을 낱개 단위로 처리할 때 매우 유용합니다.

```javascript
db.users.aggregate([
  { $unwind: "$location" }
])
```

```javascript
[
  {
    _id: ObjectId('683d195d172a0eb2876c4bd0'),
    name: 'Alice',
    age: 25,
    country: 'USA',
    active: true,
    location: 'New York'
  },
  {
    _id: ObjectId('683d195d172a0eb2876c4bd0'),
    name: 'Alice',
    age: 25,
    country: 'USA',
    active: true,
    location: 'Boston'
  },
  ...
]
```



#### $lookup
`$lookup`은 다른 컬렉션과 조인해 관련 데이터를 현재 문서에 결합합니다. 여러 컬렉션 데이터를 합쳐 분석할 때 자주 사용됩니다.

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "name",
      as: "users"
    }
  }
])
```

```javascript
[
  {
    _id: ObjectId('683d1960172a0eb2876c4bda'),
    orderId: 1,
    userId: 'Alice',
    amount: 100,
    status: 'completed',
    users: [
      {
        _id: ObjectId('683d195d172a0eb2876c4bd0'),
        name: 'Alice',
        age: 25,
        country: 'USA',
        active: true,
        location: [ 'New York', 'Boston' ]
      }
    ]
  },
  ...
]
```

#### $bucket
`$bucket`은 특정 필드 값을 정해진 범위별로 나누어 그룹화하고, 각 구간에 대한 집계를 수행할 때 활용됩니다.

```javascript
db.users.aggregate([
  {
    $bucket: {
      groupBy: "$age",
      boundaries: [0, 10, 20, 30, 40, 50],
      default: "Other",
      output: { count: { $sum: 1 } }
    }
  }
])
```

```javascript
[
  { _id: 10, count: 1 },
  { _id: 20, count: 6 },
  { _id: 30, count: 5 },
  { _id: 40, count: 2 }
]
```


#### $facet
`$face`t은 여러 개의 하위 파이프라인을 동시에 병렬로 실행하여, 각각의 결과를 한 번에 묶어 반환할 때 사용합니다.

```javascript
db.users.aggregate([
  {
    $facet: {
      americans: [ { $match: { country: { $in: ["USA", "Canada"] } } } ],
      europeans : [ { $match: { country: { $in: ["UK", "Germany"] } } } ]
    }
  }
])
```

```javascript
[
  {
    americans: [
      {
        _id: ObjectId('683d195d172a0eb2876c4bd0'),
        name: 'Alice',
        age: 25,
        country: 'USA',
        active: true,
        location: [ 'New York', 'Boston' ]
      },
      ...
    ],
    europeans: [
      {
        _id: ObjectId('683d195d172a0eb2876c4bd3'),
        name: 'Diana',
        age: 28,
        country: 'UK',
        active: true,
        location: [ 'London' ]
      },
      ...
    ]
  }
]
```

### Output

#### $out
`$out`은 파이프라인 결과를 지정한 컬렉션에 저장하거나 기존 컬렉션을 완전히 덮어쓰는 역할을 합니다. 최종 결과 저장용입니다.

```javascript
db.users.aggregate([
  { $match: { active: true } },
  { $out: "active_users" }
])
```

#### $merge
`$merge`는 집계 결과를 기존 컬렉션에 병합하며, _id 기준으로 삽입, 갱신, 삭제를 수행할 수 있어 복잡한 업데이트 작업에 적합합니다.

```javascript
db.users.aggregate([
  {
    $merge: {
      into: "merge_users",
      whenMatched: "merge",
      whenNotMatched: "insert"
    }
  }
])
```

---

## References
- [MongoDB 공식 문서](https://www.mongodb.com/docs/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
