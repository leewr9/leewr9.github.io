---
title: Essential Command
category: Docker
tag: [Docker]
---

> Docker는 명령어로 컨테이너 관리, 이미지 빌드 등 핵심적인 작업을 수행합니다. 명령어는 Docker 환경에서의 작업 흐름을 원활하게 하고, 개발 및 배포에서 필수적으로 활용됩니다. 이를 통해 안정적이고 효율적인 시스템 구축이 가능합니다.

---

## Container

### run
컨테이너를 실행할 때는 `docker run` 명령어를 사용합니다. 여러 옵션을 통해 실행할 수 있습니다.
```bash
docker run <options> <image_name>
# docker container run <options> <image_name>
```

- `-d`: 백그라운드에서 실행
- `--name <container_name>`: 컨테이너 이름 지정
- `-p <host_port>:<container_port>`: 포트 매핑

### ls
실행 중인 컨테이너 목록을 확인하려면 `docker ps` 명령어를 사용합니다.
```bash
docker ps
# docker container ls
```

- `-a`: 종료된 컨테이너까지 포함한 모든 컨테이너 보기

### logs
컨테이너의 로그를 확인하려면 `docker logs` 명령어를 사용합니다.
```bash
docker logs <container_name_or_id>
# docker container logs <container_name_or_id>
```

### stop
실행 중인 컨테이너를 중지하려면 `docker stop` 명령어를 사용합니다.
```bash
docker stop <container_name_or_id>
# docker container stop <container_name_or_id>
```

### start
중지된 컨테이너를 다시 시작하려면 `docker start` 명령어를 사용합니다.
```bash
docker start <container_name_or_id>
# docker container start <container_name_or_id>
```

### restart
컨테이너를 재시작하려면 `docker restart` 명령어를 사용합니다.
```bash
docker restart <container_name_or_id>
# docker container restart <container_name_or_id>
```

### rm
사용하지 않는 컨테이너를 삭제하려면 `docker rm` 명령어를 사용합니다.
```bash
docker rm <container_name_or_id>
# docker container rm <container_name_or_id>
```

### exec
컨테이너 내에서 명령어를 실행하려면 `docker exec` 명령어를 사용합니다.
```bash
docker exec -it <container_name_or_id> <command>
# docker container exec -it <container_name_or_id> <command>
```

- `--user <username_or_uid>`: 옵션으로 특정 사용자로 명령어 실행
```bash
docker exec -it --user root <container_name_or_id> sh # 관리자 권한으로 셸을 실행
```

---

## Image

### images
로컬에 저장된 Docker 이미지를 확인하려면 `docker images` 명령어를 사용합니다.
```bash
docker images
# docker image ls
```

### pull
Docker Hub에서 이미지를 다운로드하려면 `docker pull` 명령어를 사용합니다.
```bash
docker pull <image_name>
# docker image pull <image_name>
```

### build
새로운 Docker 이미지를 빌드하려면 `docker build` 명령어를 사용합니다.
```bash
docker build -t <image_name> <path_to_dockerfile>
# docker image build -t <image_name> <path_to_dockerfile>
```

### rm
사용하지 않는 이미지를 삭제하려면 `docker rmi` 명령어를 사용합니다.
```bash
docker rmi <image_name_or_id>
# docker image rm -t <image_name> <path_to_dockerfile>
```

---

## References
- [Docker 공식 문서](https://docs.docker.com/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
