---
title: Network Protocol
category: Computer
tag: [Topology, Layer, Network]
---

> 네트워크는 여러 컴퓨터나 장치들이 서로 연결되어 데이터를 주고받을 수 있도록 해주는 시스템입니다. 이 시스템은 단순히 물리적 연결을 넘어서, 데이터와 자원의 공유를 가능하게 하여 다양한 서비스와 기능을 제공합니다.

---

## Layer Model

### OSI
**OSI(Open Systems Interconnection)** 모델은 네트워크 통신을 7개의 계층으로 나누어 각 계층이 독립적으로 작동하면서도 전체적으로 협력하여 통신을 이루게 합니다. `OSI` 모델은 네트워크에서 발생하는 다양한 문제를 해결하기 위해 각 계층을 분리하여 구조화한 모델로, 네트워크 프로토콜을 설계하고 문제를 해결하는 데 유용합니다.

[![](/assets/posts/2025-04-27-Network Protocol.md/osi.png)](/assets/posts/2025-04-27-Network Protocol.md/osi.png)

- `Physical Layer`: 물리적 전송 담당
- `Data Link Layer`: 데이터 오류 감지 및 프레임 생성 담당
- `Network Layer`: 데이터 라우팅 담당
- `Transport Layer`: 데이터 정확한 전달 보장
- `Session Layer`: 세션 관리 및 연결 설정
- `Presentation Layer`: 데이터 형식 및 인코딩 처리
- `Application Layer`: 사용자와 응용 프로그램 서비스 지원

### TCP/IP
`TCP/IP` 모델은 `OSI` 모델을 간소화한 4계층 모델로, 인터넷 프로토콜을 기준으로 네트워크 통신을 분류합니다. TCP/IP는 실제로 인터넷을 구성하는 주요 프로토콜이며, OSI 모델에 비해 좀 더 간단한 구조를 가지고 있습니다.

[![](/assets/posts/2025-04-27-Network Protocol.md/tcpip.png)](/assets/posts/2025-04-27-Network Protocol.md/tcpip.png)

- `Link Layer`: 물리적 전송 담당
- `Internet Layer`: IP 주소 기반 라우팅 담당
- `Transport Layer`: 데이터 전송 (TCP, UDP 사용)
- `Application Layer`: 사용자 및 응용 프로그램 서비스 지원

---

## Switching

### Packet
`Packet` 교환 방식은 데이터를 작은 패킷으로 나누어 네트워크를 통해 전송하는 방식입니다. 각 패킷은 독립적으로 전달되며, 목적지에서 다시 원래의 데이터로 재조합됩니다. 이는 네트워크 자원을 효율적으로 사용하며, 장애 발생 시 복구가 용이합니다.

[![](/assets/posts/2025-04-27-Network Protocol.md/packet.gif)](/assets/posts/2025-04-27-Network Protocol.md/packet.gif)

- 장점: 네트워크 자원의 효율적 사용과 장애에 대한 강한 내성을 가지고 있습니다.
- 단점: 패킷 손실이 있을 경우 재전송이 필요하며, 패킷 순서가 바뀔 수 있습니다.

### Circuit
`Circuit` 교환 방식은 데이터 전송을 위해 통신 경로를 전용으로 설정하여 데이터를 보내는 방식입니다. 주로 전화망에서 사용되며, 전용 경로가 할당되므로 일정한 품질의 데이터 전송이 보장됩니

- 장점: 데이터 전송 품질이 일정하고, 패킷 손실이 없습니다.
- 단점: 전용 경로를 사용하므로 자원을 낭비할 수 있습니다.

---

## Topology
`Topology`는 장치들이 서로 연결되는 방식을 의미합니다. 네트워크의 성능, 확장성, 유지보수 비용에 영향을 주므로, 목적에 따라 적절한 구조를 선택해야 합니다.

[![](/assets/posts/2025-04-27-Network Protocol.md/topology.png)](/assets/posts/2025-04-27-Network Protocol.md/topology.png)

| 종류 | 설명 | 장점 | 단점 |
|-|-|-|-|
| **Ring** | 노드들이 원형으로 연결되어 데이터가 한 방향이나 양방향으로 전달됨 | 데이터 충돌 없음 | 단일 노드 장애 시 네트워크 단절 가능 |
| **Line** | 노드들이 직선 형태로 연결됨 | 구현 간단 | 중간 노드 장애 시 전체 네트워크 단절 가능 |
| **Mesh** | 노드들이 여러 경로로 서로 연결됨 | 장애에 강함 | 설치 비용 및 복잡성 증가 |
| **Tree** | 여러 개의 스타 토폴로지를 계층적으로 연결 | 확장성 우수 | 상위 노드 장애 시 하위 노드 영향 |
| **Star** | 중앙 허브를 통해 모든 노드가 연결됨 | 관리 용이 | 중앙 장애 시 전체 네트워크 마비 가능 |
| **Bus** | 하나의 메인 케이블에 모든 노드가 연결됨 | 설치 비용 저렴 | 단일 장애 발생 시 전체 네트워크 영향 |
| **Fully Connected** | 모든 노드가 서로 직접 연결됨 | 신뢰성 최고 | 비용과 자원 비효율적 |

---

## References
- [Wikipedia 공식 문서](https://wikipedia.org/wiki/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
