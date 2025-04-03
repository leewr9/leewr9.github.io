---
title: Traffic Management
category: Network
tag: [Load Balancing, Routing, Network]
---

> 네트워크의 성능을 극대화하고 안정성을 보장하는 데 중요한 요소가 바로 트래픽 관리입니다. 라우팅은 데이터 패킷을 적절한 경로로 전달하여 네트워크 효율을 높이고, 로드밸런싱은 서버 간 트래픽을 균등하게 분배하여 과부하를 방지하고 시스템의 가용성과 확장성을 확보합니다. 

---

## Routing
`Routing`은 네트워크 상의 데이터 패킷이 목적지까지 효율적으로 전달될 수 있도록 경로를 선택하는 과정입니다. 

[![](/assets/posts/2025-05-07-Traffic Management.md/routing.png)](/assets/posts/2025-05-07-Traffic Management.md/routing.png)

### Static Routing
`Static Routing`은 네트워크 관리자가 수동으로 경로를 설정하는 방식입니다. 관리자는 라우팅 테이블을 직접 설정하며, 네트워크의 변화에 따라 수동으로 수정해야 합니다. 정적 라우팅은 네트워크가 작거나 변화가 적을 때 유용합니다.

### Dynamic Routing
`Dynamic Routing`은 라우터가 자동으로 네트워크의 상태를 감지하고 최적의 경로를 선택하는 방식입니다. 동적 라우팅 프로토콜은 네트워크의 변화를 실시간으로 반영하여 경로를 조정합니다. 

#### BGP
**BGP(Border Gateway Protocol)**는 인터넷 상에서 자주 사용되는 라우팅 프로토콜입니다. `BGP`는 경로 벡터 방식으로 작동하며, 자율 시스템(AS) 간의 라우팅 정보를 교환합니다. 

- 장점: 큰 네트워크 환경에서 효율적으로 작동
- 단점: 설정과 유지보수가 복잡하고, 네트워크 트래픽이 많음

#### OSPF
**OSPF(Open Shortest Path First)**는 링크 상태 기반의 동적 라우팅 프로토콜입니다. 각 라우터는 자신이 연결된 네트워크 상태를 다른 라우터에 알리고, 모든 라우터는 동일한 네트워크 맵을 기반으로 최단 경로를 계산합니다. 

- 장점: 대규모 네트워크에서 효율적이고 빠르게 경로를 계산
- 단점: 설정이 복잡하고, 더 많은 메모리와 계산 리소스를 필요로 함

#### RIP
**RIP(Routing Information Protocol)**은 거리 벡터 기반의 동적 라우팅 프로토콜입니다. 각 라우터는 자신의 네트워크 상태를 주기적으로 다른 라우터와 공유하여 경로 정보를 갱신합니다. 

- 장점: 구현이 간단하고 설정이 쉬움
- 단점: 네트워크 규모가 커질수록 비효율적이고 성능이 저하됨

---

## Load Balancing
`Load Balancing`은 서버나 네트워크의 부하를 여러 시스템에 고르게 분배하여 성능을 최적화하고, 서비스의 고가용성과 확장성을 제공합니다. 이를 통해 트래픽 증가에 맞춰 서버를 추가하고, 서버가 다운되더라도 다른 서버가 대신 처리하여 서비스를 지속할 수 있습니다.

[![](/assets/posts/2025-05-07-Traffic Management.md/balancing.png)](/assets/posts/2025-05-07-Traffic Management.md/balancing.png)

- `L4 Load Balancer`: OSI 모델의 `Transport Layer`에서 IP 주소와 `TCP/UDP` 포트를 기반으로 트래픽을 분배합니다. 빠르고 간단하지만 요청에 대한 심층 분석은 하지 않습니다.
- `L7 Load Balancer`: OSI 모델의 `Application Layer`에서 HTTP 요청, URL 경로, 헤더, 쿠키 등을 기반으로 트래픽을 분배합니다. 더 정교한 트래픽 관리가 가능하지만, 상대적으로 처리 속도는 느릴 수 있습니다.

### Least Connection
`Least Connection`은 현재 연결 수가 가장 적은 서버에 트래픽을 분배하는 방식입니다. 서버의 연결 수가 적은 서버는 더 적은 부하를 받고 있다는 의미이므로, 트래픽을 해당 서버로 보냅니다.

- 장점: 서버 과부하를 방지하고 부하를 고르게 분배
- 단점: 트래픽 패턴이 불규칙할 경우 부하 분배가 비효율적일 수 있음

### WRR
**WRR(Weighted Round Robin)**은 서버 성능을 반영하여 각 서버에 가중치를 부여한 후, 그 가중치에 비례해서 트래픽을 분배하는 방식입니다. 성능이 더 좋은 서버에는 더 많은 트래픽을 할당하고, 성능이 낮은 서버에는 상대적으로 적은 트래픽을 분배합니다.

- 장점: 고사양 서버에 더 많은 요청을 할당해 성능 차이를 반영
- 단점: 가중치 설정이 부정확하면 비효율적인 트래픽 분배가 발생할 수 있음

### Round Robin DNS
`Round Robin DNS`는 DNS 서버가 클라이언트의 요청에 대해 여러 IP 주소를 순차적으로 반환하여 트래픽을 분배하는 방식입니다. 일반적으로 DNS 레벨에서 동작하기 때문에 간단하게 설정할 수 있습니다.

- 장점: 설정이 간단하고 추가 장비 없이 트래픽 분배가 가능
- 단점: 서버 상태를 체크하지 않아 다운된 서버로도 요청이 갈 수 있음

---

## References
- [Wikipedia 공식 문서](https://wikipedia.org/wiki/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
