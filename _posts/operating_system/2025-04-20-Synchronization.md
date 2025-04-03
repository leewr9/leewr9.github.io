---
title: Synchronization
category: Operating System
tag: [Python, Spinlock, Semaphore, Mutex, OS, Operating System]
---

> 운영체제는 다양한 동기화 기법과 메모리 관리 기법을 통해 효율적인 작업 처리를 보장합니다. 동기화는 여러 스레드가 공유 자원에 동시에 접근할 때 발생할 수 있는 문제를 해결하는 기법입니다. 이를 통해 스레드 간 충돌을 방지하고, 순차적으로 자원을 접근하게 할 수 있습니다.

---

## Techniques

### Mutex
`Mutex`는 `Mutual Exclusion`의 약자로, 공유 자원에 대한 동시 접근을 제어하는 동기화 기법입니다. 여러 프로세스나 스레드가 자원에 동시에 접근하지 않도록 보장하는 역할을 합니다. 뮤텍스는 한 스레드만 자원을 사용할 수 있도록 하며, 다른 스레드는 자원을 사용할 수 없을 때까지 대기합니다.

```python
import threading

total = 0
lock = threading.Lock()  # Mutual Exclusion

def no_lock():
    global total
    for _ in range(3):
        print(f"No Lock: {threading.current_thread().name} - Before: {total}")
        total += 1
        print(f"No Lock: {threading.current_thread().name} - After: {total}")

def with_lock():
    global total
    for _ in range(3):
        with lock:
            print(f"Lock: {threading.current_thread().name} - Before: {total}")
            total += 1
            print(f"Lock: {threading.current_thread().name} - After: {total}")

threads_no_lock = [threading.Thread(target=no_lock, name=f"Thread-{i}") for i in range(2)]
threads_with_lock = [threading.Thread(target=with_lock, name=f"Thread-{i}") for i in range(2)]

print("Running without Lock:")
for t in threads_no_lock:
    t.start()
for t in threads_no_lock:
    t.join()

print("\nRunning with Lock:")
for t in threads_with_lock:
    t.start()
for t in threads_with_lock:
    t.join()
```

```bash
Running without Lock:
No Lock: Thread-0 - Before: 0
No Lock: Thread-0 - After: 1
No Lock: Thread-1 - Before: 1 # Race Condition
No Lock: Thread-0 - Before: 1 # Race Condition
No Lock: Thread-1 - After: 2
No Lock: Thread-0 - After: 3
...

Running with Lock:
Lock: Thread-0 - Before: 6
Lock: Thread-0 - After: 7
Lock: Thread-0 - Before: 7
Lock: Thread-0 - After: 8
Lock: Thread-0 - Before: 8
Lock: Thread-0 - After: 9
Lock: Thread-1 - Before: 9
Lock: Thread-1 - After: 10
...
```

### Semaphore
`Semaphore`는 카운팅 기반의 동기화 기법으로, 지정된 개수의 스레드가 동시에 자원에 접근할 수 있도록 허용합니다. 뮤텍스와는 달리 세마포어는 단일 자원에만 국한되지 않고, 여러 자원에 대해 관리할 수 있습니다.

```python
import time
import threading

semaphore = threading.Semaphore(2)  # Semaphore

def no_semaphore():
    print(f"No Semaphore: {threading.current_thread().name} starting")
    time.sleep(1)
    print(f"No Semaphore: {threading.current_thread().name} exiting")

def with_semaphore():
    with semaphore:
        print(f"Semaphore: {threading.current_thread().name} starting")
        time.sleep(1)
        print(f"Semaphore: {threading.current_thread().name} exiting")

threads_no_semaphore = [threading.Thread(target=no_semaphore, name=f"Thread-{i}") for i in range(4)]
threads_with_semaphore = [threading.Thread(target=with_semaphore, name=f"Thread-{i}") for i in range(4)]

print("Running without Semaphore:")
for t in threads_no_semaphore:
    t.start()
for t in threads_no_semaphore:
    t.join()

print("\nRunning with Semaphore:")
for t in threads_with_semaphore:
    t.start()
for t in threads_with_semaphore:
    t.join()
```

```bash
Running without Semaphore:
No Semaphore: Thread-0 starting
No Semaphore: Thread-1 starting
No Semaphore: Thread-2 starting
No Semaphore: Thread-3 starting
...

Running with Semaphore: 
Semaphore: Thread-0 starting # Thread-0 시작 (1/2)
Semaphore: Thread-1 starting # Thread-1 시작 (2/2)
Semaphore: Thread-0 exiting # Thread-0 종료 (1/2)
Semaphore: Thread-2 starting # Thread-2 시작 (2/2)
Semaphore: Thread-1 exiting # Thread-1 종료 (1/2)
Semaphore: Thread-3 starting # Thread-3 시작 (2/2)
...
```

