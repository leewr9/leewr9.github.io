---
title: HTTP Requests
category: Crawling
tag: [Requests, Python, Crawling]
---

> HTTP(HyperText Transfer Protocol)는 웹에서 클라이언트와 서버 간에 데이터를 주고받는 프로토콜입니다. 웹 페이지를 요청하거나 데이터를 전송할 때, HTTP 요청을 통해 정보를 주고받습니다. 

---

## HTTP Protocol
HTTP 요청에는 여러 가지 방식이 있으며, 그 중 가장 많이 사용되는 것은 GET과 POST입니다.

- `GET`: 서버에서 정보를 요청하는 방식입니다. 웹 페이지를 열 때, URL을 입력하고 요청하는 것이 바로 `GET` 요청입니다. 주로 데이터를 가져올 때 사용됩니다.
- `POST`: 서버에 데이터를 전송할 때 사용하는 방식입니다. `POST` 요청은 보통 사용자 입력을 서버로 보내거나, 파일 업로드와 같은 데이터를 전송할 때 사용됩니다.
- `Headers`: HTTP 요청에는 헤더(Header)가 포함될 수 있습니다. 헤더는 요청에 대한 추가 정보를 담고 있으며, 서버가 요청을 어떻게 처리할지에 대한 정보를 제공합니다. 예를 들어, `User-Agent` 헤더는 요청을 보낸 클라이언트의 정보를 서버에 전달합니다.

```sql
GET / HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
```

---

## HTTP Requests
Python에서 HTTP 요청을 보내는 가장 간편한 방법은 `requests` 라이브러리를 사용하는 것입니다. 이 라이브러리를 사용하면 `GET`, `POST` 요청을 쉽게 보낼 수 있으며, 응답도 쉽게 처리할 수 있습니다. `requests` 라이브러리는 HTTP 요청을 처리하고 서버로부터 받은 응답을 Python 객체로 변환해줍니다.

```bash
pip install requests
```

### GET
`requests.get()` 메서드를 사용하여 웹 페이지의 HTML을 가져오고, 그 내용을 출력합니다.

```python
import requests

# GET 요청을 통해 웹 페이지의 HTML 데이터 가져오기
response = requests.get('https://www.example.com')

# 서버로부터 받은 응답의 상태 코드 확인
print(response.status_code) # 200이 성공을 의미

# 응답 받은 HTML 내용 출력
print(response.text) # 웹 페이지의 HTML 출력
```
- `response.status_code`: 서버의 응답 상태 코드를 반환합니다. `200`은 성공적인 요청을 의미합니다.
- `response.text`: 서버가 응답한 HTML 데이터를 반환합니다.

### POST
`requests.post` 메서드를 사용하여 `POST` 요청을 보내며, 주로 사용자 데이터를 서버로 전송할 때 사용됩니다.

```python
import requests

# POST 요청을 통해 서버에 데이터 전송
data = {'username': 'user', 'password': 'password'}
response = requests.post('https://www.example.com/login', data=data)

# 서버 응답 확인
print(response.status_code) # 200 또는 다른 상태 코드

# 응답 받은 데이터 출력
print(response.text) # 로그인 후의 페이지 내용 등
```
- data: 서버로 전송할 데이터를 딕셔너리 형태로 전달합니다.
- requests.post(): POST 요청을 보낼 때 사용합니다.

---

## Crawling Rules
`robots.txt`는 웹사이트 소유자가 검색 엔진 크롤러에 대해 사이트의 특정 페이지나 디렉토리에 대한 접근을 제어하기 위해 사용하는 파일입니다. 

- `User-agent`: 특정 검색 엔진 크롤러를 지정합니다.
- `Disallow`: 크롤링을 허용하지 않는 경로를 지정합니다.

```txt
User-agent: *  
Disallow: / 
```
위 예시는 모든 크롤러(*)가 전체 디렉토리에 접근하지 못하도록 설정한 것입니다.

---

## References
- [Requests 공식 문서](https://requests.readthedocs.io/en/latest/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
