---
title: Seaborn and Visualization
category: Crawling
tag: [Seaborn, Python, Crawling]
---

> 웹 크롤링 후 얻은 데이터를 시각화하는 것은 데이터를 이해하고 분석하는 데 매우 중요한 과정입니다. Seaborn을 사용하여 데이터 분석을 시각화할 수 있게 도와줍니다.

---

## Seaborn Visualization
`Seaborn`은 Python에서 데이터를 시각화하는 데 매우 유용한 라이브러리입니다. `Matplotlib`을 기반으로 하여 통계적 데이터를 쉽게 시각화할 수 있도록 도와줍니다. `Seaborn`을 사용하면 데이터의 분포, 관계, 트렌드 등을 직관적으로 분석할 수 있습니다.

```bash
pip install seaborn
```

### Histplot
![](\assets\posts\2024-04-19-Seaborn and Visualization\histplot.png)
```python
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
tips = sns.load_dataset('tips')

sns.histplot(tips['total_bill'], kde=True) # KDE는 커널 밀도 추정
plt.show() 
```

### Boxplot
![](\assets\posts\2024-04-19-Seaborn and Visualization\boxplot.png)
```python
sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()
```

### Scatterplot
![](\assets\posts\2024-04-19-Seaborn and Visualization\scatterplot.png)
```python
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.show()
```

### Lmplot 
![](\assets\posts\2024-04-19-Seaborn and Visualization\lmplot.png)
```python
sns.lmplot(x='total_bill', y='tip', data=tips)
plt.show()
```

### Swarmplot 
![](\assets\posts\2024-04-19-Seaborn and Visualization\swarmplot.png)
```python
sns.swarmplot(x='total_bill', y='tip', data=tips)
plt.show()
```

---

## Replot
Seaborn의 `replot()` 기능을 사용하면 기존의 플롯을 분할 또는 재사용하거나 새 데이터를 적용하여 업데이트할 수 있습니다.

### Splitting
![](\assets\posts\2024-04-19-Seaborn and Visualization\replot-splittingl.png)
```python
# relplot을 사용하여 col과 row로 데이터를 분할
sns.relplot(
    x='total_bill', 
    y='tip', 
    hue='sex', 
    col='time',      # 'time' 컬럼을 기준으로 열을 나누기 (Lunch, Dinner)
    row='sex',       # 'sex' 컬럼을 기준으로 행을 나누기 (Male, Female)
    data=tips
)

plt.show() # 'time'과 'sex'에 따른 산점도 플롯
```

### Replotting
![](\assets\posts\2024-04-19-Seaborn and Visualization\replot-total_bill.png)
![](\assets\posts\2024-04-19-Seaborn and Visualization\replot-size.png)
```python
# 첫 번째 플롯
sns.set_theme(style='whitegrid')
sns.relplot(x='total_bill', y='tip', kind='line', data=tips)
plt.show()

# 두 번째 플롯, 다른 데이터로 재플로팅
sns.relplot(x='size', y='tip', kind='line', data=tips)
plt.show()
```

---

## References
- [Python 공식 문서](https://docs.python.org/3/)
- [Seaborn 공식 문서](https://seaborn.pydata.org/)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
