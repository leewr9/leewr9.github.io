---
title: Virtualization
category: Operating System
tag: [Virtualization, OS, Operating System]
---

> 가상화는 물리적인 하드웨어 자원을 추상화하여, 하나의 물리 서버에서 여러 개의 독립적인 운영체제, 실행 환경을 동시에 실행할 수 있도록 하는 기술입니다. 이를 통해 서버 자원의 효율적인 사용, 유연한 배포, 테스트 환경 격리, 비용 절감 등을 달성할 수 있습니다.

---

## Hardware Virtualization

`Hardware Virtualization`은 물리 서버 위에서 여러 가상 머신을 실행하는 기술입니다. 각 VM은 독립적인 운영체제와 커널을 갖고, 하이퍼바이저가 이를 관리합니다. 하드웨어 가상화에서는 커널 분리가 이루어지며, VM마다 독립적인 환경을 제공합니다.

[![](\assets\posts\2025-08-24-Virtualization.md\hardware.png)](\assets\posts\2025-08-24-Virtualization.md\hardware.png)

### Hypervisor

`Hypervisor`는 하드웨어 가상화 계층에서 가상 머신을 생성하고 관리하는 핵심 소프트웨어입니다. 물리 서버의 CPU, 메모리, 디스크, 네트워크 등 자원을 VM에 할당하고, 각 VM이 독립적인 운영체제와 커널을 사용할 수 있도록 격리하며, VM 간 자원 충돌 방지, 효율적 스케줄링, I/O 처리, 보안 관리까지 담당합니다.

[![](\assets\posts\2025-08-24-Virtualization.md\hypervisor.png)](\assets\posts\2025-08-24-Virtualization.md\hypervisor.png)

- **Type 1**
  - 물리 서버 바로 위에서 실행되며 운영체제 없이 하드웨어를 직접 관리합니다. 높은 성능과 보안을 제공하며 하드웨어를 직접 제어할 수 있지만, 설치와 관리가 다소 복잡합니다.
  - `VMware ESXi`, `Microsoft Hyper-V`, `Xen`
- **Type 2**
  - 기존 호스트 운영체제 위에서 실행되며, 하이퍼바이저가 OS의 자원 관리 기능을 활용해 VM을 관리합니다. 설치가 쉽고 다양한 OS 환경에서 실행 가능하지만, 성능은 Type 1보다 낮고 호스트 OS에 의존합니다.
  - `Oracle VirtualBox`, `VMware Workstation`, `Parallels Desktop`

### Full Virtualization

`Full Virtualization`은 하드웨어를 완전히 가상화하여 게스트 OS를 수정하지 않고 그대로 실행할 수 있는 방식입니다. 하이퍼바이저가 게스트 OS의 명령어를 변환하거나 하드웨어 가상화 기능을 활용해 실행합니다.

- OS 변경 불필요, 높은 호환성
- 거의 모든 운영체제 실행 가능
- 명령어 변환으로 성능 오버헤드 발생
- 하드웨어 요구 높음

### Paravirtualization

`Paravirtualization`은 게스트 OS를 하이퍼바이저와 협력하도록 일부 수정하여 성능을 최적화하는 방식입니다. OS가 하이퍼바이저에 직접 명령을 전달하기 때문에 CPU와 I/O 효율이 향상됩니다.

- 높은 성능과 효율적인 자원 활용
- 하드웨어 가상화 한계 극복 가능
- OS 수정 필요 → 호환성 제한

### Hybrid Virtualization

`Hybrid Virtualization`은 Full과 Paravirtualization의 장점을 결합한 방식으로, 일부 하드웨어 가상화 기능을 활용하면서 게스트 OS의 일부를 수정해 성능과 호환성을 균형 있게 제공합니다.

- 성능과 호환성 균형
- 기존 OS 실행 가능성 유지
- 구현/설정 복잡
- 일부 환경에서는 OS 수정 필요

---

## Desktop Virtualization

`Desktop Virtualization`은 중앙 서버에서 가상 데스크탑 환경을 제공하고, 원격으로 접속하여 사용하는 기술입니다. 각 가상 데스크탑은 독립적인 운영체제와 커널을 가지며, 네트워크를 통해 중앙 서버와 연결됩니다.

[![](\assets\posts\2025-08-24-Virtualization.md\desktop.png)](\assets\posts\2025-08-24-Virtualization.md\desktop.png)

- `VMware Horizon`, `Citrix Virtual Apps and Desktops`, `Microsoft Remote Desktop Services`

---

## Containerization

`Containerization` 또는 `OS-level Virtualization`은 커널을 공유하면서 프로세스 단위로 격리된 환경을 제공하는 기술입니다. VM처럼 운영체제를 새로 설치하지 않고도 여러 격리된 환경을 동시에 실행할 수 있으며, 컨테이너 엔진이 리소스를 관리합니다.

[![](\assets\posts\2025-08-24-Virtualization.md\docker.png)](\assets\posts\2025-08-24-Virtualization.md\docker.png)

- `Docker`, `LXC`, `Podman`

| 구분          | Hardware          | Desktop                          | OS-level               |
| ------------- | ----------------- | -------------------------------- | ---------------------- |
| **실행 환경** | 독립적인 VM 실행  | 중앙 서버에서 가상 데스크탑 제공 | 호스트 OS 위에서 실행  |
| **커널**      | VM마다 독립적     | VM마다 독립적                    | 호스트 OS 커널 공유    |
| **격리 수준** | 매우 높음         | 높음                             | 프로세스 단위 격리     |
| **성능**      | 높음              | 중간                             | 경량 / 빠름            |
| **OS 유무**   | 독립 OS 필요      | 독립 OS 필요                     | 호스트 OS만 필요       |
| **관리/설정** | 하이퍼바이저 필요 | 중앙 관리 서버 필요              | 컨테이너 엔진으로 관리 |

---

## References

- [Wikipedia 공식 문서](https://wikipedia.org/wiki/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
