---
title: Processing Flow
category: Kafka
tag: [Consumer, Producer, Kafka]
---

> Kafka는 분산 메시지 시스템으로, 프로듀서가 데이터를 파티션에 분배하고, 컨슈머가 그 데이터를 읽는 방식으로 메시지를 전달합니다. 컨슈머는 파티션의 오프셋을 통해 데이터를 읽고, 이를 처리한 후 오프셋을 커밋하여 메시지의 순서와 중복 처리 문제를 관리합니다

---

## Producer
`Producer`는 데이터를 **토픽(Topic)**에 전송하며, 이를 **파티션(Partition)**에 저장합니다. 메시지는 **키(Key)**를 기반으로 특정 파티션에 할당되며, **오프셋(Offset)**을 통해 순서를 유지합니다. 또한, 데이터를 전송하기 전에 `Serialization`를 통해 바이트 형태로 변환합니다.

[![](\assets\posts\2025-02-12-Processing Flow\producer.png)](\assets\posts\2025-02-12-Processing Flow\producer.png)

```python
from kafka import KafkaProducer

# Kafka 프로듀서 설정
producer = KafkaProducer(bootstrap_servers="localhost:9092",
                         key_serializer=str.encode,
                         value_serializer=str.encode)

# 메시지 보내기 (키 기반 분배)
key = "user-1"
value = "Message for user-1"
producer.send("user_topic", key=key, value=value)

# 전송 완료 후 종료
producer.flush()
producer.close()
```

### Partitioner
`Partitioner`는 프로듀서가 메시지를 보낼 때 어떤 파티션에 저장할지를 결정하는 역할을 합니다. 키가 있는 경우에는 해시 기반으로 파티션이 선택되지만, 키가 없는 경우에는 기본 파티셔너가 적용됩니다.

```python
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092",
                         key_serializer=str.encode,
                         value_serializer=str.encode)

# 메시지 보내기 (키 없는 경우)
value = "Message without key"
producer.send("user_topic", value=value)

producer.flush()
producer.close()
```

- `RoundRobinPartitioner`: 모든 파티션에 메시지를 순차적으로 분배하여 부하를 균등하게 나누는 방식 (Kafka 2.4 이전)
- `UniformStickyPartitioner`: 여러 개의 메시지를 같은 파티션에 배치한 후 일정량이 되면 다른 파티션으로 전환하는 방식 (Kafka 2.4 이상)

---

## Consumer
`Consumer`는 **토픽(Topic)**에서 데이터를 읽고, **오프셋(Offset)**을 통해 메시지의 순서를 추적합니다. 메시지를 읽을 때마다 오프셋이 증가하며, 처리된 데이터는 **커밋(Commit)**을 통해 저장됩니다. 또한, 전송된 데이터를 사용하기 전에 `Deserialization`하여 원래 형식으로 변환합니다.

[![](\assets\posts\2025-02-12-Processing Flow\consumer.png)](\assets\posts\2025-02-12-Processing Flow\consumer.png)

### Consumer Group
`Consumer Group`은 여러 개의 컨슈머가 하나의 그룹으로 묶여 동일한 토픽의 메시지를 분배받아 처리하는 방식입니다. 카프카에서는 각 파티션을 Consumer Group 내의 단 하나의 컨슈머에게만 할당하여, 데이터의 병렬 처리와 메시지 순서를 보장합니다.

[![](\assets\posts\2025-02-12-Processing Flow\consumer-group.png)](\assets\posts\2025-02-12-Processing Flow\consumer-group.png)

- 파티션 할당
  - 각 파티션은 `Consumer Group` 내의 단 하나의 컨슈머에게만 할당됩니다. 이를 통해 동일한 파티션의 메시지는 중복 처리되지 않으며, 각 컨슈머는 자신에게 할당된 파티션만 처리합니다.
- 리밸런싱
  - 컨슈머가 그룹에 추가되거나 삭제되면, 카프카는 자동으로 `Rebalancing`을 수행하여 파티션을 다른 컨슈머에게 재배치합니다.

```python
from kafka import KafkaConsumer

# Kafka 컨슈머 설정
consumer = KafkaConsumer("user_topic",
                         group_id="consumer-group-1",  # 컨슈머 그룹 설정
                         bootstrap_servers="localhost:9092",
                         key_deserializer=bytes.decode,
                         value_deserializer=bytes.decode)

# 메시지 읽기
for message in consumer:
    print(f"Received message: {message.value} at offset {message.offset}")
```

### Auto Commit
Kafka는 기본적으로 일정 주기마다 자동으로 오프셋을 커밋합니다. 이는 간단하지만, 컨슈머가 처리 중인 메시지가 커밋되기 전에 실패할 경우 메시지가 중복으로 처리될 위험이 있습니다.

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer("user_topic",
                         group_id="commit-consumer-group",
                         bootstrap_servers="localhost:9092",
                         key_deserializer=bytes.decode,
                         value_deserializer=bytes.decode)

for message in consumer:
    print(f"Received message: {message.value} at offset {message.offset}")
```

### Manual Commit
`enable_auto_commit`을 설정하면, 컨슈머는 메시지를 처리한 후에 오프셋을 명시적으로 커밋해야 합니다. 이 방식은 실패 시 메시지를 중복 처리하지 않도록 보장할 수 있지만, 커밋을 적절히 관리하는 로직이 필요합니다.

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer("user_topic",
                         group_id="manual-commit-group",
                         bootstrap_servers="localhost:9092",
                         enable_auto_commit=False,  # 자동 커밋 비활성화
                         key_deserializer=bytes.decode,
                         value_deserializer=bytes.decode)

for message in consumer:
    print(f"Received message: {message.value} at offset {message.offset}")

    # 수동으로 오프셋 커밋
    consumer.commit()
```


### Auto Offset
`auto_offset_reset`은 컨슈머가 읽을 수 있는 오프셋이 없거나, 오프셋이 더 이상 유효하지 않은 경우(예: 처음 실행할 때 또는 오프셋이 삭제된 경우) 어떤 방식으로 데이터를 읽을지를 설정하는 옵션입니다. 

- `earliest`: 컨슈머가 읽을 수 있는 오프셋이 없으면, 가장 오래된 메시지부터 처리 (처음부터 데이터를 처리하고 싶을 때 사용)
- `latest`: 오프셋이 없으면 가장 최신 메시지부터 처리 (새로운 메시지만 처리하고 싶을 때 사용)

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer("user_topic",
                         group_id="test-consumer-group",
                         bootstrap_servers="localhost:9092",
                         key_deserializer=bytes.decode,
                         value_deserializer=bytes.decode,
                         auto_offset_reset='earliest')  # 가장 오래된 메시지부터 처리

for message in consumer:
    print(f"Received message: {message.value} at offset {message.offset}")
```

---

## References
- [Kafka 공식 문서](https://kafka.apache.org/documentation/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
