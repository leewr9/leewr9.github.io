---
title: Task Management
category: Computer
tag: [Python, Thread, Process, Task, OS]
---

> 운영체제는 컴퓨터 하드웨어와 소프트웨어 자원 간의 조정 및 관리를 담당하는 중요한 역할을 합니다. 효율적인 프로그램 실행과 자원 관리를 위해 필요한 핵심 개념들을 이해하는 것은 필수적입니다. 이들 개념을 통해 시스템의 작동 방식과 성능 최적화를 위한 고려사항들을 알아볼 수 있습니다.

---

## Process
`Process`는 운영체제에서 실행 중인 프로그램을 의미합니다. 각 프로세스는 독립적인 메모리 공간을 할당받고, 운영체제 내에서 독립적으로 실행되는 작업 단위입니다. 하나의 프로그램은 여러 개의 프로세스를 생성할 수 있으며, 각 프로세스는 서로 다른 주소 공간을 가지므로 서로 간의 데이터 공유가 어렵습니다.

- **독립적인 주소 공간**: 프로세스는 자신의 코드, 데이터, 힙, 스택을 포함한 독립적인 메모리 공간을 가집니다.
- **독립적인 자원 할당**: 운영체제에서 메모리, 파일 핸들 등 자원을 별도로 할당받습니다.
- **프로세스 간 통신 필요**: 프로세스 간 자원을 공유하려면 프로세스 간 통신을 사용해야 합니다.

### Thread
`Thread`는 프로세스 내에서 실행되는 작은 실행 단위입니다. 하나의 프로세스는 여러 개의 스레드를 가질 수 있으며, 이들은 같은 메모리 공간을 공유하면서 실행됩니다.

- **같은 주소 공간**: 스레드는 프로세스의 메모리 공간을 공유하지만, 각 스레드는 개별적인 스택을 가집니다.
- **자원 공유 용이**: 스레드 간 자원 공유가 용이하지만, 동시에 접근하는 경우 동기화 문제가 발생할 수 있습니다.
- **경량화된 실행 단위**: 스레드는 프로세스에 비해 상대적으로 가벼운 실행 단위로, 문맥 교환 비용이 낮습니다.

[![](\assets\posts\2025-04-20-Task Management.md\process.png)](\assets\posts\2025-04-20-Task Management.md\process.png)

---

## Multitasking

### Multiprocessing
`Multiprocessing`은 여러 개의 프로세스를 동시에 실행하여 작업을 병렬로 처리하는 방식입니다. 각 프로세스는 독립적인 메모리 공간을 가지며, 서로 독립적으로 실행됩니다. 멀티프로세싱은 멀티코어 시스템에서 여러 프로세스가 동시에 실행되도록 하여 성능을 극대화할 수 있습니다.

```python
import time
import multiprocessing

def task():
    total = 0
    for _ in range(10000000):
        total += 1
    print(f"Running in {multiprocessing.current_process().name} with total = {total}")

if __name__ == "__main__":
    start = time.time()

    processes = [multiprocessing.Process(target=task, name=f"Process-{i}") for i in range(10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
        
    end = time.time()
    print(f"Execution time: {end - start:.2f} seconds")
```

```bash
Running in Process-0 with total = 10000000
Running in Process-1 with total = 10000000
Running in Process-3 with total = 10000000
Running in Process-2 with total = 10000000
Running in Process-6 with total = 10000000
Running in Process-5 with total = 10000000
Running in Process-7 with total = 10000000
Running in Process-4 with total = 10000000
Running in Process-8 with total = 10000000
Running in Process-9 with total = 10000000
Execution time: 0.52 seconds
```

### Multithreading
`Multithreading`은 하나의 프로세스 내에서 여러 개의 스레드가 동시에 실행되는 방식입니다. 모든 스레드는 같은 메모리 공간을 공유하므로, 스레드 간 자원 공유가 용이합니다. 멀티스레딩은 하나의 프로세스에서 여러 작업을 동시에 처리할 수 있게 해 주며, 시간 분할 방식으로 CPU를 효율적으로 사용할 수 있습니다.

```python
import time
import threading

def task():
    total = 0
    for _ in range(10000000):
        total += 1
    print(f"Running in {threading.current_thread().name} with total = {total}")

if __name__ == "__main__":
    start = time.time()

    threads = [threading.Thread(target=task, name=f"Thread-{i}") for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    end = time.time()
    print(f"Execution time: {end - start:.2f} seconds")
```

```bash
Running in Thread-1 with total = 10000000
Running in Thread-0 with total = 10000000
Running in Thread-2 with total = 10000000
Running in Thread-9 with total = 10000000
Running in Thread-6 with total = 10000000
Running in Thread-3 with total = 10000000
Running in Thread-4 with total = 10000000
Running in Thread-5 with total = 10000000
Running in Thread-8 with total = 10000000
Running in Thread-7 with total = 10000000
Execution time: 2.28 seconds
```

### Context Switching
`Context Switching`은 CPU가 현재 실행 중인 작업을 중단하고 다른 작업을 실행하기 위해 상태 정보를 저장하고 복원하는 과정입니다. 멀티태스킹 환경에서 필수적인 개념으로, 프로세스나 스레드 간에 전환이 발생할 때마다 이루어집니다. 이 과정은 필연적으로 오버헤드를 발생시키며, 스레드 간 전환이 프로세스 간보다 적은 비용으로 수행됩니다.

---

## References
- [Wikipedia 공식 문서](https://wikipedia.org/wiki/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
