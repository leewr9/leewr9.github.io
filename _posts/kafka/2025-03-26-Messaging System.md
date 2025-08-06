---
title: Messaging System
category: Kafka
tag: [Zookeeper, Broker, Kafka]
---

> Kafka는 고성능 분산 메시징 시스템으로, 생산자(Producer)와 소비자(Consumer) 간에 데이터를 효율적으로 전달합니다. Kafka 클러스터는 여러 브로커, 주키퍼, 컨트롤러로 구성되며, 각 구성 요소는 데이터를 안정적으로 처리하고 확장성과 내구성을 제공합니다.

---

## Broker

`Broker`는 데이터를 저장하고 관리하는 서버입니다. 여러 개의 브로커가 모여서 Kafka 클러스터를 구성하며, 각 브로커는 데이터를 분산 저장하고, 클라이언트(Producer, Consumer)의 요청을 처리합니다.

### Controller

Controller는 Kafka 클러스터 내에서 중요한 메타데이터와 브로커 상태를 관리하는 역할을 담당하는 브로커입니다.

- 리더 선출: 파티션 리더 장애 발생 시 새로운 리더를 선출하여 데이터의 일관성을 유지
- ISR 관리: 정상적인 **ISR(In-Sync Replicas)** 목록을 유지하여 복제본 상태를 모니터링
- 브로커 모니터링: 브로커 추가나 제거 시 이를 반영하여 메타데이터를 업데이트
- 메타데이터 관리: 클러스터 내 `Topic` 및 `Partition`을 관리하고 업데이트

### Management

[![](\assets\posts\2025-03-26-Messaging System.md\management.png)](\assets\posts\2025-03-26-Messaging System.md\management.png)

#### Zookeeper

`Zookeeper`는 Kafka 클러스터의 메타데이터를 관리하는 분산 시스템으로, 주로 브로커 간의 조정 및 상태 모니터링을 담당합니다.

- 브로커 관리: 클러스터 내 활성 `Broker`의 상태를 추적하고 장애 발생 시 감지
- 컨트롤러 선출: 브로커 중 하나를 클러스터 `Controller`로 선출
- 메타데이터 저장: `Topic`, `Partition`, `Replica`에 대한 정보를 저장하여 클러스터 내 일관성 유지

#### KRaft

**KRaft(Kafka Raft)**는 Zookeeper 없이 Kafka가 직접 메타데이터를 관리하는 방식으로, Kafka 브로커 간의 동기화와 컨트롤러 선출을 Raft 프로토콜을 통해 처리합니다.

- Raft 프로토콜: Kafka 내부에서 직접 `Controller`를 선출하고 메타데이터를 동기화
- 빠른 장애 복구: `Zookeeper`를 제거하여 성능 향상과 클러스터 관리 간소화
- 확장성: 대규모 클러스터에서의 안정성과 성능 최적화

---

## Data Management

Kafka는 데이터를 여러 서버에 분산하여 저장하고, 데이터가 안전하게 보관될 수 있도록 복제합니다. 또한, 새로운 데이터가 추가될 때마다 저장 공간을 관리하며, 오래된 데이터는 설정에 따라 자동으로 삭제되거나 정리됩니다.

### Replica

Kafka는 데이터를 여러 브로커에 복제하여 가용성과 내구성을 높입니다. 각 파티션에는 리더와 여러 팔로워가 있으며, 리더가 데이터를 처리합니다. **ISR(In-Sync Replica)**는 리더와 동기화된 팔로워들로, 리더가 장애를 겪으면 그 중 하나가 새로운 리더가 될 수 있습니다.

[![](\assets\posts\2025-03-26-Messaging System.md\replica.png)](\assets\posts\2025-03-26-Messaging System.md\replica.png)

- `Leader`: 모든 클라이언트의 읽기 및 쓰기 요청을 처리하는 파티션
- `Follower`: 리더 파티션의 데이터를 복제하여 고가용성을 보장하는 파티션

```python
from kafka import KafkaAdminClient
from kafka.admin import NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id="test-client"
)

# 토픽 생성
topic = NewTopic(
    name="test-topic",
    num_partitions=1,  # 파티션 수
    replication_factor=3  # 레플리카 수 (각 파티션에 3개의 복제본 생성)
)

admin_client.create_topics(new_topics=[topic])
```

### Segment

`Segment`는 파티션 내 로그 파일을 일정 크기나 시간 단위로 분할하여 저장하는 개념입니다. 각 파티션은 로그 파일이 일정 크기나 일정 시간이 지나면 새로운 Segment로 분할됩니다.

[![](\assets\posts\2025-03-26-Messaging System.md\segment.png)](\assets\posts\2025-03-26-Messaging System.md\segment.png)

- 세그먼트 생성: 일정 크기(예: 1GB)나 시간(예: 7일) 후 새 로그 파일 생성
- 메시지 기록: 최신 로그 파일에 메시지 추가
- Retention 정책: 설정된 기간/크기 후 자동 삭제 또는 정리

#### Compaction

`Compaction`은 Kafka에서 중복된 키를 가진 메시지를 정리하는 과정입니다. 동일한 키를 가진 여러 메시지가 있을 때, 가장 최신 메시지만 남기고 나머지는 삭제됩니다. 이를 통해 Kafka는 저장 공간을 절약하고, 최신 상태의 데이터만 유지합니다.

[![](\assets\posts\2025-03-26-Messaging System.md\compaction.png)](\assets\posts\2025-03-26-Messaging System.md\compaction.png)

### Acknowledgment

`Acknowledgment`는 메시지가 성공적으로 전송되었는지를 확인하는 응답입니다. Kafka에서는 프로듀서가 메시지를 브로커에 보낸 후, 그 메시지가 제대로 처리되었는지 확인하기 위해 사용합니다.

```python
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    acks="all",  # 리더와 모든 팔로워가 데이터를 수신한 후 응답 반환
    retries=5  # 전송 실패 시 재시도
)

topic = "test-topic"
for i in range(10):
    key = f"key-{i}".encode()
    value = f"message-{i}".encode()
    producer.send(topic, key=key, value=value)
    print(f"Produced: key={key}, value={value}")

producer.flush()
producer.close()
```

- `acks="all"`: 리더와 모든 팔로워가 데이터를 받은 후 응답 (높은 안정성).
- `acks="1"`: 리더가 데이터 받으면 응답 (성능 최적화, 일부 데이터 손실 가능).
- `acks="0"`: 응답을 기다리지 않음 (가장 빠르지만 데이터 손실 위험).

---

## References

- [Confluent 공식 문서](https://docs.confluent.io/)
- [Kafka 공식 문서](https://kafka.apache.org/documentation/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
