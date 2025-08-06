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

`HTTP/0.9`는 1991년에 처음 등장한 HTTP 버전으로, 오직 GET 요청만 처리할 수 있는 아주 단순한 방식입니다. 요청에 대한 부가 정보를 주고받지 않고, 텍스트 데이터만 전달하는 구조입니다.

- 하나의 GET 요청만 처리
- 헤더, 상태 코드 없음
- 텍스트 데이터만 전달 가능

### HTTP/1.0

`HTTP/1.0`은 1996년 표준화되면서, 요청/응답에 대한 상태 코드와 헤더를 주고받는 기능이 도입되었습니다. 다만 요청마다 새로운 연결을 만들기 때문에 속도와 효율이 떨어졌습니다.

- 상태 코드와 헤더 주고받기 기능 도입
- 요청마다 새로운 연결 생성 (Non-persistent Connection)
- 기본적인 캐싱과 어떤 형태의 데이터를 받을지 선택하는 기능 지원 (Content Negotiation)

### HTTP/1.1

`HTTP/1.1`은 1997년에 발표되어 하나의 연결을 여러 요청에 재사용할 수 있게 되었고, 파일 일부만 다운로드하는 기능 등 다양한 확장이 이루어졌습니다.

- 하나의 연결을 여러 요청에 재사용 (Persistent Connection)
- 여러 요청을 순차적으로 미리 보내는 기능 도입 (Pipelining)
- 파일 일부만 다운로드하는 기능 도입 (Range Request)
- Host 정보를 헤더에 명시적으로 전달하도록 필수화
- 상태 코드, 캐싱 정책 등 확장

### HTTP/2

`HTTP/2`는 2015년 표준화된 버전으로, 데이터를 텍스트가 아닌 바이너리 형태로 주고받는 구조로 변경되고, 여러 요청을 한꺼번에 처리하는 기능이 추가되었습니다.

- 하나의 연결로 여러 요청/응답을 동시에 처리 (Multiplexing)
- 데이터를 바이너리로 주고받아 속도 향상 (Binary Framing)
- 헤더 정보를 압축해서 데이터 양 절감 (HPACK)
- 서버가 필요한 리소스를 클라이언트 요청 전에 전달 (Server Push)
- TLS 사용 권장

### HTTP/3

`HTTP/3`는 기존 TCP 연결 방식에서 벗어나, UDP 기반의 QUIC 프로토콜을 사용하는 최신 HTTP 버전입니다. 연결 지연을 줄이고, 하나의 요청이 막혀도 다른 요청들이 영향을 받지 않게 개선되었습니다.

- 하나의 요청 지연이 다른 요청에 영향 주지 않도록 개선 (Head-of-Line Blocking)
- 기존 TCP 대신 UDP를 기반으로 빠른 연결 설정
- 연결 도중 끊겨도 빠르게 복구
- TLS 암호화 통신을 기본 적용

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
