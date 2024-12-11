---
title: Parallel Processing
category: Python
tag: [Python]
---

> Python에서 병렬 처리(parallel processing)는 다중 작업을 동시에 수행하여 효율성을 높이는 방법입니다. 병렬 처리 기법으로는 멀티스레딩, 멀티프로세싱, 비동기 프로그래밍 등이 있습니다. 각 기법은 상황에 따라 다르게 사용될 수 있으며, 이를 적절히 활용하면 성능을 크게 향상시킬 수 있습니다.

---

## Multithreading
`멀티스레딩(Multithreading)`은 하나의 프로세스 내에서 여러 개의 스레드를 생성하여 동시에 여러 작업을 처리하는 기법입니다. Python에서 멀티스레딩은 `threading` 모듈을 통해 구현할 수 있습니다. 그러나 Python의 `Global Interpreter Lock(GIL)` 때문에 멀티스레딩은 CPU 집약적인 작업에서 성능을 크게 향상시키지 않습니다. I/O 작업에서 효과적입니다.

```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(letter)
        time.sleep(1)

# 스레드 생성
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# 스레드 시작
thread1.start()
thread2.start()

# 스레드 종료 대기
thread1.join()
thread2.join()

print("Both threads have finished.")
# 숫자와 문자들이 번갈아가며 출력되고, "Both threads have finished."가 마지막에 출력됨.
```
이 코드에서는 두 개의 스레드를 동시에 실행하여 숫자와 문자를 번갈아 출력합니다. `join()` 메서드는 스레드가 모두 종료될 때까지 기다리게 합니다.

---

## Multiprocessing
`멀티프로세싱(Multiprocessing)`은 여러 프로세스를 생성하여 각 프로세스가 독립적으로 실행되도록 하는 기법입니다. 멀티프로세싱은 GIL의 영향을 받지 않기 때문에 CPU 집약적인 작업에서 성능을 극대화할 수 있습니다. Python에서는 `multiprocessing` 모듈을 사용합니다.

```python
import multiprocessing
import time

def print_square(number):
    print(f"Square of {number}: {number * number}")
    time.sleep(1)

def print_cube(number):
    print(f"Cube of {number}: {number * number * number}")
    time.sleep(1)

if __name__ == '__main__':
    # 멀티프로세싱을 이용한 프로세스 생성
    process1 = multiprocessing.Process(target=print_square, args=(3,))
    process2 = multiprocessing.Process(target=print_cube, args=(3,))

    # 프로세스 시작
    process1.start()
    process2.start()

    # 프로세스 종료 대기
    process1.join()
    process2.join()

    print("Both processes have finished.")
# 3의 제곱과 3의 세제곱이 출력되고, 마지막에 "Both processes have finished."가 출력됨.
```
위 예시에서는 두 개의 프로세스를 동시에 실행하여 각각 제곱과 세제곱을 계산합니다. 멀티프로세싱을 통해 CPU 집약적인 작업을 병렬로 처리할 수 있습니다.

---

## Asynchronous Programming
`비동기 프로그래밍(Asynchronous Programming)`은 하나의 스레드에서 여러 작업을 효율적으로 처리하는 기법입니다. Python에서는 `asyncio` 모듈을 사용하여 비동기 프로그램을 작성할 수 있습니다. 비동기 프로그래밍은 특히 I/O 작업에서 성능을 향상시키는 데 유리합니다.

```python
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data fetched!")

async def process_data():
    print("Processing data...")
    await asyncio.sleep(1)
    print("Data processed!")

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(process_data())

    await task1
    await task2
    print("Both tasks are finished.")

# 비동기 프로그래밍 실행
asyncio.run(main())
# 
# Fetching data...
# Processing data...
# Data fetched!
# Data processed!
# Both tasks are finished.
```
이 코드에서는 두 개의 비동기 함수 `fetch_data`와 `process_data`를 동시에 실행하여 I/O 작업을 비동기적으로 처리합니다. `await`를 사용하여 비동기 작업을 기다리고, `asyncio.run()`으로 메인 이벤트 루프를 실행합니다.

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
