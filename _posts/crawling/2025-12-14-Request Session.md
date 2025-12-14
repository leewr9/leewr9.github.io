---
title: Request Session
category: Crawling
tag: [requests, Python, Crawling]
---

> 웹 크롤링 시 단순한 HTTP 요청부터 로그인, 쿠키 관리 등 상태 유지를 필요로 하는 작업까지 다양합니다. Python의 requests 라이브러리는 간단한 요청부터 세션 관리를 통한 복잡한 크롤링 작업까지 폭넓게 지원합니다. 


---

## requests
`requests` 라이브러리는 Python에서 `HTTP` 요청을 간편하게 처리할 수 있는 도구입니다. 단일 요청을 보낼 때 주로 사용되며, `GET`, `POST`, `PUT`, `DELETE` 등 다양한 HTTP 메서드를 지원합니다.

```python
import requests
# GET
requests.get('https://httpbun.com/get')
# POST
requests.post('https://httpbun.com/post', data={'key': 'value'})
# PUT
requests.put('https://httpbun.com/put', data={'key': 'value'})
# DELETE
requests.delete('https://httpbun.com/delete')
```


### GET
`GET` 요청은 서버로부터 데이터를 가져올 때 사용됩니다. 헤더, 쿼리 매개변수, 타임아웃 등 다양한 옵션을 설정할 수 있습니다. 

```python
import json
import requests

response = requests.get('https://httpbun.com/get')
data = response.json()
pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
print(pretty_json)
```

```json
{
    "method": "GET",
    "args": {},
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",        
        "Host": "httpbun.com",
        "User-Agent": "python-requests/2.32.5",
        "Via": "1.1 Caddy"
    },
    "origin": "218.148.162.71",
    "url": "https://httpbun.com/get",
    "form": {},
    "data": "",
    "json": null,
    "files": {}
}
```

#### headers
`headers` 매개변수를 사용하여 요청 헤더를 설정할 수 있습니다. 인증 토큰이나 사용자 에이전트 등을 지정할 때 유용합니다.

```python
import json
import requests

headers = {'User-Agent': 'MyBot', 'Authorization': 'Bearer TOKEN'}
response = requests.get('https://httpbun.com/headers', headers=headers)
data = response.json()
pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
print(pretty_json)
```

```json
{
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",        
        "Authorization": "Bearer TOKEN",
        "Host": "httpbun.com",
        "User-Agent": "MyBot",
        "Via": "1.1 Caddy"
    }
}
```

#### params
`params` 매개변수를 사용하여 쿼리 문자열을 설정할 수 있습니다. URL에 매개변수를 추가할 때 편리합니다.

```python
import json
import requests

params = {'q': 'python', 'page': 2}
response = requests.get('https://httpbun.com/get', params=params)
data = response.json()
pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
print(response.url)  # https://httpbun.com/get?q=python&page=2
print(pretty_json)
```

```json
{
    "method": "GET",
    "args": {
        "page": "2",
        "q": "python"
    },
    "url": "https://httpbun.com/get?q=python&page=2",        
}
```



#### timeout
`timeout` 매개변수를 사용하여 요청 타임아웃을 설정할 수 있습니다. 지정한 시간 내에 응답이 없으면 예외가 발생합니다.

```python
import requests

try:
    response = requests.get('https://httpbun.com/delay/3', timeout=2)
except requests.Timeout:
    print('Timeout')
except requests.RequestException as e:
    print('Error:', e)
```

### POST
`POST` 요청은 서버에 데이터를 전송할 때 사용됩니다. 다양한 데이터 형식을 지원하며, 이로 인해 여러 가지 방식으로 데이터를 보낼 수 있습니다.

#### data
`data` 매개변수를 사용하여 폼 데이터를 전송할 수 있습니다. `application/x-www-form-urlencoded` 형식으로 전송됩니다.

```python
import json
import requests

data = {'username': 'test', 'password': '1234'}
response = requests.post('https://httpbun.com/post', data=data)
data = response.json()
pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
print(pretty_json)
```

```json
{
    "method": "POST",
    "url": "https://httpbun.com/post",
    "form": {
        "password": "1234",
        "username": "test"
    },
}
```

#### json
`json` 매개변수를 사용하여 JSON 데이터를 전송할 수 있습니다. `application/json` 형식으로 전송됩니다.

```python
import json
import requests

payload = {'id': 1, 'name': 'lee'}
response = requests.post('https://httpbun.com/post', json=payload)
data = response.json()
pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
print(pretty_json)
```

```json
{
    "method": "POST",
    "url": "https://httpbun.com/post",
    "data": "{\"id\": 1, \"name\": \"lee\"}",
    "json": {
        "id": 1,
        "name": "lee"
    },
}
```


#### files
`files` 매개변수를 사용하여 파일을 업로드할 수 있습니다. `multipart/form-data` 형식으로 전송됩니다.

```python
import json
import requests

files = {'file': open('test.txt', 'rb')}
response = requests.post('https://httpbun.com/post', files=files)
data = response.json()
pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
print(pretty_json)
```

```json
{
    "method": "POST",
    "url": "https://httpbun.com/post",
    "files": {
        "file": {
            "content": "",
            "filename": "test.txt",
            "headers": {
                "Content-Disposition": "form-data; name=\"file\"; filename=\"test.txt\""
            },
            "size": 0
        }
    }
}
```

---

## Session
`Session` 객체는 여러 요청 간에 설정과 상태를 유지할 수 있도록 도와줍니다. 로그인 세션 유지, 공통 헤더 설정 등 다양한 상황에서 유용하게 사용됩니다.

```python
import requests

session = requests.Session()
response = session.get('https://httpbun.com/cookies')
print(response.json())

session.get('https://httpbun.com/cookies/set?mycookie=value')

response = session.get('https://httpbun.com/cookies')
print(response.json())
```

```bash
{'cookies': {}}
{'cookies': {'mycookie': 'value'}}
```

### Adapter
`Adapter`를 사용하면 특정 프로토콜에 대한 설정을 커스터마이징할 수 있습니다. 예를 들어, 재시도 정책을 설정하거나 프록시를 지정할 수 있습니다.

```python
import requests
from requests.adapters import HTTPAdapter

session = requests.Session()
adapter = HTTPAdapter(max_retries=5) # 최대 5회 재시도 설정
session.mount('http://', adapter)  # HTTP에 어댑터 장착
session.mount('https://', adapter) # HTTPS에 어댑터 장착
```

---

## References

- [requests 공식 문서](https://requests.readthedocs.io/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
