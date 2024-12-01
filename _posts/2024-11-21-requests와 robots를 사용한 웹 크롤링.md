---
title: requests와 robots를 사용한 웹 크롤링
category: Study
tag: [Education, Requests, Crawling, Python]
---

<nav class="post-toc" markdown="1">
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>


## `requests` 라이브러리란?
> Python에서 HTTP 요청을 보내기 위한 강력하고 사용이 쉬운 라이브러리입니다. `GET`, `POST`, `PUT` 등의 HTTP 메서드를 간단한 코드로 실행할 수 있습니다.

### 1. 설치
```bash
pip install requests
```

### 2. 주요 기능
#### 1. GET 요청
* 서버로부터 데이터를 가져오는 데 사용됩니다.

```python
import requests

response = requests.get('https://httpbin.org/get')
print(response.status_code)  # 상태 코드 출력 (예: 200)
print(response.text)         # 응답 본문 출력
```

#### 2. POST 요청
* 서버에 데이터를 전송할 때 사용됩니다.

```python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.json())  # JSON 응답 출력
```

#### 3. JSON 데이터 전송
* JSON 데이터를 POST 요청으로 보낼 수 있습니다.

```python
url = 'https://httpbin.org/post'
json_data = {'name': 'Alice', 'age': 25}
response = requests.post(url, json=json_data)
print(response.json())
```

#### 4. URL 매개변수 전달 (params)
* GET 요청에 쿼리 문자열을 추가할 수 있습니다.

```python
params = {'q': 'Python', 'sort': 'relevance'}
response = requests.get('https://httpbin.org/get', params=params)
print(response.url)  # 완성된 URL 출력
```

#### 5. 헤더 설정 (headers)
* HTTP 헤더를 사용자 정의할 수 있습니다.

```python
headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get('https://httpbin.org/get', headers=headers)
print(response.headers)
```

#### 6. 파일 업로드 (files)
* 파일을 서버에 업로드할 수 있습니다.

```python
files = {'file': open('example.txt', 'rb')}
response = requests.post('https://httpbin.org/post', files=files)
print(response.text)
```

#### 7. 응답 정보 확인
* 응답의 다양한 정보를 확인할 수 있습니다.

```python
response = requests.get('https://httpbin.org/get')
print(response.status_code)  # HTTP 상태 코드
print(response.headers)      # 응답 헤더
print(response.content)      # 바이트 형태의 응답 내용
```

#### 8. 타임아웃 설정 (timeout)
* 요청 시간 초과를 설정할 수 있습니다.

```python
try:
    response = requests.get('https://httpbin.org/delay/5', timeout=3)
except requests.exceptions.Timeout:
    print('요청 시간이 초과되었습니다.')
```

#### 9. 예외 처리
* 요청 중 발생할 수 있는 예외를 처리할 수 있습니다.

```python
try:
    response = requests.get('https://httpbin.org/status/404')
    response.raise_for_status()  # 상태 코드가 4xx/5xx인 경우 예외 발생
except requests.exceptions.HTTPError as e:
    print(f'HTTP 오류 발생: {e}')
```

## robots.txt란?
>robots.txt는 웹사이트 소유자가 크롤러의 접근을 제어하기 위해 사용하는 텍스트 파일입니다. 주로 크롤러가 특정 경로를 크롤링하지 않도록 안내합니다.

``` javascript
// robots.txt

User-agent: *
Disallow: /admin/
Allow: /public/
```

* User-agent: *는 모든 크롤러를 의미합니다.
* Disallow: /admin/은 /admin/ 디렉터리에 대한 접근을 차단합니다.
* Allow: /public/은 /public/ 디렉터리를 허용합니다.

## requests와 robots.txt를 함께 사용하는 크롤링
```python
import requests

# robots.txt 내용 가져오기
robots_txt_url = 'https://example.com/robots.txt'
response = requests.get(robots_txt_url)

if response.status_code == 200:
    print("robots.txt 내용:")
    print(response.text)
else:
    print("robots.txt 파일을 가져올 수 없습니다.")

# 특정 페이지에 GET 요청
target_url = 'https://example.com/public/'
response = requests.get(target_url)
print(f"{target_url}에 대한 응답 코드:", response.status_code)
```

## 크롤링 시 주의사항
* robots.txt 준수: 크롤러가 웹사이트 소유자의 요청을 존중하는 것이 중요합니다.
* 법적 및 윤리적 책임: robots.txt는 법적 강제력이 없지만, 웹사이트 정책을 무시한 크롤링은 법적 문제를 초래할 수 있습니다.
* 트래픽 관리: 웹사이트에 과도한 트래픽을 유발하지 않도록 주의해야 합니다.

## 참고 자료
* [Python Requests 공식 문서](https://docs.python-requests.org/en/latest/)
* [robots.txt 소개 (Google Developers)](https://developers.google.com/search/docs/advanced/robots/intro)
* [robots.txt 표준 사이트](https://www.robotstxt.org/)
