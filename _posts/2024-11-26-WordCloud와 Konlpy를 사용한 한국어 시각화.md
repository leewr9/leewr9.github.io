---
title: WordCloud와 Konlpy를 사용한 한국어 시각화
category: Study
tag: [Education, WordCloud, Konlpy, Visualization, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

## `Konlpy` 라이브러리란?
> `Konlpy`는 한국어 텍스트 분석을 위한 다양한 기능과 **형태소 분석기**를 제공하는 라이브러리로, 
단어 빈도수 분석 등 다양한 텍스트 분석을 쉽게 할 수 있습니다.

### 1. Hannanum
[![](/assets/posts/2024-11-26-WordCloud와 Konlpy를 사용한 한국어 시각화/hannanum.png)](/assets/posts/2024-11-26-WordCloud와 Konlpy를 사용한 한국어 시각화/hannanum.png)

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Hannanum

# Hannanum 분석기 사용
hannanum = Hannanum()

text = '안녕하세요. 파이썬을 사용하여 형태소 분석을 하고 있습니다.'

nouns = hannanum.nouns(text)
print(nouns)
text_nouns = ' '.join(nouns)

wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf', width=800, height=800, background_color='white').generate(text_nouns)

plt.figure(figsize=(8, 8), dpi=80)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

### 2. Kkma
[![](/assets/posts/2024-11-26-WordCloud와 Konlpy를 사용한 한국어 시각화/kkma.png)](/assets/posts/2024-11-26-WordCloud와 Konlpy를 사용한 한국어 시각화/kkma.png)

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Kkma

# Kkma 분석기 사용
kkma = Kkma()

text = '안녕하세요. 파이썬을 사용하여 형태소 분석을 하고 있습니다.'

nouns = kkma.nouns(text)
print(nouns)
text_nouns = ' '.join(nouns)

wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf', width=800, height=800, background_color='white').generate(text_nouns)

plt.figure(figsize=(8, 8), dpi=80)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

### 3. Komoran
[![](/assets/posts/2024-11-26-WordCloud와 Konlpy를 사용한 한국어 시각화/komoran.png)](/assets/posts/2024-11-26-WordCloud와 Konlpy를 사용한 한국어 시각화/komoran.png)

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Komoran

# Komoran 분석기 사용
komoran = Komoran()

text = '안녕하세요. 파이썬을 사용하여 형태소 분석을 하고 있습니다.'

nouns = komoran.nouns(text)
print(nouns)
text_nouns = ' '.join(nouns)

wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf', width=800, height=800, background_color='white').generate(text_nouns)

plt.figure(figsize=(8, 8), dpi=80)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

### 4. Okt
[![](/assets/posts/2024-11-26-WordCloud와 Konlpy를 사용한 한국어 시각화/okt.png)](/assets/posts/2024-11-26-WordCloud와 Konlpy를 사용한 한국어 시각화/okt.png)

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt

# Okt 분석기 사용
okt = Okt()

text = '안녕하세요. 파이썬을 사용하여 형태소 분석을 하고 있습니다.'

nouns = okt.nouns(text)
print(nouns)
text_nouns = ' '.join(nouns)

wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf', width=800, height=800, background_color='white').generate(text_nouns)

plt.figure(figsize=(8, 8), dpi=80)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

### 5. Mecab
```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Mecab

# Mecab 분석기 사용
mecab = Mecab()

text = '안녕하세요. 파이썬을 사용하여 형태소 분석을 하고 있습니다.'

nouns = mecab.nouns(text)
print(nouns)
text_nouns = ' '.join(nouns)

wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf', width=800, height=800, background_color='white').generate(text_nouns)

plt.figure(figsize=(8, 8), dpi=80)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

* 설명
  * 위 형태소 분석기를 사용하여 한국어 텍스트에서 명사만 추출합니다.
  * 한글을 제대로 표시하기 위해 한글 폰트를 지정해줍니다. (font_path='path')

## 형태소 분석기의 장점과 단점 비교

| 분석기 | 장점 | 단점 | 추천 사용 사례 | 10만 문자 소요시간 |
| - | - | - | - | - |
| Hannanum | 구문 분석 가능, 기능이 다양함 | 속도가 느릴 수 있음, 최신 텍스트 분석에는 부족	 | 구문 분석 필요, 정확성 중요 | 8.8초 |
| Kkma | 구문 분석과 함께 정확한 형태소 분석 지원 | 상대적으로 속도가 느림, 메모리 소모가 큼 | 구문 분석 필요, 높은 정확도 요구 | 35.7초 |
| Komoran | 높은 정확도, 빠른 분석 속도 | 설치가 복잡, 메모리 소모가 큼 | 고정밀 분석 필요, 속도 중시 | 25.6초 |
| Okt	| 설치 간편, 품사 태깅과 명사 추출이 용이 | 속도가 느릴 수 있음, 정확도가 약간 낮음 | 빠른 프로토타입, 간단한 텍스트 분석 | 2.5초 |
| Mecab	| 매우 빠르고 정확한 성능, 대규모 텍스트 처리 | 설치가 복잡하고, 환경 설정에 따라 달라짐, 윈도우는 지원하지 않음 | 속도가 중요한 경우, 대용량 데이터 처리 | 0.2초 |

## 참고 자료
* [WordCloud 공식 문서](https://github.com/amueller/word_cloud)
* [Konlpy 공식 문서](https://konlpy.org/)
