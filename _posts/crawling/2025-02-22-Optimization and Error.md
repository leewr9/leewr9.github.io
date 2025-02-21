---
title: Optimization and Error
category: Crawling
tag: [Python, Crawling]
---

> 웹 크롤링은 대규모 데이터를 수집하는 작업에서 속도 최적화와 에러 처리가 매우 중요합니다. 크롤러의 성능을 최적화하고, 예기치 않은 오류를 처리할 수 있는 전략을 적용하는 것이 효율적인 크롤링을 위한 핵심입니다. 이 글에서는 크롤링 속도 최적화, User-Agent 변경 및 Proxy 설정, 그리고 에러 처리와 재시도 로직 구현에 대해 다룹니다.

---

## Optimizing Speed
웹 크롤링에서 가장 큰 성능 문제 중 하나는 요청과 응답을 기다리는 시간입니다. 비동기 요청을 활용하면 여러 페이지를 동시에 요청할 수 있어 크롤링 속도를 획기적으로 개선할 수 있습니다.

비동기 요청을 처리하는 데 주로 사용하는 라이브러리는 `aiohttp`와 `asyncio`입니다. 이 두 라이브러리를 사용하여 여러 요청을 동시에 보내고, 응답을 처리할 수 있습니다.

```python
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['http://example.com', 'http://example2.com']
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results) # 여러 페이지의 응답 결과

# 비동기 요청 실행
asyncio.run(main())
```

비동기 요청을 사용하면 각 요청을 기다리지 않고 동시에 여러 페이지에서 데이터를 가져올 수 있어 크롤링 속도가 빠릅니다.

---

## Changing Configuration
웹 크롤러가 너무 많은 요청을 보내면 서버에서 차단할 수 있습니다. 이를 방지하기 위해 `User-Agent`를 변경하거나 `Proxy`를 설정하여 IP 차단을 우회할 수 있습니다.

### User-Agent
`User-Agent`는 웹 브라우저가 서버에 요청을 보낼 때 사용되는 헤더 값입니다. 이를 변경하면 웹사이트가 크롤러의 요청을 사람이 보낸 것처럼 인식하게 할 수 있습니다.

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get('http://example.com', headers=headers)
print(response.text) # 웹 페이지의 HTML 내용
```

### Proxy 
`Proxy` 서버를 사용하면 요청을 다른 IP에서 보내는 것처럼 할 수 있습니다. 이를 통해 IP 차단을 우회할 수 있습니다.

```python
import requests

proxies = {
    'http': 'http://your_proxy_ip:port',
    'https': 'https://your_proxy_ip:port'
}

response = requests.get('http://example.com', proxies=proxies)
print(response.text) # Proxy를 사용한 웹 페이지의 HTML 내용
```
Proxy를 설정하여 여러 IP에서 요청을 보낼 수 있기 때문에 차단을 피할 수 있습니다.

---

## Error Handling
웹 크롤링 중에는 다양한 에러가 발생할 수 있습니다. 네트워크 문제, 서버 오류, 시간 초과 등 예기치 않은 상황에 대비하기 위해 에러 처리 및 재시도 로직을 구현하는 것이 중요합니다.

에러가 발생했을 때, 이를 처리하고 크롤링이 계속 진행될 수 있도록 해야 합니다. 예를 들어, 네트워크 오류나 서버 오류가 발생했을 때 예외를 처리하는 방식입니다.

```python
import requests
from time import sleep

def fetch_with_error_handling(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # 상태 코드가 200이 아닌 경우 예외 발생
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

url = 'http://example.com'
data = fetch_with_error_handling(url)
if data:
    print(data) # 정상적으로 데이터를 받아온 경우
```

### Retry Logic
크롤링 중 네트워크 오류나 일시적인 서버 문제로 인해 요청이 실패할 수 있습니다. 이를 해결하기 위해 재시도 로직을 구현하여 일정 시간 후 다시 시도할 수 있습니다.

```python
import requests
from time import sleep

def fetch_with_retry(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            if attempt < retries - 1:
                print(f"Retrying in {delay} seconds...")
                sleep(delay)
            else:
                print("Max retries reached. Skipping this URL.")
                return None

url = 'http://example.com'
data = fetch_with_retry(url)
if data:
    print(data) # 재시도 후 데이터를 받아온 경우
```
이 코드는 최대 3번까지 재시도하고, 각 시도 후에는 2초의 지연 시간을 둡니다. 실패한 요청에 대해서는 재시도를 통해 안정적으로 크롤링을 진행할 수 있습니다.

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
