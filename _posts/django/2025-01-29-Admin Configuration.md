---
title: Admin Configuration
category: Django
tag: [Python, Django]
---

> Django의 Admin 사이트는 강력한 관리 인터페이스를 제공합니다. 기본적으로 Django에서 제공하는 이 기능은 모델 데이터를 CRUD(생성, 읽기, 업데이트, 삭제) 작업을 빠르게 수행할 수 있도록 도와줍니다.

---

## Site Configuration

Django Admin 사이트는 프로젝트 생성 시 기본적으로 활성화되어 있습니다.

```bash
python manage.py createsuperuser
```

명령어 실행 후 사용자 이름, 이메일, 비밀번호를 입력하여 관리자 계정을 생성합니다.

[![](\assets\posts\2025-01-29-Admin Configuration.md\admin.png)](\assets\posts\2025-01-29-Admin Configuration.md\admin.png)

```python
# urls.py

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

위 코드로 `/admin/` URL로 Admin 페이지에 접근할 수 있도록 설정합니다.

---

## Model Registration

모델을 Admin 사이트에서 관리하려면 `admin.py` 파일에 등록해야 합니다.

[![](\assets\posts\2025-01-29-Admin Configuration.md\register.png)](\assets\posts\2025-01-29-Admin Configuration.md\register.png)
[![](\assets\posts\2025-01-29-Admin Configuration.md\register_author.png)](\assets\posts\2025-01-29-Admin Configuration.md\register_author.png)

```python
# admin.py

from django.contrib import admin
from .models import Author, Post

admin.site.register(Author)
admin.site.register(Post)
```

위 코드로 `Author`와 `Post` 모델이 Admin 사이트에 표시됩니다.

---

## Customization

관리 인터페이스를 커스터마이징하려면 `ModelAdmin` 클래스를 사용합니다.

[![](\assets\posts\2025-01-29-Admin Configuration.md\custom.png)](\assets\posts\2025-01-29-Admin Configuration.md\custom.png)

```python
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published') # 리스트에 표시할 필드
    search_fields = ('title', 'content') # 검색창에서 검색할 필드
    readonly_fields = ('created_at') # 읽기 전용 필드
    list_filter = ('created_at', 'author') # 필터 추가
    ordering = ('-created_at',) # 정렬 기준

admin.site.register(Post, PostAdmin)
```

- `list_display`: 리스트 화면에서 표시할 필드.
- `search_fields`: 검색 가능한 필드.
- `readonly_fields`: 수정 불가능한 필드.
- `list_filter`: 사이드바 필터 추가.
- `ordering`: 기본 정렬 기준 설정.

### Filter

필터링을 더 세부적으로 설정하려면 커스텀 필터를 정의할 수 있습니다.

[![](\assets\posts\2025-01-29-Admin Configuration.md\filter.png)](\assets\posts\2025-01-29-Admin Configuration.md\filter.png)

```python
class PublishedFilter(admin.SimpleListFilter):
    title = '공개 여부'
    parameter_name = 'is_published'

    def lookups(self, request, model_admin):
        return [
            ('published', '공개됨'),
            ('draft', '비공개'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'published':
            return queryset.filter(is_published=True)
        elif self.value() == 'draft':
            return queryset.filter(is_published=False)

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', PublishedFilter) # 커스텀 필터 포함
```

### Action

데이터에 대한 사용자 정의 액션을 정의할 수 있습니다.

[![](\assets\posts\2025-01-29-Admin Configuration.md\action.png)](\assets\posts\2025-01-29-Admin Configuration.md\action.png)

```python
def mark_as_published(modeladmin, request, queryset):
    queryset.update(is_published=True)

mark_as_published.short_description = "선택된 게시글을 공개로 변경"

class PostAdmin(admin.ModelAdmin):
    actions = [mark_as_published]
```

---

## References

- [Django 공식 문서](https://www.djangoproject.com/)
- [Python 공식 문서](https://docs.python.org/3/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
