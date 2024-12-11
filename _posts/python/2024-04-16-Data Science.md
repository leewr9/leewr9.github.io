---
title: Data Science
category: Python
tag: [Data, Python]
---

> Python은 데이터 분석, 처리, 시각화 및 수집에 매우 유용한 라이브러리들을 제공합니다.

---

## Data Analysis and Processing

### Numpy
Numpy는 수치 계산을 위한 라이브러리로, 고성능 다차원 배열 객체와 다양한 수학 함수를 제공합니다.

```python
import numpy as np

# Numpy 배열 생성
arr = np.array([1, 2, 3, 4, 5])
print(arr) # [1 2 3 4 5]

# 배열의 기본적인 수학 연산
arr2 = arr * 2
print(arr2) # [2 4 6 8 10]
```
Numpy 배열은 Python의 리스트보다 훨씬 빠르고 효율적으로 데이터를 처리할 수 있습니다. 여러 수학 함수들을 사용하여 배열을 다룰 수 있습니다.

### Pandas
Pandas는 데이터 분석을 위한 강력한 라이브러리로, `DataFrame`과 `Series`라는 두 가지 주요 자료형을 제공합니다.

```python
import pandas as pd

# DataFrame 생성
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

print(df)
#
#       Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
```
Pandas는 데이터 프레임을 이용해 데이터를 쉽게 탐색하고 분석할 수 있는 다양한 기능을 제공합니다. `read_csv()`, `head()`, `describe()` 등 데이터 분석에 유용한 메서드를 제공합니다.

```python
# CSV 파일 읽기
df = pd.read_csv('data.csv')

# 데이터프레임의 첫 5행 출력
print(df.head()) # 첫 5행
```

---

## Data Visualization

### Matplotlib
Matplotlib는 가장 널리 사용되는 데이터 시각화 라이브러리 중 하나로, 다양한 그래프를 그릴 수 있습니다.

![](\assets\posts\2024-04-16-Data Science\matplotlib.png)
```python
import matplotlib.pyplot as plt

# 간단한 선 그래프
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show() # 선 그래프
```
`plt.plot()`을 사용하여 선 그래프, `plt.bar()`를 사용하여 막대 그래프 등 다양한 시각화 기능을 제공합니다.

### Seaborn
Seaborn은 Matplotlib을 기반으로 한 고급 시각화 라이브러리로, 더 아름답고 간편한 시각화 도구를 제공합니다.

![](\assets\posts\2024-04-16-Data Science\seaborn.png)
```python
import seaborn as sns

# 데이터 로딩
tips = sns.load_dataset("tips")

# 산점도 그리기
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Scatterplot of Total Bill vs Tip")
plt.show() # 산점도
```
Seaborn은 `scatterplot()`, `barplot()`, `heatmap()` 등 다양한 시각화 기능을 제공합니다. 데이터의 관계를 더욱 직관적으로 시각화할 수 있습니다.

---

## Data Collection

### Web Scraping
웹 스크래핑은 웹사이트에서 데이터를 추출하는 기술입니다. `BeautifulSoup`과 `requests` 라이브러리를 사용하여 웹 페이지를 크롤링할 수 있습니다.

```python
import requests
from bs4 import BeautifulSoup

# 웹 페이지 요청
url = "https://example.com"
response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 원하는 데이터 추출
title = soup.title.string
print(title) # 웹 페이지의 제목
```
웹 스크래핑은 데이터를 자동으로 추출하여 분석에 활용할 수 있게 해줍니다. 웹 페이지에서 HTML 태그를 탐색하고 필요한 데이터를 가져옵니다.

### API Usage 
API(Application Programming Interface)는 프로그램이 다른 프로그램과 데이터를 주고받을 수 있게 해주는 인터페이스입니다. Python에서 `requests` 라이브러리를 사용하여 API에 접근할 수 있습니다.

```python
import requests

# API 요청
url = "https://api.github.com/users/octocat"
response = requests.get(url)

# JSON 데이터 처리
data = response.json()
print(data['login']) # octocat (GitHub 사용자 로그인 이름)
```
API는 JSON 형식으로 데이터를 반환하며, 이를 쉽게 처리할 수 있습니다. 위의 예시에서는 GitHub API를 호출하여 사용자 정보를 가져왔습니다.

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
