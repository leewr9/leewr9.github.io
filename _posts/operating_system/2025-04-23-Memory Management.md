---
title: Memory Management
category: Operating System
tag: [Memory, OS, Operating System]
---

> 운영체제는 메모리 관리와 관련된 여러 기법을 사용하여 시스템의 성능과 안정성을 보장합니다. 이 기법들은 프로그램이 실행될 때 발생할 수 있는 메모리 부족 문제를 해결하고, 효율적인 자원 사용을 최적화하는 데 중요한 역할을 합니다.

---

## Virtual Memory
`Virtual Memory`는 물리적 메모리의 한계를 넘어서서 프로그램이 더 많은 메모리를 사용할 수 있도록 돕는 기술입니다. 운영체제는 하드 드라이브의 일부 공간을 가상 메모리로 사용하여, 실제 물리 메모리보다 더 큰 메모리 공간을 제공하는 것처럼 다룰 수 있습니다. 가상 메모리는 페이징을 통해 가상 주소와 물리 주소 간의 매핑을 관리합니다.

[![](\assets\posts\2025-04-23-Memory Operation.md\paging.png)](\assets\posts\2025-04-23-Memory Operation.md\paging.png)

### Paging
`Paging`은 메모리를 작은 고정 크기의 블록으로 나누어 관리하는 기법입니다. 각 블록을 페이지라고 하며, 가상 메모리 주소 공간을 물리 메모리로 매핑하여 운영체제가 효율적으로 메모리를 관리하도록 합니다. 페이징은 메모리 단편화를 방지하고, 프로그램 실행 시 메모리 자원을 최적화하는 데 도움이 됩니다.

- **FIFO(First In First Out)**: 가장 먼저 메모리에 들어온 페이지를 가장 먼저 교체하는 방식입니다. 구현이 간단하지만, 최근에 자주 사용된 데이터가 교체될 수 있어 비효율적일 수 있습니다.
- **LRU(Least Recently Used)**: 가장 최근에 사용되지 않은 페이지를 교체하는 방식입니다. 오랫동안 사용되지 않은 페이지를 메모리에서 제거하여 자주 사용되는 데이터를 더 오래 유지하려는 전략입니다.
- **LFU(Least Frequently Used)**: 가장 적게 사용된 데이터를 교체하는 방식입니다. 자주 사용된 데이터가 캐시에서 더 오래 유지되도록 하여, 장기적인 사용 패턴에 기반한 최적화를 제공합니다.

### Segmentation
`Segmentation`은 프로그램을 논리적인 단위인 세그먼트로 나누어 관리하는 기법입니다. 각 세그먼트는 코드, 데이터, 스택 등으로 구분되며, 크기가 다를 수 있습니다. 세그멘테이션은 프로그램의 논리적인 구조에 맞게 메모리를 할당하고 관리할 수 있기 때문에 더 직관적입니다. 하지만 외부 단편화가 발생할 수 있다는 단점이 있습니다.

### Fragmentation 
`Fragmentation`는 메모리가 여러 개의 작은 조각으로 나누어져 비효율적으로 사용되는 현상입니다. 이는 메모리 할당 시 발생할 수 있으며, 메모리 자원의 낭비를 초래할 수 있습니다. 내부 단편화와 외부 단편화로 나뉘어, 각각 다른 방식으로 문제를 일으킬 수 있습니다.

---

## Cache Memory
`Cache Memory`는 CPU와 주 메모리 사이에서 데이터를 임시로 저장하는 고속 메모리입니다. 캐시 메모리는 CPU 내부에 위치하며, 여러 레벨로 구성됩니다. 캐시는 CPU가 자주 접근하는 데이터를 저장하여, CPU와 메모리 간의 속도 차이를 줄여주며, 데이터 로컬리티 원리에 따라 동작합니다. 

[![](\assets\posts\2025-04-23-Memory Operation.md\cache.png)](\assets\posts\2025-04-23-Memory Operation.md\cache.png)

- `Temporal Locality`: 한 번 사용된 데이터는 가까운 시간 내에 다시 사용될 가능성이 높다는 원리
- `Spatial Locality`: 연속적인 메모리 주소에 있는 데이터는 함께 사용될 가능성이 높다는 원리

| 캐시 레벨 | 위치 | 속도 | 용량 |
|-|-|-|-|
| **L1 캐시** | CPU 코어 내에 위치 | 가장 빠름 | 가장 작음 |
| **L2 캐시** | CPU 코어와 가까운 위치 | 빠름 | L1보다 큼 |
| **L3 캐시** | 여러 CPU 코어가 공유하는 공간 | 가장 느림 | 가장 큼 |

### MMU
**MMU(Memory Operation Unit)**는 가상 메모리 시스템에서 가상 주소를 물리 주소로 변환하는 하드웨어 장치입니다. `MMU`는 페이지 테이블을 사용하여 주소 변환을 처리합니다. 

[![](\assets\posts\2025-04-23-Memory Operation.md\mmu.png)](\assets\posts\2025-04-23-Memory Operation.md\mmu.png)

- **페이지 테이블**: 가상 주소와 물리 주소의 매핑을 관리하는 테이블입니다.
- **메모리 보호**: 잘못된 메모리 접근을 방지하여 시스템 안정성을 높입니다.

### TLB
**TLB(Translation Lookaside Buffer)**는 `MMU`와 함께 동작하며, 가상 주소를 물리 주소로 변환하는 캐시입니다. MMU가 페이지 테이블을 조회하는 시간을 줄이기 위해 `TLB`는 자주 사용되는 주소 변환을 저장하고 빠르게 접근할 수 있도록 도와줍니다. TLB는 CPU와 MMU 사이에서 효율적인 주소 변환을 제공합니다.

[![](\assets\posts\2025-04-23-Memory Operation.md\tlb.png)](\assets\posts\2025-04-23-Memory Operation.md\tlb.png)

---

## Swapping
`Swapping`은 물리 메모리가 부족할 때 사용되지 않는 데이터를 하드 드라이브로 이동시키고, 필요한 데이터를 메모리로 가져오는 기법입니다. 시스템 성능이 떨어질 수 있기 때문에, 자주 발생하면 쓰레싱이 발생할 수 있습니다.

[![](\assets\posts\2025-04-23-Memory Operation.md\swapping.png)](\assets\posts\2025-04-23-Memory Operation.md\swapping.png)

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

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
