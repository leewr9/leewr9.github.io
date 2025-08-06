---
title: Writing Dockerfile
category: Docker
tag: [Dockerfile, Docker]
---

> Docker는 소프트웨어를 컨테이너라는 독립적인 단위로 패키징하여 실행할 수 있는 오픈소스 플랫폼이며, Dockerfile은 Docker 이미지를 자동으로 빌드하기 위해 필요한 명령어를 정의한 파일입니다. 이를 통해 반복적인 설정 과정을 자동화하고, 특정 애플리케이션 환경을 정확하게 재현할 수 있습니다.

---

## Basic Structure

`Dockerfile`은 기본적으로 텍스트 파일로, 각 명령어는 한 줄씩 작성되며, 컨테이너가 시작될 때 어떤 프로세스를 실행할지, 어떤 파일을 포함할지 등을 설정합니다.

```Dockerfile
# 1. 베이스 이미지 지정
FROM <이미지>

# 2. 환경 변수 설정
ENV <변수명>=<값>

# 3. 의존성 설치 및 소프트웨어 추가
RUN <명령어>

# 4. 작업 디렉토리 설정
WORKDIR <디렉토리>

# 5. 파일 복사
COPY <소스> <대상>

# 6. 컨테이너 실행 명령어 설정
ENTRYPOINT ["실행할 프로그램"]
CMD ["옵션"]
# CMD ["실행할 프로그램", "옵션"]
```

각 항목은 Docker 이미지의 빌드를 구성하는 중요한 부분으로, 필요한 경우 추가적인 명령어를 삽입할 수 있습니다.

### FROM

`Dockerfile`의 첫 번째 명령어로, 사용할 베이스 이미지를 정의합니다.
다른 명령어들이 실행될 기반 환경을 설정하는 중요한 명령입니다.

```Dockerfile
FROM ubuntu:20.04
```

이 명령어는 `Ubuntu 20.04` 이미지를 사용하여 Docker 이미지를 빌드하도록 합니다.

### RUN

`RUN` 명령어는 컨테이너 안에서 명령을 실행합니다.
주로 필요한 패키지 설치나 애플리케이션 설정을 위해 사용됩니다.

```Dockerfile
RUN apt-get update && apt-get install -y python3 python3-pip
```

이 명령어는 `apt-get`을 사용하여 `python3`와 `pip`을 설치합니다.

### COPY

`COPY` 명령어는 로컬 시스템의 파일을 Docker 컨테이너 내부로 복사할 때 사용합니다.
`COPY <소스> <대상>` 형식으로 작성되며, 소스는 로컬 경로, 대상은 컨테이너 내부의 경로입니다.

```Dockerfile
COPY . /app
```

이 명령어는 현재 디렉토리의 모든 파일을 `/app` 디렉토리로 복사합니다.

### WORKDIR

`WORKDIR` 명령어는 작업 디렉토리를 설정하는 명령어입니다. 이후 실행될 명령어들은 이 디렉토리에서 실행됩니다.

```Dockerfile
WORKDIR /app
```

이 명령어는 작업 디렉토리를 `/app`으로 설정합니다.

### ENTRYPOINT

`ENTRYPOINT`는 Docker 컨테이너가 실행될 때 기본적으로 실행되는 명령어를 설정하는 데 사용됩니다. 주로 컨테이너 실행 시 필요한 주요 프로세스를 정의하는 데 사용되며, 이 명령어로 설정된 프로세스는 컨테이너가 종료될 때까지 실행됩니다.

```Dockerfile
ENTRYPOINT ["python", "app.py"]
```

이 명령어는 컨테이너 실행 시 항상 `python app.py` 명령을 실행하게 됩니다.

### CMD

`CMD`는 ENTRYPOINT가 없을 경우 기본적으로 실행될 명령어를 설정하거나, ENTRYPOINT와 함께 실행될 인자를 설정합니다. CMD는 덧붙여지는 인자 또는 기본 실행 명령어로 사용됩니다.

```Dockerfile
CMD ["python", "app.py"]
```

컨테이너를 실행하면 `python app.py`가 기본으로 실행됩니다.

```Dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

이 경우, `ENTRYPOINT`는 항상 `python`을 실행하고, `CMD`는 `app.py`라는 인자를 넘깁니다.
만약 컨테이너 실행 시 다른 인자를 넘긴다면, CMD의 인자는 덮어쓰여지고 새로운 인자가 사용됩니다.

---

## Advanced Configuration

`Dockerfile`에서는 컨테이너의 동작을 세밀하게 설정하는 데 필요한 명령어도 존재하며, 이 설정들은 환경 변수 설정, 컨테이너 포트 노출, 지속적인 데이터 저장을 위한 볼륨 관리 등 다양한 기능을 다룹니다.

### ENV

`ENV` 명령어는 컨테이너 내에서 사용할 환경 변수를 설정하는 데 사용됩니다. 이를 통해 애플리케이션 설정값을 Dockerfile에 미리 정의하고, 실행 시 필요한 값을 전달할 수 있습니다.

```Dockerfile
ENV APP_ENV=production
```

이 명령어는 `APP_ENV`라는 환경 변수를 `production`으로 설정합니다.

### EXPOSE

`EXPOSE` 명령어는 컨테이너에서 외부와 통신할 포트를 설정합니다. 실제로 포트를 개방하는 것은 docker run 명령어에서 -p 옵션을 사용하여 설정합니다. 하지만 EXPOSE는 어떤 포트를 사용할지 명시적으로 알려주는 역할을 합니다.

```Dockerfile
EXPOSE 8080
```

이 명령어는 컨테이너가 `8080` 포트를 사용할 것임을 알립니다.

### VOLUME

`VOLUME` 명령어는 컨테이너와 호스트 간의 데이터를 공유하거나, 데이터를 지속적으로 저장하기 위한 볼륨을 생성합니다. 이 명령어를 통해 데이터의 지속성을 보장할 수 있습니다.

```Dockerfile
VOLUME ["/data"]
```

이 명령어는 /data 디렉토리를 볼륨으로 설정하여 컨테이너와 호스트 간에 데이터를 공유할 수 있게 합니다.

### ADD

`ADD` 명령어는 호스트 시스템의 파일이나 디렉토리를 컨테이너로 복사하거나, URL에서 파일을 다운로드하여 컨테이너 내에 추가하는 데 사용됩니다. 또한 압축된 파일을 자동으로 압축 해제할 수도 있습니다.

```Dockerfile
ADD https://example.com/myfile.tar.gz /app/
```

이 명령어는 `https://example.com/myfile.tar.gz` URL에서 `myfile.tar.gz` 파일을 다운로드하여 컨테이너의 `/app/` 디렉토리로 복사합니다.

### USER

USER 명령어는 컨테이너 내에서 명령어를 실행할 사용자를 설정합니다. 이 명령어는 보안을 강화하고, 권한 제어가 필요한 경우 유용하게 사용됩니다.

```Dockerfile
USER nobody
```

이 명령어는 이후 실행되는 명령어들이 `nobody` 사용자 권한으로 실행되도록 설정합니다.

### ARG

`ARG` 명령어는 Docker 이미지 빌드 시 사용될 변수를 설정합니다. ARG는 빌드 과정에서만 유효하며, 이미지를 실행하는 데는 영향을 미치지 않습니다.

```Dockerfile
ARG VERSION=1.0
```

이 명령어는 `VERSION`이라는 빌드 변수에 기본값 `1.0`을 설정합니다. docker build 명령어에서 `--build-arg` 옵션을 통해 다른 값을 지정할 수도 있습니다.

---

## Python Dockerfile

```Dockerfile
# Python 베이스 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 로컬 파일을 컨테이너로 복사
COPY . /app

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 컨테이너 실행 시 기본 명령어 설정
CMD ["python", "app.py"]
```

- FROM: Python 3.9-slim 이미지를 사용하여 기본 이미지를 설정합니다.
- WORKDIR: /app 디렉토리를 작업 디렉토리로 설정합니다.
- COPY: 로컬 시스템에서 현재 디렉토리의 파일을 /app 디렉토리로 복사합니다.
- RUN: requirements.txt에 정의된 의존성 라이브러리들을 설치합니다.
- CMD: 컨테이너 실행 시 python app.py 명령어를 자동으로 실행합니다.

### Usage

```bash
# Dockerfile

docker build -t my-python-app .
# Sending build context to Docker daemon  12.34kB
# Step 1/5 : FROM python:3.9-slim
#  ---> 7a2d95b47db2
# ...
# Step 5/5 : CMD ["python", "app.py"]
#  ---> Running in abc456789xyz
# Removing intermediate container abc456789xyz
#  ---> 9d1234f5a678
# Successfully built 9d1234f5a678
# Successfully tagged my-python-app:latest
```

```bash
docker run -d --name python-app my-python-app
```

위 명령어는 `my-python-app`이라는 이름으로 이미지를 빌드하고, 이를 기반으로 `python-app` 컨테이너를 실행합니다.

---

## References

- [Docker 공식 문서](https://docs.docker.com/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
