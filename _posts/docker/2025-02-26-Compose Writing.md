---
title: Compose Writing
category: Docker
tag: [Docker Compose, Docker]
---

> Docker Compose는 여러 개의 Docker 컨테이너를 하나의 설정 파일로 정의하고, 이들 간의 관계를 설정할 수 있게 해줍니다. 특히, 복잡한 애플리케이션을 여러 서비스로 나누어 관리할 때 유용하며, 각 서비스가 필요한 네트워크, 볼륨 등을 설정하고 실행할 수 있습니다.

---

## Basic Structure
Docker Compose 파일은 `yaml` 형식으로 작성되며, 각 서비스와 그에 관련된 설정을 정의합니다. 
```yaml
version: '3'  # Docker Compose 버전

services:  # 서비스 정의 시작
  service_name:  # 서비스 이름
    image: image_name:tag  # 사용할 이미지
    ports:
      - "external_port:internal_port"  # 외부 포트와 내부 포트 연결
    environment:  # 환경 변수 설정
      - ENV_VAR_NAME=value
    volumes:
      - volume_name:/path/in/container  # 볼륨 연결
    networks:
      - network_name  # 네트워크 설정
```

이렇게 구성된 Compose 파일에서 각 서비스는 `image`, `ports`, `volumes와` 같은 설정을 가질 수 있으며, 네트워크와 환경 변수도 지정할 수 있습니다.

---

## Creating Services
Docker Compose를 사용하면, 여러 서비스를 쉽게 정의하고 실행할 수 있습니다. 
예를 들어, 웹 애플리케이션과 데이터베이스를 연결하는 두 개의 서비스를 설정할 수 있습니다. 각 서비스는 독립적으로 구성되며, `docker-compose.yml` 파일에 작성된 설정에 따라 자동으로 실행됩니다.
```yaml
version: '3'

services:
  web:
    image: nginx:latest  # Nginx 웹 서버 사용
    ports:
      - "8080:80"  # 외부 포트 8080과 내부 포트 80 연결
    networks:
      - app-network  # app-network 네트워크에 연결

  db:
    image: postgres:latest  # PostgreSQL 데이터베이스 사용
    environment:
      POSTGRES_USER: example_user
      POSTGRES_PASSWORD: example_password
      POSTGRES_DB: example_db
    volumes:
      - db-data:/var/lib/postgresql/data  # 데이터 저장을 위한 볼륨 설정
    networks:
      - app-network  # app-network 네트워크에 연결

networks:
  app-network:  # 서비스가 연결될 네트워크 정의

volumes:
  db-data:  # 데이터 영속성 보장
```

위 구성에서는 `web` 서비스와 `db` 서비스가 정의되어 있으며, 각각 `Nginx` 웹 서버와 `PostgreSQL` 데이터베이스를 사용합니다.

---

## Connecting Services
Docker Compose의 강력한 기능 중 하나는 서비스 간의 연결입니다. Compose는 각 서비스가 기본적으로 동일한 네트워크에 연결되도록 설정해주므로, 별도로 네트워크 설정을 하지 않아도 됩니다. 예를 들어, `web` 서비스가 `db` 서비스에 접근하려면 `db`라는 서비스 이름을 사용하면 됩니다.

위 예시에서 web 서비스는 db 서비스와 같은 네트워크에 연결되어 있어, db 서비스를 db라는 이름으로 참조할 수 있습니다.
```bash
postgres://example_user:example_password@db:5432/example_db
```

여기서 `db`는 Compose 파일에서 정의한 데이터베이스 서비스 이름입니다. 이와 같이 서비스 이름을 사용하여 쉽게 다른 서비스와 연결할 수 있습니다.

---

## Running Compose
Docker Compose 파일을 작성한 후, 서비스를 실행하려면 `docker-compose` 명령어를 사용합니다.

### up
```bash
docker-compose up -d
```
`docker-compose.yml` 파일에 정의된 모든 서비스를 백그라운드에서 실행합니다. 로컬에 이미지가 없으면 자동으로 다운로드하거나, 필요한 경우 이미지를 빌드합니다.

### down
```bash
docker-compose down
```
실행 중인 모든 서비스를 중지하고 삭제합니다.

---

## References
- [Docker Compose 공식 문서](https://docs.docker.com/compose/)
- [Docker 공식 문서](https://docs.docker.com/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
