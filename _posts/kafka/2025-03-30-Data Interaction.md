---
title: Data Interaction
category: Kafka
tag: [ksqlDB, Kafka]
---

> Kafka의 스트리밍 데이터 처리는 실시간 데이터 파이프라인을 구축하고 데이터를 빠르게 분석하는 데 중요한 역할을 합니다. 이를 위해 ksqlDB와 Kafka CLI는 필수적인 도구로 사용됩니다. 두 가지 모두 Kafka 스트리밍 데이터를 효율적으로 관리하고, 실시간으로 데이터를 쿼리하고 처리하는 데 유용합니다

---

## ksqlDB
`ksqlDB`는 실시간 스트리밍 데이터를 SQL로 처리하고 분석할 수 있는 데이터베이스로, Kafka와 통합되어 실시간 데이터 읽기 및 변환이 가능합니다. 또한, 높은 유연성을 제공해 다양한 스트리밍 데이터 처리 요구에 맞게 쉽게 조정할 수 있습니다.

[![](\assets\posts\{{ page.name }}\ksqldb.png)](\assets\posts\{{ page.name }}\ksqldb.png)

### STREAM
`STREAM`은 실시간 데이터 스트리밍을 처리하는 구조입니다.STREAM은 데이터가 지속적으로 흐르는 이벤트로 취급되며, 각 이벤트는 독립적이고 순차적으로 처리됩니다. 새로운 데이터가 들어오면 그때그때 처리되며, 과거 데이터는 변경되지 않고 삭제됩니다.

- 실시간으로 들어오는 이벤트를 처리
- 순차적이고 독립적인 이벤트로 구성
- 각 이벤트는 변경되지 않으며, 실시간 처리에 적합

```sql
CREATE STREAM <stream_name> (
    <field_name> <data_type>,
    -- name STRING,
    -- birth TIMESTAMP,
    -- age INT
    ...
) WITH (
    KAFKA_TOPIC='<kafka_topic>',
    VALUE_FORMAT='<format>'
);

SELECT <fields> FROM <stream_name> EMIT CHANGES;
```

- `KAFKA_TOPIC`: 토픽 이름
- `VALUE_FORMAT`: 데이터 포맷 (`JSON`, `AVRO`, `DELIMITED`, `PROTOBUF`, `KAFKA` 등)
- `EMIT CHANGES`: 실시간으로 결과를 반환

### TABLE
`TABLE`은 상태 저장을 목적으로 하는 구조입니다. TABLE은 키-값 쌍으로 데이터를 저장하며, 각 키에 대해 최신 값만 유지합니다. 즉, 같은 키에 대해 새로운 값이 들어오면 이전 값은 덮어쓰여 최신 상태만 유지됩니다. 

- 상태를 저장하고 최신 값만 유지
- 특정 키에 대한 최신 상태를 관리
- 실시간 상태 추적 및 집계에 적합

```sql
CREATE TABLE <table_name> (
    <field_name> <data_type>,
    ...
) WITH (
    KAFKA_TOPIC='<kafka_topic>',
    VALUE_FORMAT='<format>', -- JSON / AVRO
    KEY='<key_column>'
);

SELECT <fields> FROM <table_name>;
```

- `KAFKA_TOPIC`: 토픽 이름
- `VALUE_FORMAT`: 데이터 포맷 (`JSON`, `AVRO`, `DELIMITED`, `PROTOBUF`, `KAFKA` 등)
- `KEY`: 키 컬럼 (데이터를 구분하는 기준 컬럼)

---

## Console
`Kafka Console`은 Kafka의 데이터를 관리하고 상호작용하는데 사용하는 명령줄 도구입니다. Kafka Console을 사용하면 Kafka 토픽, 소비자, 프로듀서 등을 쉽게 관리할 수 있습니다. 

### producer
`kafka-console-producer`은 사용자로부터 입력 받은 데이터를 지정한 Kafka 토픽에 전송하는 Producer 역할을 합니다. 데이터를 한 줄씩 입력하면, 해당 데이터가 지정된 토픽에 전송됩니다.

```bash
kafka-console-producer --bootstrap-server <kafka_broker> --topic <topic_name>
```

- `--bootstrap-server`: 브로커 주소를 지정
- `--topic`: 데이터를 보낼 토픽의 이름을 지정

### consumer
`kafka-console-producer`는 지정된 Kafka 토픽에서 데이터를 읽어오는 Consumer 역할을 합니다. 지정된 토픽에 존재하는 데이터를 읽어옵니다.

```bash
kafka-console-consumer --bootstrap-server <kafka_broker> --topic <topic_name> --from-beginning
```

- `--bootstrap-server`: 브로커 주소를 지정
- `--topic`: 데이터를 보낼 토픽의 이름을 지정
- `--from-beginning`
  - 지정된 토픽의 데이터를 처음부터 읽어옵니다. 이 옵션을 사용하지 않으면, 기본적으로 새로운 데이터부터 읽게 됩니다.

### topics
`kafka-topics`는 Kafka 클러스터에서 토픽 목록을 확인하거나, 새로운 토픽을 생성하거나, 기존 토픽을 삭제하는 등 토픽과 관련된 모든 관리 작업을 수행할 수 있는 명령어입니다.

- `--list`: 토픽 목록 확인
```bash
kafka-topics --bootstrap-server <kafka_broker> --list
```
- `--describe`: 토픽 확인
```bash
kafka-topics --bootstrap-server <kafka_broker> --describe --topic <topic_name>
```
- `--delete`: 토픽 삭제
```bash
kafka-topics --bootstrap-server <kafka_broker> --delete --topic <topic_name>
```
- `--create`: 토픽 생성
```bash
kafka-topics --bootstrap-server <kafka_broker> --create --topic <topic_name> --partitions <num_partitons> --replication-factor <replication_factor>
```
  - `--topic`: 생성할 토픽의 이름을 지정
  - `--partitions`: 토픽의 파티션 수를 지정
  - `--replication-factor`: 각 파티션에 대한 복제본 수를 지정

---

## References
- [Confluent 공식 문서](https://docs.confluent.io/)
- [Kafka 공식 문서](https://kafka.apache.org/documentation/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
