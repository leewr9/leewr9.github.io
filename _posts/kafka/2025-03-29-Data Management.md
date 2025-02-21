---
title: Data Management
category: Kafka
tag: [Kafka Connect, Schema Registry, Kafka]
---

> Kafka는 실시간 데이터 처리 및 통합을 위한 강력한 플랫폼으로, 다양한 시스템 간 데이터 흐름을 효율적으로 관리할 수 있는 여러 기능을 제공합니다. 그 중에서도 Schema Registry와 Kafka Connect는 Kafka의 핵심 기능으로, 데이터를 안전하고 일관되게 관리하는 데 중요한 역할을 합니다.

---

## Schema Registry
`Schema Registry`는 Kafka에서 전송되는 데이터의 형식을 관리하고 검증하는 중앙 저장소입니다. 데이터가 올바른 형식과 구조를 따르도록 보장하는 중요한 역할을 하며, Kafka에서의 데이터 흐름이 일관되고 정확하게 처리될 수 있도록 도와줍니다.

[![](\assets\posts\{{ page.name }}\schema-registry.png)](\assets\posts\{{ page.name }}\schema-registry.png)

- 스키마 관리: `Schema Registry`는 각 Kafka 토픽에 대한 스키마를 관리합니다. Producer가 데이터를 전송할 때, 해당 데이터는 지정된 스키마에 맞게 직렬화되고 검증됩니다.
- 버전 관리: 스키마는 시간이 지남에 따라 변화할 수 있습니다. `Schema Registry`는 스키마 버전 관리를 통해 데이터 형식의 변경을 안전하게 처리할 수 있도록 합니다. 
- 스키마 검증
  - `Producer`: 데이터를 보낼 때 `Schema Registry`에 정의된 스키마를 확인하고, 데이터를 전송하기 전에 스키마와 일치하는지 검증합니다. 데이터가 일치하지 않으면 전송되지 않습니다.
  - `Consumer`: Kafka에서 메시지를 수신할 때, `Schema Registry`에서 해당 메시지의 스키마를 조회하여 데이터를 정확하게 역직렬화하고 처리할 수 있습니다. 

---

## Connect
`Kafka Connect`는 Kafka와 외부 시스템 간의 데이터 이동을 간소화하는 데 사용되는 프레임워크입니다. Kafka Connect는 `Source Connector`와 `Sink Connector`를 통해 데이터를 Kafka와 다른 시스템 간에 효율적으로 주고받을 수 있도록 합니다.

[![](\assets\posts\{{ page.name }}\connect.png)](\assets\posts\{{ page.name }}\connect.png)

### Source Connector
`Source Connector`는 외부 시스템의 데이터를 Kafka 토픽으로 스트리밍하는 역할을 합니다. 외부 데이터베이스, 파일 시스템, 메시지 큐 등에서 데이터를 가져와 Kafka로 전송합니다. 주로 읽기 작업을 담당하며, Kafka 토픽에 데이터를 입력하는 역할을 합니다.

```json
{
  "name": "postgres-source-connector",  
  "config": {
    "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",  
    "tasks.max": "1",  
    "topic.prefix": "topic-",  
    "connection.url": "jdbc:postgresql://<postgres-host>:5432/<database>",
    "connection.user": "postgres",
    "connection.password": "postgres",
    "mode": "incrementing",  
    "incrementing.column.name": "id",  
    "poll.interval.ms": "5000",  
    "numeric.mapping": "best_fit",  
    "transforms": "createKey",  
    "transforms.createKey.type": "org.apache.kafka.connect.transforms.ValueToKey",  
    "transforms.createKey.fields": "id",  
    "table.whitelist": "public.source_table"  
  }
}

```
- `topic.prefix`: 토픽 이름에 붙일 접두어 (`topic-source_table`)
- `connection.~`: 데이터베이스 설정
- `mode`: 데이터를 어떻게 가져올지 설정
  - `incrementing `: 증가하는 컬럼 기준 (`id`, `no`)
  - `timestamp `: 컬럼에 저장된 타임스탬프 기준 (`created_at`, `updated_at`)
- `poll.interval.ms`: 커넥터가 데이터를 읽는 간격
- `transforms.~`: 데이터를 메시지의 Key로 변환하는 설정
- `table.whitelist`: 데이터를 읽을 테이블을 지정

### Sink Connector
`Sink Connector`는 Kafka에서 데이터를 소비하여 외부 시스템에 저장하는 역할을 합니다. Kafka 토픽에 쌓인 데이터를 외부 데이터베이스나 파일 시스템, 애플리케이션 등으로 보내는 일을 합니다. 주로 쓰기 작업을 담당하며, Kafka 토픽의 데이터를 소비해 외부 시스템에 저장합니다.

```json
{
  "name": "postgres-sink-connector",  
  "config": {
    "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector", 
    "tasks.max": "1",  
    "topics": "topic-source_table",  
    "connection.url": "jdbc:postgresql://<postgres-host>:5432/<database>",
    "connection.user": "postgres",  
    "connection.password": "postgres", 
    "insert.mode": "insert",  
    "auto.create": "true",  
    "auto.evolve": "true",  
    "pk.mode": "record_key",  
    "pk.fields": "id",  
    "table.name.format": "sink_table"  
  }
}
```
- `topics`: 데이터를 읽을 토픽을 지정
- `connection.~`: 데이터베이스 설정
- `insert.mode`: 데이터를 삽입하는 모드를 지정 (`insert`, `upsert`, `delete`)
- `auto.create`: 대상 테이블이 존재하지 않으면 자동으로 생성
- `auto.evolve`: 데이터 구조나 스키마가 변경되면 테이블을 자동으로 변경
- `pk.~`: primary key로 사용할지 필드 지정
- `table.name.format`: 데이터를 삽입할 테이블의 이름을 지정

```bash
curl -X POST -H "Content-Type: application/json" \
  --data @connector-config.json \
  http://<kafka-connect-host>:<port>/connectors
```
위 명령어를 실행하면, 파일에 정의된 Connector 설정을 `Kafka Connect`에 등록할 수 있습니다.


---

## References
- [Confluent 공식 문서](https://docs.confluent.io/)
- [Kafka 공식 문서](https://kafka.apache.org/documentation/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
