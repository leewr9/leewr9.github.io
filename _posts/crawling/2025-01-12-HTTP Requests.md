---
title: HTTP Requests
category: Crawling
tag: [Requests, Python, Crawling]
---

> HTTP(HyperText Transfer Protocol)는 웹에서 클라이언트와 서버 간에 데이터를 주고받는 프로토콜입니다. 웹 페이지를 요청하거나 데이터를 전송할 때, HTTP 요청을 통해 정보를 주고받습니다.

---

## Protocol

`HTTP` 요청 방식에는 여러 가지가 있으며, 각각 특정한 목적에 맞게 사용됩니다. 가장 일반적으로 사용되는 방식은 `GET`과 `POST`이며, 데이터 수정이나 삭제를 위해 `PUT`, `DELETE`, `PATCH`도 사용됩니다.

- `GET`: 서버에서 데이터를 조회할 때 사용됩니다. 웹 페이지를 열거나 API에서 정보를 가져올 때 활용됩니다.
- `POST`: 서버에 데이터를 전송할 때 사용됩니다. 폼 제출, 파일 업로드 등의 요청에 활용됩니다.
- `PUT`: 서버의 기존 데이터를 업데이트할 때 사용됩니다. 전체 리소스를 새로운 데이터로 교체합니다.
- `DELETE`: 서버에서 특정 데이터를 삭제할 때 사용됩니다.
- `PATCH`: 서버의 기존 데이터 중 일부를 수정할 때 사용됩니다. `PUT`은 전체 리소스를 교체하는 반면, `PATCH`는 변경된 부분만 업데이트합니다.
- `Headers`: HTTP 요청과 응답에 대한 추가 정보를 포함하며, 서버와 클라이언트 간의 통신 방식을 제어하는 데 사용됩니다.

---

## Requests

Python에서 `HTTP` 요청을 보내는 가장 간편한 방법은 `requests` 라이브러리를 사용하는 것입니다. 이 라이브러리를 사용하면 `GET`, `POST` 요청을 쉽게 보낼 수 있으며, 응답도 쉽게 처리할 수 있습니다. `requests` 라이브러리는 HTTP 요청을 처리하고 서버로부터 받은 응답을 Python 객체로 변환해줍니다.

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

---

## Crawling Rules

`robots.txt`는 웹사이트 소유자가 검색 엔진 크롤러에 대해 사이트의 특정 페이지나 디렉토리에 대한 접근을 제어하기 위해 사용하는 파일입니다.

- `User-agent`: 특정 검색 엔진 크롤러를 지정합니다.
- `Disallow`: 크롤링을 허용하지 않는 경로를 지정합니다.

```txt
User-agent: *
Disallow: /
```

위 예시는 모든 크롤러(\*)가 전체 디렉토리에 접근하지 못하도록 설정한 것입니다.

---

## References

- [Requests 공식 문서](https://requests.readthedocs.io/en/latest/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
