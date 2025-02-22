---
title: Message Delivery
category: Kafka
tag: [Kafka]
---

> Apache Kafka는 분산 스트리밍 플랫폼으로, 메시지를 내구성 있게 전송하고 처리할 수 있도록 설계되었습니다. Kafka에서는 메시지의 전달 보장 수준에 따라 Exactly Once, At Least Once, At Most Once라는 세 가지 전송 보장 정책을 제공합니다.

---

## Exactly Once
`Exactly Once`는 메시지가 소비자에게 정확히 한 번만 전달되도록 보장하는 전송 보장 방식입니다. 이 방식은 중복된 메시지를 처리하지 않으므로, 시스템에서 중복 메시지로 인한 부작용을 없애는 데 중요한 역할을 합니다.

- 메시지는 정확히 한 번만 소비자에게 전달됩니다.
- 메시지가 중복으로 처리되지 않도록 보장합니다.

### Producer
```python
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    acks='all',  # 모든 브로커가 메시지를 받았을 때만 응답을 받음
    enable_idempotence=True,  # 중복 방지
    transactional_id='unique_transaction_id'  # 트랜잭션 설정
)

producer.begin_transaction()  # 트랜잭션 시작

try:
    producer.send('test_topic', value=b'Hello, Kafka!')
    producer.commit_transaction()  # 트랜잭션 커밋
    print("Message sent successfully")
except KafkaError as e:
    producer.abort_transaction()  # 오류가 발생하면 트랜잭션 롤백
    print(f"Error sending message: {e}")

producer.close()

```

### Consumer
```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test_topic',
    bootstrap_servers='localhost:9092',
    group_id='test_group',
    enable_auto_commit=True,
    auto_offset_reset='earliest'
)

for message in consumer:
    print(f"Received message: {message.value.decode()}")
```

- 장점: 중복 처리와 데이터 손실을 방지하며, 데이터의 일관성을 보장합니다.
- 단점: 성능 상의 오버헤드가 발생할 수 있으며, 처리 속도가 다소 떨어질 수 있습니다.

---

## At Least Once
`At Least Once`는 메시지가 적어도 한 번 이상 소비자에게 전달된다는 보장입니다. 이 방식에서는 중복된 메시지가 있을 수 있습니다. 즉, 메시지가 여러 번 소비자에게 전달될 수 있지만, 최소한 한 번은 반드시 전달된다는 보장이 있습니다.

- 메시지가 최소 한 번 전달됩니다.
- 메시지 중복이 발생할 수 있습니다.

### Producer
```python
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    acks='all',  # 메시지를 모든 브로커에 기록할 때까지 기다림
    enable_idempotence=False  # 중복을 방지하지 않음
)

producer.send('test_topic', value=b'Hello, Kafka!')
producer.flush() 
producer.close()
```

### Consumer
```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test_topic',
    bootstrap_servers='localhost:9092',
    group_id='test_group',
    enable_auto_commit=False,  # 자동 커밋 끄기
    auto_offset_reset='earliest'
)

for message in consumer:
    print(f"Received message: {message.value.decode()}")
    consumer.commit()  # 메시지를 처리하고 명시적으로 커밋
```
- 장점: 시스템이 일관되게 메시지를 전달하므로, 소비자는 메시지를 놓치지 않게 됩니다.
- 단점: 중복 메시지가 발생할 수 있습니다. 이를 처리하려면 소비자 측에서 중복 제거 로직을 추가해야 합니다.

---

## At Most Once
`At Most Once`는 메시지가 최대 한 번만 전달된다는 보장을 제공합니다. 이 방식에서는 메시지가 전달되지 않거나, 한 번만 전달되며, 중복된 메시지가 전송되지 않도록 보장합니다.

- 메시지가 최대 한 번 전달됩니다.
- 메시지가 전달되지 않거나, 한 번만 전달되므로 메시지 손실이 발생할 수 있습니다.

### Producer
```python
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    acks='1',  # 리더 브로커만 응답
    enable_idempotence=False  # 중복 방지 기능 비활성화
)

producer.send('test_topic', value=b'Hello, Kafka!')
producer.flush() 
producer.close()
```

### Consumer 
```python
from kafka import KafkaConsumer

# 컨슈머 설정
consumer = KafkaConsumer(
    'test_topic',
    bootstrap_servers='localhost:9092',
    group_id='test_group',
    enable_auto_commit=True,  # 자동 커밋 활성화
    auto_offset_reset='earliest'
)

for message in consumer:
    print(f"Received message: {message.value.decode()}")
```

- 장점: 성능이 가장 뛰어나며, 빠른 처리가 가능합니다.
- 단점: 메시지 손실이 발생할 수 있기 때문에 안정성이 중요한 시스템에서는 사용하기 어렵습니다.

---

## Comparison

| 전송 보장 방식   | 설명                                                | 적합한 용도                                      |
|----------------|---------------------------------------------------|------------------------------------------------|
| **Exactly Once** | 메시지가 정확히 한 번만 전달되도록 보장               | 금융 거래와 같은 높은 신뢰성을 요구하는 시스템    |
| **At Least Once** | 메시지가 최소 한 번 전달되도록 보장, 중복 허용 가능     | 대부분의 Kafka 애플리케이션, 데이터 손실 방지    |
| **At Most Once**  | 메시지가 최대 한 번만 전달되도록 보장, 중복 없음       | 성능 우선 시스템, 메시지 손실 허용               |

---

## References
- [Confluent 공식 문서](https://docs.confluent.io/)
- [Kafka 공식 문서](https://kafka.apache.org/documentation/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
