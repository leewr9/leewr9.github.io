---
title: Structure Configuration 
category: Nginx
tag: [Nginx]
---

> Nginx는 고성능 웹 서버이자 리버스 프록시, 로드 밸런서, 캐시 서버로 널리 사용되는 오픈소스 소프트웨어입니다. 다양한 프로토콜 지원과 비동기 이벤트 기반 아키텍처 덕분에 높은 동시성 처리 능력을 자랑하며, 정적 파일 서비스, API 게이트웨이, 로드 밸런싱 등 다양한 용도로 활용됩니다.

---

## Nginx

`Nginx`는 `HTTP`, `HTTPS`, `SMTP`, `POP3`, `IMAP` 등 다양한 프로토콜을 지원하는 웹 서버입니다. 가벼운 구조와 높은 동시 처리 성능 덕분에 정적 파일 서비스, 리버스 프록시, API Gateway, 로드 밸런싱 등 다양한 용도로 활용됩니다.

- 비동기 이벤트 기반 아키텍처로 높은 동시성 처리
- 정적 파일 서비스, 리버스 프록시, 로드 밸런서, 캐시 서버 등 다양한 역할
- `Apache` 대비 가볍고 빠른 성능

---


## Architecture

`Nginx`의 구조는 `Master` 프로세스 모델을 기반으로 하며, 각 `Worker` 프로세스가 클라이언트 요청을 비동기적으로 처리합니다. 정적 파일 서비스, 리버스 프록시, SSL/TLS, 로드 밸런싱, 캐싱, 압축, 리다이렉트 등 다양한 기능을 제공합니다.

[![](\assets\posts\2025-11-16-Structure Configuration.md\architecture.png)](\assets\posts\2025-11-16-Structure Configuration.md\architecture.png)

### Master Process
`Master Process`는 Nginx의 전체 운영을 관리하는 프로세스입니다. 설정 파일을 로드하고, 워커 프로세스를 제어하며, 서버의 안정적인 운영을 책임집니다. 

- Worker 프로세스 생성/종료/재시작을 담당
- 설정 변경 시에 무중단으로 `Worker` 교체
- 로그 파일 관리, 신호 처리 등 전체 운영

### Worker Process
`Worker Process`는 실제 클라이언트 요청을 처리하는 프로세스입니다. 비동기 이벤트 기반으로 여러 연결을 동시에 효율적으로 처리합니다.

- 각 프로세스는 독립적으로 동작하며, CPU 코어에 맞춰 여러 개가 생성
- 장애 발생 시 `Master`가 자동으로 새로운 `Worker`를 생성해 복구
- 리소스 분배, 요청 큐 관리, Keep-Alive 등 고성능 네트워킹을 담당


---

## Configuration

`Nginx`의 설정 파일은 블록 구조로 되어 있으며, 서버/리버스 프록시/로드밸런싱 등 다양한 역할을 쉽게 설정할 수 있습니다. `nginx.conf` 파일을 통해 설정을 관리합니다.

### HTTP Server

```nginx
http {
    server {
        listen 80;
        server_name example.com;
        location / {
            root /var/www/html;
            index index.html index.htm;
        }
    }
}
```

### Reverse Proxy

```nginx
http {
    server {
        listen 80;
        server_name api.example.com;
        location / {
            proxy_pass http://localhost:5000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
```

### Load Balancer

```nginx
http {
    upstream backend {
        server backend1.example.com;
        server backend2.example.com;
    }

    server {
        listen 80;
        server_name www.example.com;
        location / {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
```

---

## References

- [Nginx 공식 문서](https://nginx.org/docs/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
