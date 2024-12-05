---
title: Stack, Queue 자료구조
category: Study
tag: [Education, Structure, Python]
---

<nav class="post-toc" markdown="1">
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

## 스택 (Stack)
> 스택(Stack)은 후입선출(LIFO, Last In First Out) 방식의 자료구조로, 마지막에 들어온 데이터가 가장 먼저 나오는 구조입니다. 
스택은 주로 함수 호출, 웹 브라우저의 뒤로 가기 버튼, 괄호 짝 맞추기 등에서 사용됩니다.

### 1. 기본 기능
* push: 데이터를 스택에 추가
* pop: 스택에서 데이터를 제거하고 반환
* peek: 스택의 가장 위에 있는 데이터를 반환 (제거하지 않음)
* isEmpty: 스택이 비었는지 확인

### 2. Python에서 스택 구현
> Python에서는 기본적으로 **리스트(List)**를 사용하여 스택을 구현할 수 있습니다. 리스트의 append()는 push, pop()은 pop 연산에 해당합니다.

```python
stack = []

# push
stack.append(10)  # 스택에 10 추가
stack.append(20)  # 스택에 20 추가
stack.append(30)  # 스택에 30 추가

print(stack)  # [10, 20, 30]

# pop
top_element = stack.pop()  # 30 제거
print(top_element)  # 30
print(stack)  # [10, 20]

# peek
top_element = stack[-1]  # 마지막 요소 조회 (제거하지 않음)
print(top_element)  # 20

# isEmpty
print(len(stack) == 0)  # False (스택이 비지 않았음)
```

## 큐 (Queue)
> 큐(Queue)는 선입선출(FIFO, First In First Out) 방식의 자료구조로, 가장 먼저 들어온 데이터가 가장 먼저 나옵니다. 
큐는 대기열, 프린터 작업 관리, 데이터 스트리밍 등에 사용됩니다.

### 1. 기본 기능
* enqueue: 큐에 데이터를 추가
* dequeue: 큐에서 데이터를 제거하고 반환
* peek: 큐의 첫 번째 데이터를 반환 (제거하지 않음)
* isEmpty: 큐가 비었는지 확인

### 2. Python에서 큐 구현
> Python에서는 **리스트(List)** 를 사용하여 큐를 구현할 수 있지만, collections.deque를 사용하는 것이 더 효율적입니다. 리스트는 pop(0) 연산이 비효율적이지만, deque는 양쪽 끝에서 데이터를 효율적으로 추가하고 제거할 수 있습니다.

* list() 사용

```python
queue = []

# enqueue
queue.append(10)  # 큐에 10 추가
queue.append(20)  # 큐에 20 추가
queue.append(30)  # 큐에 30 추가

print(queue)  # [10, 20, 30]

# dequeue
front_element = queue.pop(0)  # 10 제거
print(front_element)  # 10
print(queue)  # [20, 30]

# peek
front_element = queue[0]  # 첫 번째 요소 조회
print(front_element)  # 20

# isEmpty
print(len(queue) == 0)  # False (큐가 비지 않았음)
```

* deque() 사용

```python
from collections import deque

queue = deque()

# enqueue
queue.append(10)  # 큐에 10 추가
queue.append(20)  # 큐에 20 추가
queue.append(30)  # 큐에 30 추가

print(queue)  # deque([10, 20, 30])

# dequeue
front_element = queue.popleft()  # 10 제거
print(front_element)  # 10
print(queue)  # deque([20, 30])

# peek
front_element = queue[0]  # 첫 번째 요소 조회
print(front_element)  # 20

# isEmpty
print(len(queue) == 0)  # False (큐가 비지 않았음)
```

## 스택과 큐의 차이점

| 특성 | 스택 (Stack) | 큐 (Queue) |
| - | - | - |
| 작동 방식 | 후입선출(LIFO) | 선입선출(FIFO) |
| 기본 연산 | push, pop, peek, isEmpty | enqueue, dequeue, peek, isEmpty |
| 사용 예시	| 함수 호출 스택, 웹 브라우저 뒤로 가기	| 대기열, 프린터 큐, 데이터 스트리밍 |
