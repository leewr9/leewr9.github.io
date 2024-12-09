---
title: Selenium and Dynamic Websites
category: Crawling
tag: [Selenium, Python, Crawling]
---

> Selenium은 동적 웹사이트에서 데이터를 크롤링하는 데 매우 유용한 도구입니다. 최근에는 webdriver-manager 패키지를 사용하여 브라우저 드라이버를 자동으로 설치하고 관리하는 방식이 선호되고 있습니다. 이를 사용하면 번거롭게 드라이버를 직접 다운로드하거나 경로를 설정하지 않아도 됩니다.

---

## Selenium Manager
아래 명령어를 통해 `selenium`과 `webdriver-manager`를 설치합니다.

```bash
pip install selenium webdriver-manager
```

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# WebDriver-Manager를 사용한 ChromeDriver 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 웹 페이지 열기
url = 'https://example.com'
driver.get(url)

# 페이지 제목 출력
print('Page Title:', driver.title) # Page Title: Example Domain

# 브라우저 종료
driver.quit()
```
이 코드를 실행하면 WebDriver-Manager가 ChromeDriver를 자동으로 다운로드하여 실행합니다.

### find_element
`find_element` 함수는 다양한 방법으로 웹 요소를 찾을 수 있습니다.
- By.ID: `id` 속성을 기준으로 찾기
- By.NAME: `name` 속성을 기준으로 찾기
- By.XPATH: XPath 표현식을 사용해 찾기
- By.CLASS_NAME: `class` 속성을 기준으로 찾기
- By.TAG_NAME: `HTML` 태그를 기준으로 찾기

```python
from selenium.webdriver.common.by import By

# 요소 찾기
element = driver.find_element(By.XPATH, '//h1')
print('Element Text:', element.text) # Element Text: Example Domain
```

### click
`click` 함수는 웹 페이지의 버튼 또는 링크를 클릭할 수 있습니다.

```python
button = driver.find_element(By.XPATH, '//button[text()='Click Me']')
button.click()
```

### send_keys
`send_keys` 함수는 텍스트 필드에 데이터를 입력할 수 있습니다.

```python
input_box = driver.find_element(By.ID, 'username')
input_box.send_keys('my_username')
```

### get_attribute
`get_attribute` 함수는 특정 요소의 속성값을 가져올 수 있습니다.

```python
image = driver.find_element(By.TAG_NAME, 'img')
src = image.get_attribute('src')
print('Image Source:', src)
```

---

## Handling Delays
웹 페이지의 요소가 로드될 때까지 기다리는 것은 크롤링에서 매우 중요합니다. Selenium은 암시적 대기와 명시적 대기 두 가지 대기 방식을 제공합니다.

### Implicit Waits
- Selenium은 요소를 찾기 전에 설정된 시간만큼 대기합니다.
- 설정 시간 내에 요소가 로드되면 즉시 실행을 재개합니다.
- 한 번 설정하면 WebDriver 세션 동안 모든 요소 검색에 적용됩니다.

```python
driver.implicitly_wait(10) # 최대 10초 대기
```

### Explicit Wait
- 특정 조건이 충족될 때까지 기다립니다.
- 더 복잡한 대기 조건을 정의할 수 있습니다.
- `WebDriverWait`과 `ExpectedConditions`를 함께 사용합니다.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 특정 요소가 나타날 때까지 대기
wait = WebDriverWait(driver, 10)
dynamic_element = wait.until(EC.presence_of_element_located((By.ID, 'dynamic-content')))
print('Dynamic Content:', dynamic_element.text)
```

- 대기 조건 종류:
    - `presence_of_element_located`: 요소가 DOM에 존재할 때
    - `visibility_of_element_located`: 요소가 DOM에 존재하며 가시적일 때
    - `element_to_be_clickable`: 요소가 클릭 가능할 때

---

## Scraping JavaScript
JavaScript로 렌더링된 데이터는 일반적인 HTML 파싱 도구로는 접근할 수 없습니다. Selenium은 JavaScript 실행 기능을 제공해 이러한 데이터를 크롤링할 수 있습니다.

```python
result = driver.execute_script('return document.title;')
print('Page Title via JS:', result) # Page Title via JS: Example Domain
```

### Infinite Scroll
많은 웹사이트는 사용자가 페이지를 아래로 스크롤할 때 콘텐츠를 동적으로 로드합니다. Selenium을 사용하면 스크롤 동작을 시뮬레이션하고 콘텐츠가 로드될 때까지 기다릴 수 있습니다.

```python
import time

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

print('Scrolling Complete!')
```

---

## References
- [Python 공식 문서](https://docs.python.org/3/)
* [Selenium 문서](https://selenium-python.readthedocs.io/)
* [Webdriver Manager 문서](https://github.com/SergeyPirogov/webdriver_manager)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
