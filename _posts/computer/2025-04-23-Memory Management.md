---
title: Memory Management
category: Computer
tag: [Memory, OS]
---

> 운영체제는 메모리 관리와 관련된 여러 기법을 사용하여 시스템의 성능과 안정성을 보장합니다. 이 기법들은 프로그램이 실행될 때 발생할 수 있는 메모리 부족 문제를 해결하고, 효율적인 자원 사용을 최적화하는 데 중요한 역할을 합니다.

---

## Virtual Memory
`Virtual Memory`는 물리적 메모리의 한계를 넘어서서 프로그램이 더 많은 메모리를 사용할 수 있도록 돕는 기술입니다. 운영체제는 하드 드라이브의 일부 공간을 가상 메모리로 사용하여, 실제 물리 메모리보다 더 큰 메모리 공간을 제공하는 것처럼 다룰 수 있습니다. 가상 메모리는 페이징을 통해 가상 주소와 물리 주소 간의 매핑을 관리합니다.

[![](\assets\posts\2025-04-23-Memory Management.md\paging.png)](\assets\posts\2025-04-23-Memory Management.md\paging.png)

### Paging
`Paging`은 메모리를 작은 고정 크기의 블록으로 나누어 관리하는 기법입니다. 각 블록을 페이지라고 하며, 가상 메모리 주소 공간을 물리 메모리로 매핑하여 운영체제가 효율적으로 메모리를 관리하도록 합니다. 페이징은 메모리 단편화를 방지하고, 프로그램 실행 시 메모리 자원을 최적화하는 데 도움이 됩니다.

### Fragmentation 
`Fragmentation`는 메모리가 여러 개의 작은 조각으로 나누어져 비효율적으로 사용되는 현상입니다. 이는 메모리 할당 시 발생할 수 있으며, 메모리 자원의 낭비를 초래할 수 있습니다. 내부 단편화와 외부 단편화로 나뉘어, 각각 다른 방식으로 문제를 일으킬 수 있습니다.

---

## Cache Memory
`Cache Memory`는 CPU와 메인 메모리 간의 속도 차이를 해결하기 위한 고속의 임시 저장소입니다. CPU가 자주 사용하는 데이터를 캐시 메모리에 저장하여, 메인 메모리보다 더 빠르게 데이터에 접근할 수 있도록 합니다. 캐시 메모리는 성능을 최적화하며, 여러 레벨로 구성됩니다.

[![](\assets\posts\2025-04-23-Memory Management.md\cache.png)](\assets\posts\2025-04-23-Memory Management.md\cache.png)

---

## Swapping
`Swapping`은 물리 메모리가 부족할 때 사용되지 않는 데이터를 하드 드라이브로 이동시키고, 필요한 데이터를 메모리로 가져오는 기법입니다. 시스템 성능이 떨어질 수 있기 때문에, 자주 발생하면 쓰레싱이 발생할 수 있습니다.

[![](\assets\posts\2025-04-23-Memory Management.md\swapping.png)](\assets\posts\2025-04-23-Memory Management.md\swapping.png)

### Thrashing
`Thrashing`은 시스템이 과도하게 스와핑을 수행할 때 발생하는 문제로, CPU와 디스크 간의 지나치게 많은 데이터 이동으로 인해 시스템 성능이 크게 저하되는 현상입니다. 쓰래싱이 발생하면, 프로그램 실행 속도가 느려지고, 시스템 자원을 낭비하게 됩니다.

---

## Issues

### Page Fault
`Page Fault`는 프로그램이 가상 메모리에서 접근하려는 페이지가 물리 메모리에 존재하지 않을 때 발생하는 오류입니다. 이 경우 운영체제는 하드 디스크에서 필요한 페이지를 로드해야 합니다. 페이지 폴트가 자주 발생하면 시스템 성능에 영향을 미칠 수 있습니다.

### Memory Leaks
`Memory Leaks`는 프로그램이 동적으로 할당한 메모리를 제대로 해제하지 않아, 계속해서 메모리 자원이 소모되는 오류입니다. 이 문제는 특히 장기 실행되는 프로그램에서 심각한 성능 저하를 초래할 수 있습니다.

---

## References
- [Wikipedia 공식 문서](https://wikipedia.org/wiki/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
