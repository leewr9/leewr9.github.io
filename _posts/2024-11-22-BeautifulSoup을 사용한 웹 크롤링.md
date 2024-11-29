---
title: BeautifulSoup을 사용한 웹 크롤링
category: Study
tag: [Education, Crawling, Requests, Python]
---

<nav class="post-toc" markdown="1">
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>


## `BeautifulSoup` 라이브러리란?
> `BeautifulSoup`은 가져온 HTML 데이터를 파싱하고 원하는 정보를 추출하는 데 사용됩니다. `requests`와 함께 사용하면 웹 크롤링을 쉽게 구현할 수 있습니다.

### 1. 설치
```bash
pip install beautifulsoup4
pip install requests
```

### 2. 기본 사용법
* 예제: 웹 페이지에서 제목 태그(`<title>`) 가져오기

```python
import requests
from bs4 import BeautifulSoup

# 1. 웹 페이지 요청
url = 'https://example.com'
response = requests.get(url)

# 2. HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 3. <title> 태그 가져오기
title_tag = soup.title
print("페이지 제목:", title_tag.string)
```

### 3. 주요 기능 예제
* (1) 모든 `<a>` 태그에서 링크 추출

```python
# 모든 <a> 태그 추출
for link in soup.find_all('a'):
    print("링크:", link.get('href'))
```

* (2) 특정 클래스의 요소 추출

```python
# 특정 클래스의 <div> 태그 찾기
divs = soup.find_all('div', class_='example-class')
for div in divs:
    print(div.text)
```

* (3) ID로 요소 찾기

```python
# 특정 ID의 태그 찾기
specific_element = soup.find(id='specific-id')
if specific_element:
    print("ID로 찾은 내용:", specific_element.text)
```

### 4. 사용자 정의 헤더 추가
```python
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.string)
```

### 5. 크롤링 시 주의사항
* robots.txt 파일 확인: 크롤링 전 웹사이트의 robots.txt를 확인하고 정책을 준수하세요.
* 예외 처리: 요청 실패나 HTML 파싱 오류에 대비한 예외 처리가 필요합니다.
* 트래픽 부하 최소화: 크롤링 빈도를 조정하여 서버에 과도한 부하를 주지 않도록 주의하세요.

## 참고 자료
* [BeautifulSoup 공식 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests 공식 문서](https://docs.python-requests.org/en/latest/)
* [robots.txt 소개 (Google Developers)](https://developers.google.com/search/docs/advanced/robots/intro)