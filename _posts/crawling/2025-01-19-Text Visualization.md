---
title: Text Visualization
category: Crawling
tag: [Konlpy, WordCloud, Python, Crawling]
---

> 텍스트를 분석하는 데 있어서 중요한 과정 중 하나는 형태소 분석입니다. 형태소 분석을 통해 단어를 더 작은 의미 있는 단위로 나누고, 각 단어의 품사를 태깅할 수 있습니다. 

---

## WordCloud Visualization
`WordCloud`는 텍스트 데이터에서 단어들의 빈도를 기반으로 시각화하는 기법입니다. 주로 텍스트에서 중요한 단어들을 강조하고, 자주 등장하는 단어들을 크게 표시하여 데이터의 주요 특징을 시각적으로 쉽게 파악할 수 있도록 도와줍니다.

```bash
pip install wordcloud nltk
```

[![](\assets\posts\{{ page.name }}\wordcloud.png)](\assets\posts\{{ page.name }}\wordcloud.png)
```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = '''
Data science is a field that extracts meaningful information from complex data.
Machine learning and artificial intelligence are key technologies in data science, used in various fields.
'''

# WordCloud 생성
wordcloud = WordCloud(background_color='white').generate(text)

# WordCloud 출력
plt.figure(figsize=(5, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```
위 코드는 주어진 텍스트에서 단어를 분리한 후, 빈도수를 기반으로 `WordCloud`를 생성하여 중요한 단어들이 더 크게 표시되도록 시각화합니다.

### Tagging
`nltk`는 텍스트에 품사 태깅을 하는 라이브러리입니다. 품사 태깅은 단어가 문장에서 어떤 역할을 하는지 알려주기 때문에, 이를 시각화하면 텍스트의 구조를 더 잘 이해할 수 있습니다.

```python
import nltk
from nltk.tokenize import word_tokenize

# 텍스트를 단어로 토큰화
words = word_tokenize(text)

# 품사 태깅 수행
pos_tags = nltk.pos_tag(words)

print(pos_tags)
# [('Data', 'NNP'), ('science', 'NN'), ('is', 'VBZ'), ('a', 'DT'), ('field', 'NN'), ('that', 'WDT'), ('extracts', 'VBZ'), ('meaningful', 'JJ'), ('information', 'NN'), ('from', 'IN'), ('complex', 'JJ'), ('data', 'NNS'), ('.', '.'), ('Machine', 'NNP'), ('learning', 'NN'), ('and', 'CC'), ('artificial', 'JJ'), ('intelligence', 'NN'), ('are', 'VBP'), ('key', 'JJ'), ('technologies', 'NNS'), ('in', 'IN'), ('data', 'NNS'), ('science', 'NN'), (',', ','), ('used', 'VBN'), ('in', 'IN'), ('various', 'JJ'), ('fields', 'NNS'), ('.', '.')] 
```
- `NN`: 명사
- `VBZ`: 동사
- `JJ`: 형용사
- `DT`: 한정사
- `IN`: 전치사

---

## Konlpy Visualization
`Konlpy`는 한국어 텍스트의 형태소 분석을 위한 라이브러리로, 텍스트를 분석하여 명사, 동사, 형용사 등의 품사를 추출할 수 있습니다. 이 정보를 시각화하면 텍스트에서 어떤 형태소들이 중요한지, 자주 사용되는지 알 수 있습니다.

```bash
pip install konlpy
```

[![](\assets\posts\{{ page.name }}\konlpy.png)](\assets\posts\{{ page.name }}\konlpy.png)

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt

okt = Okt()

text = '''
데이터 과학은 복잡한 데이터에서 의미 있는 정보를 추출하는 과학입니다.
기계 학습과 인공지능은 데이터 과학의 핵심 기술로, 다양한 분야에서 활용되고 있습니다.
'''

nouns = okt.nouns(text)
text_nouns = ' '.join(nouns)

wordcloud = WordCloud(font_path='malgun.ttf', background_color='white').generate(text_nouns)

plt.figure(figsize=(8, 8), dpi=80)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

위 코드는 `Okt` 분석기를 사용하여 텍스트에서 형태소를 추출하고, 이를 기반으로 빈도수를 막대 그래프로 시각화합니다. 이를 통해 텍스트에서 자주 등장하는 형태소를 확인할 수 있습니다.

### Tagging
`Okt` 분석기는 품사 태깅도 지원합니다. 품사 태깅은 단어가 문장에서 어떤 역할을 하는지 알려주기 때문에, 이를 시각화하면 텍스트의 구조를 더 잘 이해할 수 있습니다.

```python
# 품사 태깅 수행
pos_tags = okt.pos(text)

print(pos_tags)
# [('\n', 'Foreign'), ('데이터', 'Noun'), ('과학', 'Noun'), ('은', 'Josa'), ('복잡한', 'Adjective'), ('데이터', 'Noun'), ('에서', 'Josa'), ('의미', 'Noun'), ('있는', 'Adjective'), ('정보', 'Noun'), ('를', 'Josa'), ('추출', 'Noun'), ('하는', 'Verb'), ('과학', 'Noun'), ('입니다', 'Adjective'), ('.', 'Punctuation'), ('\n', 'Foreign'), ('기계', 'Noun'), ('학습', 'Noun'), ('과', 'Josa'), ('인공', 'Noun'), ('지능', 'Noun'), ('은', 'Josa'), ('데이터', 'Noun'), ('과학', 'Noun'), ('의', 'Josa'), ('핵심', 'Noun'), ('기술', 'Noun'), ('로', 'Josa'), (',', 'Punctuation'), ('다양한', 'Adjective'), ('분야', 'Noun'), ('에서', 'Josa'), ('활용', 'Noun'), ('되고', 'Verb'), ('있습니다', 'Adjective'), ('.', 'Punctuation'), ('\n', 'Foreign')]
```
- `Noun`: 명사
- `Verb`: 동사
- `Adjective`: 형용사
- `Josa`: 조사

| 분석기 | 장점 | 단점 | 추천 사용 사례 | 10만 문자 소요시간 |
| - | - | - | - | - |
| Hannanum | 구문 분석 가능, 기능이 다양함 | 속도가 느릴 수 있음, 최신 텍스트 분석에는 부족	 | 구문 분석 필요, 정확성 중요 | 8.8초 |
| Kkma | 구문 분석과 함께 정확한 형태소 분석 지원 | 상대적으로 속도가 느림, 메모리 소모가 큼 | 구문 분석 필요, 높은 정확도 요구 | 35.7초 |
| Komoran | 높은 정확도, 빠른 분석 속도 | 설치가 복잡, 메모리 소모가 큼 | 고정밀 분석 필요, 속도 중시 | 25.6초 |
| Okt	| 설치 간편, 품사 태깅과 명사 추출이 용이 | 속도가 느릴 수 있음, 정확도가 약간 낮음 | 빠른 프로토타입, 간단한 텍스트 분석 | 2.5초 |
| Mecab	| 매우 빠르고 정확한 성능, 대규모 텍스트 처리 | 설치가 복잡하고, 환경 설정에 따라 달라짐, 윈도우는 지원하지 않음 | 속도가 중요한 경우, 대용량 데이터 처리 | 0.2초 |

---

## References
- [Konlpy 공식 문서](https://konlpy.org/en/latest/)
- [WorldCloud 공식 문서](https://github.com/amueller/word_cloud/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class='post-toc' markdown='1'>
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
