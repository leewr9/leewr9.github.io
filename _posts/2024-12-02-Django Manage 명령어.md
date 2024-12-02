---
title: Django Manage 명령어
category: Study
tag: [Education, Django, Python]
---

<nav class='post-toc' markdown='1'>
  <h4>Table of Content</h4>
* TOC
{:toc}
</nav>

{% raw %}

## loaddata와 dumpdata
### 1. dumpdata (데이터 백업)
> dumpdata는 Django의 데이터베이스 데이터를 JSON, XML 등으로 내보내는 명령어입니다.

```bash
python manage.py dumpdata [app_label] [model_name] --indent 2 > data.json

# app_label: 특정 앱의 데이터를 백업 (예: myapp)
# model_name: 특정 모델의 데이터만 백업 (예: MyModel)
# --indent: 출력 JSON의 들여쓰기 설정
```

* 모든 데이터 백업
```bash
python manage.py dumpdata --indent 2 > all_data.json
```

* 특정 앱 데이터 백업
```bash
python manage.py dumpdata myapp --indent 2 > myapp_data.json
```

* 특정 모델 데이터 백업
```bash
python manage.py dumpdata myapp.MyModel --indent 2 > mymodel_data.json
```

### 2. loaddata (데이터 복원)
> loaddata는 JSON, XML 등의 파일에서 데이터를 데이터베이스로 로드하는 명령어입니다.

```bash
python manage.py loaddata data.json
```

* 전체 데이터 복원

```bash
python manage.py loaddata all_data.json
```

* 특정 데이터 복원

```bash
python manage.py loaddata myapp_data.json
```

* 모든 데이터 삭제

```bash
python manage.py flush
```

## 사용자 정의 관리 명령어
> Django는 사용자 정의 관리 명령어를 추가할 수 있도록 management/commands 디렉토리를 제공합니다. 이를 통해 python manage.py 명령어를 확장할 수 있습니다.

```bash
myapp/
├── management/
│   ├── __init__.py
│   └── commands/
│       ├── __init__.py
│       └── my_command.py
```

```python
# my_command.py

from django.core.management.base import BaseCommand
from myapp.models import MyModel

class Command(BaseCommand):
    help = '이 명령어는 MyModel의 데이터를 출력합니다.'

    def handle(self, *args, **kwargs):
        data = MyModel.objects.all()
        for item in data:
            self.stdout.write(f'{item}')
```

```bash
python manage.py my_command
```

```bash
python manage.py my_command --help

# 이 명령어는 MyModel의 데이터를 출력합니다.
```


## 참고 자료
* [Django 공식 문서](https://docs.djangoproject.com/en/stable/)

{% endraw %}