### Spinlock
`Spinlock`은 락을 획득하려는 스레드가 자원을 사용 중인 다른 스레드를 기다리는 동안 CPU 자원을 소모하면서 대기하는 형태입니다. 이 방식은 자원을 잠시 기다리는 데 유리할 수 있지만, 대기 시간이 길어지면 비효율적일 수 있습니다.

```python
import time
import threading

spinlock = threading.Lock()  # Spinlock

def no_spinlock():
    print(f"No Spinlock: {threading.current_thread().name} starting")
    time.sleep(1)
    print(f"No Spinlock: {threading.current_thread().name} exiting")

def with_spinlock():
    while not spinlock.acquire(blocking=False):  # Spinlock Wait
        pass
    print(f"Spinlock: {threading.current_thread().name} starting")
    time.sleep(1)
    print(f"Spinlock: {threading.current_thread().name} exiting")
    spinlock.release()  # Spinlock Release

threads_no_spinlock = [threading.Thread(target=no_spinlock, name=f"Thread-{i}") for i in range(4)]
threads_with_spinlock = [threading.Thread(target=with_spinlock, name=f"Thread-{i}") for i in range(4)]

print("Running without Spinlock:")
for t in threads_no_spinlock:
    t.start()
for t in threads_no_spinlock:
    t.join()

print("\nRunning with Spinlock:")
for t in threads_with_spinlock:
    t.start()
for t in threads_with_spinlock:
    t.join()
```

```bash
Running without Spinlock:
No Spinlock: Thread-0 starting
No Spinlock: Thread-1 starting
No Spinlock: Thread-2 starting
No Spinlock: Thread-3 starting
...

Running with Spinlock:
Spinlock: Thread-0 starting
Spinlock: Thread-0 exiting
Spinlock: Thread-1 starting
Spinlock: Thread-1 exiting
...
```

---

## Issues

### Race Condition
`Race Condition`은 둘 이상의 스레드가 공유 자원에 동시에 접근하면서 예기치 않은 결과를 초래하는 현상입니다. 이런 문제가 발생하는 코드 영역을 **크리티컬 섹션(Critical Section)**이라고 하며, 동기화 없이 실행되면 데이터 충돌이 일어날 수 있습니다

- **해결 방안**
    - `Mutex`: 자원을 사용하는 스레드를 하나로 제한하여 동시에 접근하지 못하게 함
    - `Semaphore`: 여러 스레드가 자원에 동시에 접근할 수 있는 수를 제한

### Deadlock 
`Deadlock`은 둘 이상의 프로세스나 스레드가 서로가 가진 자원을 기다리며 무한히 대기하는 상태입니다. 이로 인해 시스템이 더 이상 진행되지 않게 됩니다.

- **해결 방안**
    - **자원 순서 정하기**: 자원 요청 순서를 미리 정해놓고, 항상 그 순서대로 요청하도록 함
    - **타임아웃**: 자원을 일정 시간 이상 기다리면 다시 시도하도록 설정

[![](\assets\posts\2025-04-20-Synchronization.md\deadlock.png)](\assets\posts\2025-04-20-Synchronization.md\deadlock.png)

### Livelock
`Livelock`은 둘 이상의 프로세스나 스레드가 서로 자원을 요청하는 동안 상태가 변하지만 자원을 얻지 못하고 무한히 반복하는 상태입니다. 데드락처럼 진행되지 않지만, 시스템은 무한히 상태 변화를 진행합니다.

- **해결 방안**
    - **상태 변화 멈추기**: 프로세스가 계속 상태를 바꾸지 않고, 자원을 차지할 때까지 기다리도록 함
    - **우선순위 높이기**: 대기 시간이 긴 프로세스가 더 빨리 자원을 할당받을 수 있도록 함

### Starvation
`Starvation`는 특정 프로세스나 스레드가 자원을 할당받지 못하고 계속 대기하는 상태입니다. 자원이 지속적으로 다른 프로세스에 의해 차지되거나 우선순위가 낮아서 발생할 수 있습니다.

- **해결 방안**
    - **공평하게 나누기**: 모든 프로세스가 자원을 받을 수 있도록 공평하게 분배
    - **우선순위 조정**: 우선순위가 낮은 프로세스도 기회를 얻을 수 있도록 우선순위를 바꾸는 방법

---

## References
- [Wikipedia 공식 문서](https://wikipedia.org/wiki/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
