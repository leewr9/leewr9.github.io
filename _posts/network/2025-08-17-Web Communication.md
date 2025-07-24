---
title: Web Communication
category: Network
tag: [HTTPS, HTTP, Network]
---

> 웹에서는 사용자와 서버 간에 다양한 정보가 실시간으로 오가며, 이 과정은 정해진 규칙과 절차에 따라 이루어집니다. 이런 규칙들은 데이터가 올바르게 전달되고, 필요한 경우 보안이 유지되도록 도우며, 안정적이고 효율적인 정보 교환은 원활한 웹 서비스 제공의 핵심 요소입니다.

---

## HTTP
**HTTP(HyperText Transfer Protocol)**는 클라이언트와 서버 간 웹 데이터 전송을 위한 기본 프로토콜로, 초기 텍스트 기반에서 시작해 상태 코드와 헤더를 도입하며 통신 제어와 확장성을 강화했고, 성능과 보안을 개선하며 지속적으로 발전해 왔습니다.

### HTTP/0.9
`HTTP/0.9`는 1991년 최초로 등장한 HTTP 버전으로, `GET` 요청 하나만 지원하며 헤더와 상태 코드가 없는 매우 단순한 프로토콜입니다. 오늘날에는 거의 사용되지 않습니다.

- 단일 GET 요청 지원
- 헤더, 상태 코드 없음
- 텍스트 데이터 전송만 가능

### HTTP/1.0
`HTTP/1.0`은 1996년 표준화된 버전으로 헤더와 상태 코드를 도입하여 통신을 좀 더 유연하게 만들었으나, 매 요청마다 새 TCP 연결을 만드는 비효율적 구조였습니다.

- 상태 코드 및 헤더 도입
- 비연결형 (요청마다 새 연결)
- 기본적인 캐싱 지원 및 콘텐츠 협상

### HTTP/1.1
`HTTP/1.1`은 1997년에 발표되어 현재까지 가장 많이 사용되는 버전입니다. 연결 재사용, 파이프라이닝, 다양한 확장 헤더와 상태 코드, 부분 콘텐츠 요청 지원 등 성능과 유연성을 크게 높였습니다.

- 기본 연결 재사용 (Persistent Connection)
- 파이프라이닝 지원 (제한적)
- 호스트 헤더 필수화
- 확장된 캐싱, 상태 코드 및 부분 요청(Range 헤더)

### HTTP/2
`HTTP/2`는 2015년 표준화된 버전으로 텍스트 기반에서 바이너리 기반 프로토콜로 전환하고, 멀티플렉싱, 헤더 압축, 서버 푸시를 도입해 웹 성능을 크게 향상시켰습니다.

- 바이너리 프레이밍
- 멀티플렉싱 (동시 다중 요청/응답 처리)
- 헤더 압축 (HPACK)
- 서버 푸시 지원
- TLS 사용 권장

### HTTP/3
`HTTP/3`는 `UDP` 기반 `QUIC` 프로토콜 위에서 동작하며, TCP 한계였던 연결 지연과 헤드 오브 라인 블로킹 문제를 해결하여 빠른 연결과 안정성을 제공합니다. 현재 점진적으로 도입 중입니다.

- UDP 기반 QUIC 프로토콜 사용
- 빠른 연결 설정과 재개
- 헤드 오브 라인 블로킹 최소화
- TLS 적용 필수

#### QUIC Protocol
**QUIC(Quick UDP Internet Connections)**는 구글이 개발한 차세대 전송 프로토콜로, 전통적인 TCP 대신 UDP 위에서 동작합니다. 웹 통신에서 TCP가 가진 지연 문제와 헤드 오브 라인 블로킹 문제를 해결하기 위해 설계되었습니다.

- **UDP 기반 프로토콜**: TCP처럼 연결 지향적이며 UDP 위에서 빠른 연결 설정 가능
- **지연 시간 기반 데이터 전송**
  - `0-RTT`: 이전에 서버와 통신한 적이 있으면 거의 지연 없이 즉시 데이터 전송 가능
  - `1-RTT`: 처음 연결 시 한 번 왕복 통신 후 안전하게 연결 성립
