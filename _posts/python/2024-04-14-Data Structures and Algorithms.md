---
title: Data Structures and Algorithms
category: Python
tag: [Algorithm, Structure, Python]
---

> 자료구조와 알고리즘은 데이터를 효율적으로 저장하고 처리하는 방법을 제공합니다. 
Python은 다양한 내장 자료구조와 이를 지원하는 모듈을 제공하며, 이를 활용하면 효과적으로 문제를 해결할 수 있습니다. 

---

## List  
리스트는 순서가 있는 가변 길이의 자료구조입니다.

```python
# 리스트 생성
numbers = [1, 2, 3, 4, 5]

# 리스트 요소 추가
numbers.append(6)

# 리스트 요소 제거
numbers.remove(3)

# 리스트 요소 접근
print(numbers[0]) # 출력: 1

# 리스트 슬라이싱
print(numbers[1:4]) # 출력: [2, 4, 5]
```

---

## Tuple  
튜플은 순서가 있지만 변경할 수 없는 자료구조입니다.

```python
# 튜플 생성
coordinates = (10, 20)

# 요소 접근
print(coordinates[0]) # 출력: 10

# 튜플 언패킹
x, y = coordinates
print(x, y) # 출력: 10 20
```

---

## Set  
세트는 중복이 없는 요소들의 집합으로, 순서가 없습니다.

```python
# 세트 생성
fruits = {"apple", "banana", "cherry"}

# 요소 추가
fruits.add("orange")

# 요소 제거
fruits.discard("banana")

# 집합 연산
other_fruits = {"apple", "grape"}
print(fruits.intersection(other_fruits)) # 출력: {'apple'}
```

---

## Dictionary  
딕셔너리는 키-값 쌍으로 이루어진 자료구조입니다.

```python
# 딕셔너리 생성
person = {"name": "Alice", "age": 25}

# 값 추가/변경
person["job"] = "Engineer"

# 값 제거
del person["age"]

# 키/값 접근
print(person["name"]) # 출력: Alice
```

---

## Stack  
스택은 후입선출(LIFO) 방식의 자료구조입니다. Python에서는 리스트를 활용해 구현합니다.

```python
stack = []

# 푸시
stack.append(1)
stack.append(2)

# 팝
print(stack.pop()) # 출력: 2
print(stack) # 출력: [1]
```

---

## Queue  
큐는 선입선출(FIFO) 방식의 자료구조입니다. `collections.deque`를 사용해 효율적으로 구현할 수 있습니다.

```python
from collections import deque

queue = deque()

# 요소 추가
queue.append(1)
queue.append(2)

# 요소 제거
print(queue.popleft()) # 출력: 1
print(queue) # 출력: deque([2])
```

---

## Heap  
힙은 우선순위 큐를 구현하는 데 사용되는 자료구조입니다. Python의 `heapq` 모듈을 이용합니다.

```python
import heapq

heap = []

# 요소 추가
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

# 최소값 제거
print(heapq.heappop(heap)) # 출력: 1
print(heap) # 출력: [2, 3]
```

---

## Hash  
해시는 키를 이용해 값을 저장하고 검색하는 데 사용됩니다. Python에서는 딕셔너리가 해시 테이블의 역할을 합니다.

```python
hash_table = {}

# 값 추가
hash_table["key1"] = "value1"

# 값 접근
print(hash_table["key1"]) # 출력: value1

# 값 삭제
del hash_table["key1"]
```

---

## Tree and Graph  
트리와 그래프는 노드와 엣지로 구성된 자료구조입니다. Python의 `collections.defaultdict`와 재귀를 활용해 구현할 수 있습니다.

```python
from collections import defaultdict

# 그래프 생성
graph = defaultdict(list)
graph[1].append(2)
graph[1].append(3)
graph[2].append(4)

# DFS (깊이 우선 탐색)
def dfs(node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=" ") # 방문한 노드 출력
        for neighbor in graph[node]:
            dfs(neighbor, visited)

visited = set()
dfs(1, visited) # 출력: 1 2 4 3
```

---

## Built-in Modules  
`collections`, `heapq` 등 모듈로 자료구조를 쉽게 구현할 수 있습니다.

- `collections.Counter`: 요소 개수 세기
- `collections.OrderedDict`: 순서를 유지하는 딕셔너리
- `heapq`: 힙 연산

```python
from collections import Counter

# 요소 개수 세기
counter = Counter(["apple", "banana", "apple", "orange"])
print(counter) # 출력: Counter({'apple': 2, 'banana': 1, 'orange': 1})
```

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
