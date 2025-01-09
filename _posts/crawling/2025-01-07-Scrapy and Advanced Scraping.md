---
title: Scrapy and Advanced Scraping
category: Crawling
tag: [Scrapy, Python, Crawling]
---

> 웹 크롤링은 웹사이트에서 데이터를 추출하는 작업입니다. 대규모 크롤링을 다룰 때 Scrapy는 매우 유용한 도구입니다. Scrapy는 효율적이고 확장 가능한 웹 크롤링 및 스크래핑 프레임워크로, 대규모 데이터를 쉽게 처리할 수 있습니다. 이 가이드에서는 Scrapy의 기본 구조, 크롤러 설계, AJAX 요청 처리 방법, OpenAPI를 활용한 API 크롤링 방법을 설명합니다.

---

## Large-Scale Scraping
`Scrapy`는 대규모 웹 크롤링 프로젝트에 적합한 프레임워크입니다. `Scrapy`는 요청을 처리하고, 응답을 파싱하며, 데이터를 저장하는 기능을 기본적으로 제공합니다. 대규모 크롤링을 할 때는 `Scrapy`를 통해 여러 페이지를 동시에 처리할 수 있습니다.

```bash
pip install scrapy

# 새로운 프로젝트 생성
scrapy startproject myproject

# 새로운 spider 생성
scrapy genspider myspider example.com
```

### Structure
```plaintext
myproject/
│
├── scrapy.cfg
│
└── myproject/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders/
        ├── __init__.py
        └──  myspider.py
```

- `scrapy.cfg`: 프로젝트 설정 파일
- `myproject/spiders/`: 크롤링할 사이트의 URL을 정의하는 파일
- `myproject/items.py`: 스크래핑한 데이터를 저장할 클래스
- `myproject/pipelines.py`: 데이터를 처리하는 파이프라인
- `myproject/settings.py`: 프로젝트의 설정 파일

### Usage
`Scrapy`는 비동기식 요청을 처리하며, 각 요청이 끝날 때까지 기다리지 않고 다른 요청을 처리합니다. 이를 통해 크롤링 속도를 크게 향상시킬 수 있습니다. 또한, 분산 크롤링 기능도 지원하여 크롤링 작업을 여러 서버에서 분산시킬 수 있습니다.

```python
import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://example.com']

    def parse(self, response):
        title = response.css('h1::text').get()
        print('Page Title:', title) # Page Title: Example Domain
```

---

## Designing a Scraper
Scrapy에서 크롤러는 데이터를 추출하는 역할을 합니다. `parse` 함수는 응답을 처리하고 데이터를 추출하는데 사용됩니다. 기본적으로 웹 페이지의 HTML을 파싱하고, 필요한 데이터를 추출하여 저장합니다.

```python
class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://example.com']

    def parse(self, response):
        page_title = response.css('h1::text').get()
        page_url = response.url
        yield {
            'title': page_title,
            'url': page_url
        }
```

---

## Data Pipelines
Scrapy는 크롤링한 데이터를 처리하는 `파이프라인(pipeline)` 기능을 제공합니다. 파이프라인은 데이터가 크롤러에서 추출된 후 저장되기 전에 처리할 수 있는 곳입니다.

```python
class MyPipeline:
    def process_item(self, item, spider):
        item['title'] = item['title'].upper() # 제목을 대문자로 변환
        return item
```

파이프라인을 활성화하려면 `settings.py`에서 설정을 추가합니다:
```python
# settings.py
ITEM_PIPELINES = {
   'myproject.pipelines.MyPipeline': 1,
}
```

---

## Handling AJAX
AJAX는 웹 페이지에서 데이터를 동적으로 로드하는 데 사용됩니다. Scrapy는 기본적으로 AJAX 요청을 처리하지 않지만, JavaScript를 통해 동적으로 로드된 데이터를 크롤링할 수 있습니다.

AJAX 요청을 처리하려면 `scrapy-selenium`을 사용하여 JavaScript 렌더링을 처리하거나, 직접 AJAX 요청을 캡처하여 데이터를 추출할 수 있습니다.

```bash
pip install scrapy-selenium
```

```python
from scrapy_selenium import SeleniumRequest

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://example.com/ajax']

    def start_requests(self):
        yield SeleniumRequest(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        data = response.css('.ajax-data::text').get()
        print('AJAX Data:', data) # AJAX Data: Dynamic Content
```

---

## API Scraping 
웹사이트에서 데이터를 직접 크롤링하는 대신, API를 통해 데이터를 요청하고 받아오는 방법도 있습니다. 많은 웹사이트는 데이터를 API로 제공하며, 이를 사용하여 효율적으로 데이터를 수집할 수 있습니다.

```python
import scrapy
import json
import requests
from scrapy.http import JsonRequest

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://example.com']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       # 웹 페이지에서 데이터 크롤링
        page_title = response.css('h1::text').get()
        page_url = response.url

       # API에서 데이터 요청
        api_url = 'https://api.example.com/data'
        api_data = self.fetch_api_data(api_url)

       # 웹 페이지 데이터와 API 데이터를 결합
        item = {
            'title': page_title,
            'url': page_url,
            'api_data': api_data, # API에서 받은 데이터 추가
        }

       # 데이터 저장
        yield item

    def fetch_api_data(self, api_url):
       # API에서 JSON 데이터 요청
        response = requests.get(api_url)
        api_data = response.json()
        return api_data
```

OpenAPI 문서를 통해 API 엔드포인트와 데이터를 요청하는 방법을 이해할 수 있습니다. Scrapy를 사용하면 API로부터 받은 데이터를 크롤링한 웹 페이지의 데이터와 함께 저장할 수 있습니다.


---

## References
* [Scrapy 문서](https://scrapy.org/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
