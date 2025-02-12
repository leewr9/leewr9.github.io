---
title: Data Storage
category: Crawling
tag: [Python, Crawling]
---

> 웹 크롤링을 통해 수집한 데이터는 저장하고 처리하는 단계가 필요합니다. 다양한 데이터 저장 방식(CSV, JSON, 데이터베이스 등)과 데이터를 효율적으로 정리하고 분석할 수 있는 방법이 필요하며, 클라우드 스토리지 서비스와 연동하여 데이터를 저장하고 관리하는 방법도 있습니다.

---

## Storage Methods
웹 크롤링을 통해 얻은 데이터는 여러 형식으로 저장할 수 있습니다. 가장 흔하게 사용되는 형식은 CSV, JSON과 같은 파일 형식과, `MySQL`, `MongoDB`와 같은 데이터베이스입니다. 데이터를 어떻게 저장할지는 주로 크롤링한 데이터의 성격과 활용 목적에 따라 결정됩니다.

- `CSV`: 간단한 테이블 형태의 데이터 저장에 적합하며, 텍스트 형식으로 저장됩니다.
- `JSON`: 계층적이고 중첩된 데이터를 저장하는 데 유용한 형식입니다.
- `Database`: 대량의 데이터를 저장하고 효율적으로 쿼리할 수 있는 데이터베이스를 사용합니다. MySQL, MongoDB 등 다양한 데이터베이스에 데이터를 저장할 수 있습니다.

---

## Storing Data

### CSV
CSV 파일은 간단하고 사람이 읽을 수 있는 형식으로 데이터를 저장하는 데 유용합니다. Python의 `csv` 라이브러리를 사용하여 데이터를 저장할 수 있습니다.

```python
import csv

# 데이터
data = [
    {"title": "Example 1", "url": "http://example.com/1"},
    {"title": "Example 2", "url": "http://example.com/2"}
]

# CSV 파일로 저장
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "url"])
    writer.writeheader()
    writer.writerows(data)
```

### JSON
JSON 파일은 더 복잡한 데이터 구조를 저장하는 데 적합합니다. `json` 라이브러리를 사용해 데이터를 JSON 형식으로 저장할 수 있습니다.

```python
import json

# 데이터
data = [
    {"title": "Example 1", "url": "http://example.com/1"},
    {"title": "Example 2", "url": "http://example.com/2"}
]

# JSON 파일로 저장
with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
```

### MySQL
MySQL을 사용하여 크롤링한 데이터를 데이터베이스에 저장할 수 있습니다. `mysql-connector-python`을 사용하여 Python에서 MySQL에 연결하고 데이터를 삽입할 수 있습니다.

```python
import mysql.connector

# MySQL 연결 설정
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

cursor = db.cursor()

# 데이터 삽입
cursor.execute("""
    CREATE TABLE IF NOT EXISTS crawled_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        url VARCHAR(255)
    )
""")

data = [("Example 1", "http://example.com/1"), ("Example 2", "http://example.com/2")]

# 데이터 삽입
cursor.executemany("INSERT INTO crawled_data (title, url) VALUES (%s, %s)", data)
db.commit()
```

### MongoDB
MongoDB는 NoSQL 데이터베이스로, 비정형 데이터를 처리하는 데 유용합니다. `pymongo` 라이브러리를 사용하여 MongoDB에 데이터를 저장할 수 있습니다.

```python
from pymongo import MongoClient

# MongoDB 연결 설정
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['crawled_data']

# 데이터 삽입
data = [
    {"title": "Example 1", "url": "http://example.com/1"},
    {"title": "Example 2", "url": "http://example.com/2"}
]

collection.insert_many(data)
```

---

## Preprocessing Data
웹 크롤링을 통해 수집한 데이터는 종종 중복되거나 누락된 값이 있을 수 있습니다. 이러한 데이터를 정리하고 분석하는 데 `Pandas` 라이브러리가 매우 유용합니다.

### Cleaning 
```python
import pandas as pd

# CSV 파일에서 데이터 읽기
df = pd.read_csv('output.csv')

# 중복 제거
df.drop_duplicates(inplace=True)

# 결측값 처리
df.fillna('', inplace=True)

# 정리된 데이터 확인
print(df.head())
```

### Analysis
`Pandas`를 사용하면 데이터를 쉽게 분석하고 통계를 낼 수 있습니다.

```python
# 데이터 분석: 특정 컬럼의 값의 빈도수 구하기
title_counts = df['title'].value_counts()

# 제목 빈도수
print(title_counts)
```

---

## Cloud Storage
클라우드 스토리지 서비스를 사용하면 데이터를 안전하게 저장하고, 필요할 때 쉽게 접근할 수 있습니다. `AWS S3`는 가장 널리 사용되는 클라우드 스토리지 중 하나입니다.

`AWS S3`에 데이터를 저장하려면 `boto3` 라이브러리를 사용하여 S3 버킷에 파일을 업로드할 수 있습니다.

```python
import boto3

# AWS S3 연결 설정
s3 = boto3.client('s3', 
                  aws_access_key_id='your-access-key', 
                  aws_secret_access_key='your-secret-key', 
                  region_name='us-east-1')

# 파일을 S3에 업로드
s3.upload_file('output.csv', 'your-bucket-name', 'output.csv')
```

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
