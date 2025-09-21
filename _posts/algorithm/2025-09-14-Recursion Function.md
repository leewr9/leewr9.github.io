---
title: Recursion Function
category: Algorithm
tag: [Python, Recursion, Algorithm]
---

> 재귀 함수는 함수가 자기 자신을 호출하는 프로그래밍 기법입니다. 복잡한 문제를 작은 문제로 나누어 해결할 수 있도록 해주며, 특히 반복적 접근보다 직관적으로 문제를 표현할 수 있는 장점이 있습니다.

---

## Recursion

재귀 함수는 자기 자신을 반복적으로 호출하는 함수로, 복잡한 문제를 더 작은 단위로 나누어 간단하게 표현할 수 있습니다. 재귀를 제대로 활용하려면 두 가지 중요한 요소를 반드시 갖춰야 합니다.

- `Base Case`: 재귀를 종료할 조건. 없으면 무한 호출 발생.
- `Recursive Case`: 문제를 더 작은 문제로 쪼개 자기 자신을 호출.

### Factorial

`Factorial`은 각 단계의 값이 호출 스택에 쌓였다가 종료 조건에 도달하면 결과를 반환하며 이전 단계로 돌아가 곱셈을 수행합니다. 이를 통해 재귀 호출의 흐름과 스택 작동 방식을 쉽게 이해할 수 있습니다.

- `n! = n * (n-1)!`

```python
def factorial(n):
    if n == 1:  # Base Case
        return 1
    return n * factorial(n-1)  # Recursive Case

factorial(5)  # 120
```

### Fibonacci

`Fibonacci`는 하위 문제를 재귀적으로 해결하고 결과를 합쳐 최종 값을 얻습니다. `Memoization`을 적용하면 중복 계산을 방지하고 성능을 높일 수 있으며, 재귀 호출과 스택의 동작 방식을 이해하는 데 적합합니다.

- `F(n) = F(n-1) + F(n-2)`

```python
def fibonacci(n):
    if n <= 1:  # Base Case
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Recursive Case

fibonacci(10)  # 55
```

### Backtracking

`Backtracking`은 재귀를 활용한 탐색 기법으로, 조건을 만족하는 선택만 유지하고 불필요한 선택은 되돌아가는 방식입니다. 문제를 단계별로 나누어 가능한 선택을 시도하고, 조건을 만족하지 않으면 이전 단계로 돌아가 다른 선택을 탐색합니다.

```python
def combinations(arr, r, start, path):
    if len(path) == r:  # Base Case
        return
    for i in range(start, len(arr)):
        path.append(arr[i])
        print('  ' * start, '>', arr[i], path)
        combinations(arr, r, i+1, path)  # Recursive Case
        path.pop()  # Backtracking
        print('  ' * start, '<', arr[i], path)

combinations(['A', 'B', 'C', 'D'], 3, 0, [])
```

```python
 > A ['A']
   > B ['A', 'B']
     > C ['A', 'B', 'C']
     < C ['A', 'B']  # Backtracking
     > D ['A', 'B', 'D']
     < D ['A', 'B']  # Backtracking
   < B ['A']  # Backtracking
   > C ['A', 'C']
       > D ['A', 'C', 'D']
       < D ['A', 'C']  # Backtracking
   < C ['A']  # Backtracking
   > D ['A', 'D']
   < D ['A']  # Backtracking
 < A []  # Backtracking
 > B ['B']
     > C ['B', 'C']
       > D ['B', 'C', 'D']
       < D ['B', 'C']  # Backtracking
     < C ['B']  # Backtracking
     > D ['B', 'D']
     < D ['B']  # Backtracking
 < B []  # Backtracking
 > C ['C']
       > D ['C', 'D']
       < D ['C']  # Backtracking
 < C []  # Backtracking
 > D ['D']
 < D []  # Backtracking
```

---

## Memoization

`Memoization`은 이미 계산한 값을 저장하여, 같은 계산을 반복하지 않도록 하는 기법입니다. 특히 재귀 호출이 중복되는 문제에서 큰 성능 향상을 가져오며, 재귀의 직관적인 구조를 유지하면서 성능 문제를 해결할 수 있습니다.

```python
memo = {}  # Memoization
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]
```

---

## Pruning

`Pruning`은 불필요한 재귀 호출을 미리 차단하여 효율성을 높이는 기법입니다. 백트래킹 문제에서 자주 사용되며, 조건을 만족하지 않으면 즉시 되돌아가 다른 선택을 시도합니다. 탐색 공간이 큰 문제에서 성능을 극적으로 개선할 수 있습니다.

```python
def subset_sum(arr, target, path=[], total=0):
    if total > target:
        return  # Pruning
    if total == target:
        return
    for i in range(len(arr)):
        subset_sum(arr[i+1:], target, path+[arr[i]], total+arr[i])
```

---

## References

- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
