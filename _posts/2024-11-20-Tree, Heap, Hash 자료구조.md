---
title: Tree, Heap, Hash 자료구조
category: Study
tag: [Education, Structure, Python]
---

<nav class="post-toc" markdown="1">
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

## 트리 (Tree)
> 트리(Tree)는 비선형 자료구조로, **노드(Node)** 와 **간선(Edge)** 로 구성된 계층적 구조입니다. 
트리는 **루트 노드(root node)** 에서 시작해 여러 개의 하위 트리로 나뉘어갑니다.

### 1. 트리의 종류
* 이진 트리(Binary Tree): 각 노드가 최대 2개의 자식 노드를 가질 수 있는 트리
* 이진 탐색 트리(Binary Search Tree, BST): 이진 트리의 일종으로, 왼쪽 자식 노드는 부모 노드보다 작은 값, 오른쪽 자식 노드는 부모 노드보다 큰 값을 가지는 트리
* 힙(Heap): 트리의 일종으로, 우선순위 큐를 구현하는 데 사용됨

### 2. Python에서 트리 구현
> Python에서 트리를 구현하려면 **클래스(Class)** 를 사용하여 트리 구조를 정의할 수 있습니다. 

* 이진 트리(Binary Tree)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 이진 트리 만들기
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)

# 트리 탐색 (중위 순회)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

inorder_traversal(root)  # 3 5 7 10 20
```

* 이진 탐색 트리(Binary Search Tree, BST)

```python
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 삽입 함수
def insert(root, value):
    if root is None:
        return BSTNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# 이진 탐색 트리 만들기
bst_root = BSTNode(10)
insert(bst_root, 5)
insert(bst_root, 15)
insert(bst_root, 3)
insert(bst_root, 7)

# 트리 탐색 (중위 순회)
 inorder_traversal(bst_root)  # 3 5 7 10 15
```

## 힙 (Heap)
> 힙(Heap)은 완전 이진 트리를 기반으로 한 자료구조로, 각 부모 노드가 자식 노드보다 우선순위가 높은 구조입니다. 
힙은 주로 우선순위 큐(Priority Queue) 구현에 사용됩니다. 힙은 두 가지 유형이 있습니다:

* 최소 힙(Min-Heap): 부모 노드의 값이 자식 노드의 값보다 작음.
* 최대 힙(Max-Heap): 부모 노드의 값이 자식 노드의 값보다 큼.

### 1. Python에서 힙 사용
> Python에서는 heapq 모듈을 통해 힙을 쉽게 구현할 수 있습니다. 
기본적으로 heapq는 최소 힙(Min-Heap)을 제공합니다.

* 최소 힙 (Min-Heap)

```python
import heapq

# 빈 리스트를 힙으로 사용
heap = []

# 데이터를 힙에 추가 (push 연산)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)

print(heap)  # [5, 20, 10]

# 힙에서 가장 작은 값 제거 (pop 연산)
smallest = heapq.heappop(heap)
print(smallest)  # 5
print(heap)  # [10, 20]

# 힙에서 가장 작은 값 조회 (peek 연산)
peek = heap[0]
print(peek)  # 10
```

* 최대 힙 (Max-Heap)

```python
import heapq

# 최대 힙을 구현하려면 값을 부호 반전시켜 최소 힙처럼 사용
heap = []

# 데이터를 힙에 추가 (push 연산)
heapq.heappush(heap, -10)
heapq.heappush(heap, -20)
heapq.heappush(heap, -5)

print([-x for x in heap])  # [20, 10, 5] (최대 힙)

# 힙에서 가장 큰 값 제거 (pop 연산)
largest = -heapq.heappop(heap)
print(largest)  # 20
```

## 해시 (Hash)
> 해시는 키-값 쌍으로 데이터를 저장하는 자료구조로, 빠른 검색과 삭제 연산을 지원합니다. 
해시는 배열을 이용한 인덱싱 방식으로 데이터를 저장하고 검색하는 방식이기 때문에 매우 효율적입니다.

### 1. Python에서 해시 사용
> Python에서는 dict(딕셔너리)를 사용하여 해시를 구현할 수 있습니다. 
딕셔너리는 해시 테이블을 기반으로 구현되어 있으며, 키를 통해 값을 빠르게 조회할 수 있습니다.

```python
# 해시맵 (딕셔너리) 생성
hash_map = {}

# 키-값 쌍 추가
hash_map["apple"] = 1
hash_map["banana"] = 2
hash_map["cherry"] = 3

# 값 조회
print(hash_map["banana"])  # 2

# 키 존재 여부 확인
print("apple" in hash_map)  # True
print("orange" in hash_map)  # False

# 키-값 쌍 삭제
del hash_map["banana"]
print(hash_map)  # {'apple': 1, 'cherry': 3}
```
