---
title: Optional Command
category: Docker
tag: [Docker Compose, Docker]
---

> Docker에서 명령어를 활용하여 특정 상황에 맞는 고급 기능을 지원합니다. 이 명령어들은 필수는 아니지만, 복잡한 배포 환경에서 유용하게 사용될 수 있으며, 특정 요구사항에 맞춘 더 세부적인 관리 및 설정을 가능하게 합니다. 이를 통해 보다 유연한 Docker 환경을 구축할 수 있습니다.

---

## Compose

### up

Docker Compose로 정의된 서비스를 시작하려면 `docker compose up` 명령어를 사용합니다.

```bash
docker compose up -d
```

- `-d`: 백그라운드에서 실행
- `-f`: 실행할 파일 지정

### down

Docker Compose로 실행 중인 서비스를 종료하려면 `docker compose down` 명령어를 사용합니다.

```bash
docker compose down
```

- `--volumes`: 연결된 볼륨을 함께 삭제
- `--rmi all`: 사용된 이미지를 모두 삭제
- `--remove-orphans`: 정의되지 않은 서비스의 컨테이너를 삭제

### ps

실행 중인 서비스의 상태를 확인하려면 `docker compose ps` 명령어를 사용합니다.

```bash
docker compose ps
```

### logs

Docker Compose의 로그를 확인하려면 `docker compose logs` 명령어를 사용합니다.

```bash
docker compose logs
```

---

## Network

### ls

Docker의 네트워크를 확인하려면 `docker network ls` 명령어를 사용합니다.

```bash
docker network ls
```

### create

새로운 네트워크를 생성하려면 `docker network create` 명령어를 사용합니다.

```bash
docker network create <network_name>
```

### connect

컨테이너를 특정 네트워크에 연결하려면 `docker network connect` 명령어를 사용합니다.

```bash
docker network connect <network_name> <container_name_or_id>
```

### disconnect

컨테이너를 네트워크에서 연결 해제하려면 `docker network disconnect` 명령어를 사용합니다.

```bash
docker network disconnect <network_name> <container_name_or_id>
```

---

## Volume

### ls

Docker 볼륨을 확인하려면 `docker volume ls` 명령어를 사용합니다.

```bash
docker volume ls
```

### create

새로운 볼륨을 생성하려면 docker volume create 명령어를 사용합니다.

```bash
docker volume create <volume_name>
```

### rm

사용하지 않는 볼륨을 삭제하려면 `docker volume rm` 명령어를 사용합니다.

```bash
docker volume rm <volume_name>
```

---

## References

- [Docker Compose 공식 문서](https://docs.docker.com/compose/)
- [Docker 공식 문서](https://docs.docker.com/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
