---
title: Networking
category: Python
tag: [Network, Python]
---

> Python은 네트워크 애플리케이션을 작성하는 데 필요한 다양한 도구와 라이브러리를 제공합니다. 네트워크 프로그래밍은 소켓 프로그래밍, HTTP 요청, 그리고 API 통신 등을 포함합니다.

---

## Socket Programming

`소켓 프로그래밍(Socket Programming)`은 네트워크를 통해 데이터 통신을 수행하는 기본적인 방법입니다. Python에서는 `socket` 모듈을 사용하여 서버와 클라이언트 간의 연결을 설정하고, 데이터를 주고받을 수 있습니다. 소켓을 사용하면 TCP/IP 연결을 통해 네트워크에서 메시지를 주고받을 수 있습니다.

### Server

서버는 클라이언트의 요청을 수신하고 응답하는 역할을 합니다.

```python
import socket

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is waiting for a connection...")

# 클라이언트 연결 수락
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established!")

# 클라이언트로 메시지 전송
client_socket.sendall("Hello, Client!".encode())

# 연결 종료
client_socket.close()
```

### Client

클라이언트는 서버에 연결하고, 요청을 보내며 응답을 받습니다.

```python
import socket

# 서버에 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# 서버로부터 메시지 수신
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

# 연결 종료
client_socket.close()
```

위의 예시에서는 서버가 `localhost`와 포트 12345에서 대기하고, 클라이언트가 해당 포트에 연결하여 서버로부터 메시지를 수신합니다.

---

## HTTP Requests

HTTP 요청은 웹 서버와 클라이언트 간의 데이터를 주고받을 때 사용됩니다. Python에서는 `requests` 모듈과 `urllib` 모듈을 통해 HTTP 요청을 쉽게 보낼 수 있습니다.

### Requests

`requests` 모듈은 HTTP 요청을 보내고 응답을 처리하는 데 사용됩니다. 간단하게 GET, POST 요청을 보낼 수 있습니다.

```python
import requests

# GET 요청 보내기
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.status_code) # 상태 코드 출력
print(response.json()) # JSON 응답 출력

# POST 요청 보내기
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.status_code) # 상태 코드 출력
print(response.json()) # JSON 응답 출력
```

### Urllib

`urllib`는 표준 라이브러리로, URL을 처리하고 HTTP 요청을 보낼 수 있습니다.

```python
import urllib.request

# GET 요청 보내기
response = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts')
data = response.read()
print(data.decode()) # 응답 내용 출력
```

`requests`는 사용하기 간편하고 다양한 기능을 제공하는 반면, `urllib`는 Python의 기본 라이브러리로 간단한 HTTP 요청을 보내는 데 유용합니다.

---

## API Communication

API(Application Programming Interface) 통신은 프로그램 간에 데이터를 주고받는 표준화된 방법입니다. Python에서 API를 사용하면 외부 서비스와 통신하여 데이터를 가져오거나 보낼 수 있습니다. 대부분의 API는 HTTP를 통해 데이터를 주고받습니다.

```python
import requests

# API 엔드포인트
url = 'https://jsonplaceholder.typicode.com/posts'

# API 요청
response = requests.get(url)
data = response.json() # JSON 형식으로 응답받기

# 받은 데이터 출력
for post in data:
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")
    print("-" * 40)
```

위 예시에서는 JSONPlaceholder라는 무료 API를 사용하여 게시물 데이터를 가져오고 출력하는 방법을 보여줍니다. `requests.get()`을 사용하여 GET 요청을 보내고, `response.json()`을 통해 JSON 데이터를 파싱합니다.

---

## References

- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
