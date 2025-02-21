---
title: BeautifulSoup and Data Extraction
category: Crawling
tag: [BeautifulSoup, Python, Crawling]
---

> BeautifulSoup는 Python에서 HTML 및 XML 문서를 파싱하고, 그 문서에서 필요한 데이터를 쉽게 추출할 수 있도록 도와주는 라이브러리입니다. 웹 크롤링을 할 때, BeautifulSoup는 웹 페이지의 HTML을 구조적으로 이해하고, 원하는 데이터를 쉽게 찾고 추출하는 데 매우 유용합니다.

---

## HTML Structure and DOM
HTML 문서는 트리 구조로 되어 있으며, 각 요소는 "태그"라고 불리는 HTML 요소들로 구성됩니다. 이러한 HTML 문서의 구조는 DOM(Document Object Model)이라고 불리며, 웹 페이지의 각 요소에 접근하는 방법을 제공합니다.

DOM은 HTML 문서의 각 태그를 노드(Node)로 변환하여 구조적으로 표현합니다. 예를 들어, `<div>`, `<a>`, `<p>` 같은 HTML 태그들이 DOM 트리에서 각각 하나의 노드로 나타납니다. BeautifulSoup는 이 DOM 구조를 바탕으로 HTML을 파싱하고, 원하는 데이터를 추출할 수 있게 합니다.

```bash
pip install beautifulsoup4
```

### find
`find` 함수는 HTML 문서에서 첫 번째로 일치하는 요소를 찾습니다. 원하는 태그나 속성에 맞는 첫 번째 요소를 반환합니다.

```python
from bs4 import BeautifulSoup
html = '<html><body><h1>Title</h1></body></html>'
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('h1').text
print(title) # 'Title' 출력
```

### find_all
`find_all` 함수는 HTML 문서에서 일치하는 모든 요소를 찾아 리스트로 반환합니다. 동일한 태그를 여러 개 찾을 때 유용합니다.

```python
html = '<html><body><h1>Title</h1><h1>Subtitle</h1></body></html>'
soup = BeautifulSoup(html, 'html.parser')
headings = soup.find_all('h1')
for heading in headings:
    print(heading.text) # 'Title', 'Subtitle' 출력
```

### select
`select` 함수는 CSS 선택자를 사용하여 원하는 요소를 찾습니다. CSS 스타일 시트를 작성할 때 사용하는 선택자를 이용하여 HTML 요소를 선택할 수 있습니다.

```python
html = '<html><body><div class="content">Content here</div></body></html>'
soup = BeautifulSoup(html, 'html.parser')
content = soup.select('.content') # 클래스명이 'content'인 div 선택
print(content[0].text) # 'Content here' 출력
```

### select_one
`select_one` 함수는 CSS 선택자를 사용하여 첫 번째 일치하는 요소를 반환합니다. `select`와 비슷하지만, 첫 번째 요소만 찾을 때 사용합니다.

```python
html = '<html><body><div id="main">Main Content</div></body></html>'
soup = BeautifulSoup(html, 'html.parser')
main_content = soup.select_one('#main') # id가 'main'인 div 선택
print(main_content.text) # 'Main Content' 출력
```

---

## Data Extraction
HTML에서 데이터를 추출하는 주요 방법은 텍스트 내용, 태그의 속성, 그리고 리스트 형태로 데이터를 가져오는 것입니다. 

### text
`text` 속성을 사용하면 HTML 태그 내부의 텍스트를 추출할 수 있습니다.

```python
html = '<html><body><h1>Welcome to Python!</h1></body></html>'
soup = BeautifulSoup(html, 'html.parser')
text = soup.find('h1').text
print(text) # 'Welcome to Python!' 출력
```

### attribute
`get()` 메서드를 사용하면 태그의 속성 값을 추출할 수 있습니다. 예를 들어, `<a>` 태그의 `href` 속성 값을 가져올 수 있습니다.

```python
html = '<html><body><a href="https://www.example.com">Visit Example</a></body></html>'
soup = BeautifulSoup(html, 'html.parser')
link = soup.find('a').get('href')
print(link) # 'https://www.example.com' 출력
```

---

## References
- [BeautifulSoup 공식 문서](https://www.crummy.com/software/BeautifulSoup/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
