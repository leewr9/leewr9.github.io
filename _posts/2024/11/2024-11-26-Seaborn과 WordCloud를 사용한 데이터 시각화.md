---
title: Seaborn과 WordCloud를 사용한 데이터 시각화
category: Study
tag: [Education, WordCloud, Seaborn, Visualization, Python]
---

<nav class="post-toc" markdown="1">
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

## `Seaborn` 라이브러리란?
> `Seaborn`은 데이터 시각화를 위한 파이썬 라이브러리로, `matplotlib`을 기반으로 더 직관적이고 세련된 그래프를 생성할 수 있습니다. 
특히 통계적 데이터 시각화에 강점이 있습니다.

### 1. 주요 기능  
* 다양한 그래프 제공: 산점도, 선 그래프, 박스플롯, 히트맵 등  
* 범주형 데이터와 연속형 데이터를 쉽게 시각화  
* `pandas` 데이터프레임과 통합하여 데이터 처리 가능  

### 2. Scatter Plot (산점도)
[![](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/scatterplot.png)](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/scatterplot.png)

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 샘플 데이터: 아이리스 데이터셋
iris = sns.load_dataset('iris')

sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=iris)
plt.title("Petal Length vs Petal Width by Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.show()
```

### 3. Line Plot (선 그래프)
[![](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/lineplot.png)](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/lineplot.png)


```python
import seaborn as sns
import matplotlib.pyplot as plt

# 샘플 데이터: 아이리스 데이터셋
iris = sns.load_dataset('iris')

sns.lineplot(x='species', y='petal_length', data=iris, estimator='mean')
plt.title("Mean Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Mean Petal Length (cm)")
plt.show()
```


### 4. Bar Plot (막대 그래프)
[![](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/barplot.png)](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/barplot.png)

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 샘플 데이터: 아이리스 데이터셋
iris = sns.load_dataset('iris')

sns.barplot(x='species', y='sepal_length', data=iris, estimator='mean', ci=None)
plt.title("Mean Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Mean Sepal Length (cm)")
plt.show()
```

### 5. Box Plot (상자 그림) 
[![](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/boxplot.png)](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/boxplot.png)

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 샘플 데이터: 아이리스 데이터셋
iris = sns.load_dataset('iris')

sns.boxplot(x='species', y='sepal_length', data=iris)
plt.title("Sepal Length Distribution by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.show()
```


### 5. relplot()
> `relplot()`은 scatterplot()과 lineplot()을 통합한 함수로, 관계형 데이터를 시각화할 때 유용합니다.

#### 산점도 (Scatter Plot)
[![](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/relplot-scatter.png)](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/relplot-scatter.png)

```python
# 샘플 데이터: 팁 데이터셋
tips = sns.load_dataset('tips')

sns.relplot(x='total_bill', y='tip', hue='sex', kind='scatter', data=tips)
plt.title("Total Bill vs Tip by Gender")
plt.show()
```

#### 선 그래프 (Line Plot)
[![](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/relplot-line.png)](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/relplot-line.png)

```python
# 샘플 데이터: FMRI 데이터셋
fmri = sns.load_dataset('fmri')

sns.relplot(x='timepoint', y='signal', kind='line', hue='event', style='region', data=fmri)
plt.title("FMRI Signal over Time by Event and Region")
plt.show()
```

* 주요 매개변수
  * x, y: 시각화할 축 데이터
  * hue: 데이터에 따라 색상을 다르게 표시
  * col, row: 데이터를 서브플롯으로 나누기 위한 변수
  * kind: 그래프 유형 선택 ('scatter', 'line')
* 그래프 종류	산점도, 선 그래프 모두 지원	각각 별도 함수로 구분
* 서브플롯 생성	가능 (Facet 기능 제공)
* 사용 난이도	한 번에 다양한 그래프 설정 가능	단일 그래프에 특화
* 유연성, 범용적, 확장성 높음, 특정 그래프에 특화된 기능 제공

## `WordCloud` 라이브러리란?
> `WordCloud`는 텍스트 데이터를 시각화하여 단어의 빈도수를 구름 모양으로 표현하는 라이브러리입니다. 
자주 등장하는 단어일수록 크기가 커집니다.

### 1. 주요 기능
* 텍스트 데이터의 주요 키워드를 시각적으로 표현
* 다양한 모양, 색상, 글꼴 적용 가능

### 2. WordCloud 기본 예제
[![](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/wordcloud.png)](/assets/posts/2024-11-26-Seaborn과 WordCloud로 데이터 시각화하기/wordcloud.png)

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 샘플 텍스트 데이터
text = """The movie was fantastic! The characters were well-developed and the plot was gripping. 
          The visual effects were stunning, and the soundtrack was memorable. Highly recommend!"""

# 워드클라우드 생성
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# 워드클라우드 시각화
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

* 설명
  * WordCloud(): 워드클라우드 객체를 생성하며 너비, 높이, 배경색을 설정합니다.
  * .generate(): 텍스트 데이터를 기반으로 워드클라우드를 생성합니다.
  * plt.imshow(): 워드클라우드를 시각화합니다.
  * plt.axis('off'): 축을 숨겨 깔끔한 출력을 제공합니다.

## 참고자료
* [Seaborn 공식 문서](https://seaborn.pydata.org/)
* [WordCloud 공식 문서](https://github.com/amueller/word_cloud)
