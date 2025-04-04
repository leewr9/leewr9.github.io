---
title: File Management
category: Python
tag: [Python]
---

> 파일 입출력은 데이터를 파일에 저장하거나 파일에서 데이터를 읽는 작업을 처리하는 과정입니다. Python은 파일 작업을 위한 다양한 기능을 제공하며, 이를 통해 텍스트 파일, JSON 파일, CSV 파일, 바이너리 파일 등을 쉽게 처리할 수 있습니다.

---

## File
파일을 읽고 쓰는 것은 가장 기본적인 파일 작업입니다. Python에서는 `open()` 함수를 사용하여 파일을 열고, `read()`, `write()` 메서드로 파일을 처리합니다.

```python
# 텍스트 파일 쓰기
with open('example.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a sample text file.")

# 텍스트 파일 읽기
with open('example.txt', 'r') as file:
    content = file.read()
    print(content) # Hello, world!
                   # This is a sample text file.
```

- `r` 읽기: 파일이 존재해야 하며 읽기만 가능
- `w` 쓰기: 파일이 존재하면 덮어쓰기, 없으면 새로 생성
- `a` 추가: 파일이 존재하면 끝에 추가, 없으면 새로 생성
- `x` 새 파일 생성: 파일이 존재하면 오류 발생 (FileExistsError)
- `b` 이진 모드: 바이너리 파일 읽기/쓰기 (`rb`, `wb`)
- `t` 텍스트 모드: 텍스트 파일 읽기/쓰기 (기본값)
- `r+` 읽기 + 쓰기: 파일이 존재해야 하며, 수정 가능
- `w+` 쓰기 + 읽기: 파일이 존재하면 덮어쓰기, 없으면 새로 생성
- `a+` 추가 + 읽기: 파일이 존재하면 끝에 추가, 없으면 새로 생성

### Binary
바이너리 파일은 텍스트 형식이 아닌 이진 데이터를 처리하는 파일입니다. Python에서는 `rb`와 `wb` 모드로 바이너리 파일을 읽고 쓸 수 있습니다.

```python
# 바이너리 파일 쓰기
data = b"Hello, binary world!"
with open('example.bin', 'wb') as file:
    file.write(data)

# 바이너리 파일 읽기
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content) # b'Hello, binary world!'
```

---

## File Formats

### JSON
`JSON` 파일은 데이터를 직렬화하여 저장하는 데 사용됩니다. Python의 `json` 모듈을 사용하면 JSON 파일을 쉽게 읽고 쓸 수 있습니다.

```python
import json

# JSON 데이터 쓰기
data = {"name": "Alice", "age": 30, "city": "New York"}
with open('data.json', 'w') as file:
    json.dump(data, file)

# JSON 데이터 읽기
with open('data.json', 'r') as file:
    data_loaded = json.load(file)
    print(data_loaded) # {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

### CSV
`CSV` 파일은 데이터를 표 형식으로 저장하는 데 사용됩니다. Python의 `csv` 모듈을 사용하면 CSV 파일을 읽고 쓸 수 있습니다.

```python
import csv

# CSV 데이터 쓰기
data = [["name", "age", "city"], ["Alice", 30, "New York"], ["Bob", 25, "Los Angeles"]]
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# CSV 데이터 읽기
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) # ['name', 'age', 'city']
                   #         ['Alice', 30, 'New York']
                   #         ['Bob', 25, 'Los Angeles']
```

---

## References
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