- **멀티플렉싱 지원**: 하나의 연결에서 여러 스트림을 독립적으로 처리해 헤드 오브 라인 블로킹 해소
- **내장된 암호화**: TLS 1.3을 기본 내장해 안전한 통신 보장
- **빠른 오류 복구 및 재전송**: 네트워크 상태 변화에 신속 대응하여 안정적 연결 유지

---

## HTTPS
**HTTPS(HyperText Transfer Protocol Secure)**는 HTTP에 `TLS` 암호화를 결합한 보안 통신 프로토콜로, 웹에서 안전한 데이터 전송을 보장합니다. 사용자와 서버 간 주고받는 모든 정보는 암호화되어 도청이나 위조로부터 보호되며, 현재 대부분의 웹사이트에서 필수적으로 사용되고 있습니다. 보안 외에도 검색엔진 최적화(SEO)나 사용자 신뢰 확보에 중요한 역할을 합니다.

[![](\assets\posts\2025-08-17-Web Communication.md\https.png)](\assets\posts\2025-08-17-Web Communication.md\https.png)

- **데이터 암호화**: 모든 통신 내용은 TLS를 통해 암호화되어 외부 노출 방지
- **서버 인증**: 브라우저가 TLS 인증서를 통해 서버의 신원을 검증
- **무결성 보장**: 데이터가 중간에서 변경되거나 위조되지 않았음을 보장
- **기본 포트 443 사용**: HTTP(80)와 달리 보안 연결을 위한 전용 포트를 사용
- **HTTP 모든 버전과 호환**: HTTP/1.1, HTTP/2, HTTP/3 모두 HTTPS를 통해 통신 가능

### Security

- **TLS Handshake**

  [![](\assets\posts\2025-08-17-Web Communication.md\handshake.png)](\assets\posts\2025-08-17-Web Communication.md\handshake.png)
  - 클라이언트와 서버는 연결 초기에 서로 지원하는 암호화 알고리즘을 협상하고, 공개키 기반 암호화로 세션 키를 안전하게 교환합니다. 이는 안전한 통신을 시작하기 위한 필수 절차입니다.


- **Symmetric Encryption**

  [![](\assets\posts\2025-08-17-Web Communication.md\encryption.png)](\assets\posts\2025-08-17-Web Communication.md\encryption.png)
  - `TLS Handshake` 이후에는 효율적인 통신을 위해 대칭키 방식으로 데이터를 암호화합니다. 이 방법은 빠르고 계산 비용이 적어 실시간 데이터 전송에 적합합니다.


- **Certificate Chain**

  [![](\assets\posts\2025-08-17-Web Communication.md\chain.png)](\assets\posts\2025-08-17-Web Communication.md\chain.png)
  - 서버 인증서는 루트 인증기관(CA)부터 시작해 중간 인증기관을 거쳐 최종 엔터티 인증서까지 이어지는 신뢰 체계로 검증됩니다. 이를 통해 서버의 신뢰성을 확인할 수 있습니다.

- **PFS(Perfect Forward Secrecy)**

  [![](\assets\posts\2025-08-17-Web Communication.md\pfs.png)](\assets\posts\2025-08-17-Web Communication.md\pfs.png)
  - 세션마다 고유한 임시 키를 사용해 암호화하며, 키가 유출되더라도 과거의 통신 내용을 복호화할 수 없도록 보호합니다. 과거 데이터의 안전성을 보장하는 중요한 보안 기능입니다.

- **Certificate Status**

  [![](\assets\posts\2025-08-17-Web Communication.md\ocsp.png)](\assets\posts\2025-08-17-Web Communication.md\ocsp.png)
  - 클라이언트는 **OCSP(Online Certificate Status Protocol)** 또는 **CRL(Certificate Revocation List)**을 통해 서버 인증서의 유효성을 실시간으로 점검합니다. 이 과정은 만료되거나 폐기된 인증서 사용을 방지합니다.


---

## References
- [Wikipedia 공식 문서](https://wikipedia.org/wiki/)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
