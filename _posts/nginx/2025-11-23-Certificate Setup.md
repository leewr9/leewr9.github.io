---
title: Certificate Setup
category: Nginx
tag: [Certbot, Let's Encrypt, HTTPS, HTTP, Nginx]
---

> Nginx는 HTTP와 HTTPS 프로토콜을 모두 지원하는 서버입니다. 안전한 통신을 위해 HTTPS 설정 시 SSL 인증서를 적용해야 하며, 이를 통해 데이터 암호화와 무결성을 보장할 수 있습니다. 인증서는 발급, 설정, 갱신 등의 과정을 올바르게 관리하는 것이 중요합니다.

---

## Configuration

### HTTP

`HTTP`는 웹 서버가 일반적인 비암호화 트래픽을 처리하는 기본 방식입니다. `80`번 포트로 요청을 받아 정적 파일, API, 프록시 등 다양한 서비스를 제공합니다. 인증서가 필요하지 않으며, 빠르고 간단하게 설정할 수 있습니다.

```nginx
server {
    listen 80;
    server_name example.com;
    location / {
        root /var/www/html;
        index index.html index.htm;
    }
}
```

- `listen` : 지정된 포트로 요청을 수신
- `server_name` : 해당 서버 블록이 처리할 도메인 지정
- `location` : 경로에 대한 요청 처리 블록
- `root` : 웹 루트 디렉터리 경로 지정
- `index` : 기본 인덱스 파일 지정

### HTTPS

`HTTPS`는 `SSL` 인증서를 적용해 암호화된 트래픽을 처리하는 방식입니다.` 443`번 포트로 요청을 받고, 데이터의 보안성과 무결성을 보장합니다. 인증서/개인키 경로 지정, 보안 옵션 설정, 만료/갱신 관리가 필수입니다.

```nginx
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/nginx/ssl/example.com.crt;
    ssl_certificate_key /etc/nginx/ssl/example.com.key;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;

    location / {
        root /var/www/html;
        index index.html index.htm;
    }
}
```

- `ssl_certificate` : 서버가 사용할 공개키 인증서 경로
- `ssl_certificate_key` : 인증서에 대응하는 개인키 경로
- `ssl_protocols` : 허용할 `SSL`/`TLS` 프로토콜 버전 지정
- `ssl_ciphers` : 사용할 암호화 알고리즘 지정
- `ssl_prefer_server_ciphers` : 서버 암호군 우선 선택
- `ssl_session_cache` : `SSL` 세션 캐시 설정
- `ssl_session_timeout` : `SSL` 세션 유지 시간

#### HSTS

**HSTS(HTTP Strict Transport Security)**는 브라우저가 해당 도메인에 대해 일정 기간 `HTTPS` 연결만 허용하도록 지시하는 보안 정책입니다. 이를 통해 **MITM(Man-In-The-Middle)** 공격과 같은 보안 위협을 줄일 수 있습니다

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
```

### Redirect

`Redirect`는 모든 `HTTP` 요청을 `HTTPS`로 강제 이동시키는 설정입니다. SEO와 보안, 사용자 경험을 위해 `301` 리다이렉트를 사용하며, 브라우저가 항상 암호화된 연결을 사용하도록 유도합니다.

```nginx
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}
```

- `return 301 https://$host$request_uri;` : 모든 `HTTP` 요청을 `HTTPS`로 리다이렉트

---

## Certificate

`Certificate`는 `HTTPS` 통신을 위해 필수적인 요소로, 서버의 신원을 검증하고 데이터 암호화를 가능하게 합니다. 올바른 인증서 설정과 관리는 안전한 웹 서비스를 제공하는 데 매우 중요합니다.

- 인증서 발급: `Let's Encrypt`나 CA 인증기관 등에서 공개키, 개인키 파일 발급
- 파일 배치: 서버의 안전한 경로에 저장 (`/etc/nginx/ssl/`)
- 만료일 관리: 자동 갱신 권장, 만료 전 갱신 필수
- 파일 권한: `root`/`nginx` 사용자만 접근 가능하게 설정
- 인증서 종류: `DV`/`OV`/`EV`, **SAN(Subject Alternative Name)** 포함 가능

### Certbot

`Certbot`은 `Let's Encrypt`에서 무료 `SSL` 인증서를 자동으로 발급/갱신/관리해주는 도구입니다. `Nginx`와 연동해 손쉽게 `HTTPS`를 설정할 수 있습니다.

- **새로운 인증서 생성**
  ```bash
  certbot --nginx -d example.com -d www.example.com
  ```
- **기존 인증서 자동 갱신**
  ```bash
  certbot renew
  ```
- **인증서 삭제**
  ```bash
  certbot delete --cert-name example.com
  ```
- **인증서 만료일 등 정보 확인**
  ```bash
  certbot certificates
  ```
- **실제 발급 전 테스트**
  ```bash
  certbot --nginx --dry-run -d example.com
  ```

---

## References

- [Nginx 공식 문서](https://nginx.org/docs/)
- [Let's Encrypt 공식 문서](https://letsencrypt.org/docs/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
