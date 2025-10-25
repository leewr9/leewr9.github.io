---
title: Event Handling
category: Django
tag: [Signal, Python, Django]
---

> Django는 특정 이벤트가 발생했을 때 자동으로 실행되는 콜백 함수를 정의할 수 있는 강력한 기능을 제공합니다. 이를 통해 Observer 패턴을 구현하고, 애플리케이션의 다양한 부분에서 발생하는 이벤트에 유연하게 반응할 수 있습니다.

---

## Signal

`Signal`은 특정 이벤트가 발생했을 때 자동으로 연결된 함수가 실행되도록 하는 메커니즘을 의미합니다. Signal을 사용하면 모델 객체의 생성, 수정, 삭제와 같은 생명주기 이벤트를 감지하고, 관련된 후처리 작업이나 알림, 로그 기록 등을 별도의 코드로 분리하여 깔끔하게 구현할 수 있습니다.

```python
# apps.py

from django.apps import AppConfig

class AppConfig(AppConfig):
    name = "app"

    def ready(self):
        import app.signals
```

`Signal`이 정상적으로 동작하도록 하기 위해서는 `apps.py` 파일에서 `ready` 메서드를 오버라이드하여 `receiver` 함수가 정의된 모듈을 임포트해야 합니다.

### pre_save

`pre_save`는 모델 객체가 데이터베이스에 저장되기 직전에 호출되는 `Signal`입니다. 이를 활용하면 객체가 저장되기 전에 데이터를 검증하거나, 특정 필드 값을 자동으로 설정하고 조정할 수 있습니다.

```python
from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=ModelName)
def your_model_pre_save(sender, instance, **kwargs):
    # 데이터 검증 또는 수정 로직
    if not instance.name:
        instance.name = "기본 이름"
```

### post_save

`post_save`는 모델 객체가 데이터베이스에 저장된 직후에 호출되는 `Signal`입니다. 이를 활용하면 저장된 데이터를 기반으로 추가 작업을 수행할 수 있습니다. post_save는 `pre_save`와 달리 저장이 완료된 상태이므로 신뢰할 수 있는 최종 데이터를 활용할 수 있습니다.

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=ModelName)
def your_model_post_save(sender, instance, created, **kwargs):
    if created:
        # 새 인스턴스가 생성된 경우 실행할 로직
        print(f"새 인스턴스가 생성되었습니다: {instance}")
    else:
        # 기존 인스턴스가 업데이트된 경우 실행할 로직
        print(f"인스턴스가 업데이트되었습니다: {instance}")
```

### pre_delete

`pre_delete`는 모델 객체가 데이터베이스에서 삭제되기 직전에 호출되는 `Signal`입니다. 이를 활용하면 객체가 삭제되기 전에 필요한 검증 작업이나 백업, 연관 데이터 정리 등을 수행할 수 있습니다.

```python
from django.db.models.signals import pre_delete
from django.dispatch import receiver
@receiver(pre_delete, sender=ModelName)
def your_model_pre_delete(sender, instance, **kwargs):
    # 삭제 전에 실행할 로직
    print(f"인스턴스가 삭제될 예정입니다: {instance}")
```

### post_delete

`post_delete`는 모델 객체가 데이터베이스에서 삭제된 직후에 호출되는 Signal입니다. 객체가 완전히 제거된 후에 실행되므로, 연관된 데이터 정리 등의 삭제 이후 후처리 작업에 적합합니다. post_delete는 `pre_delete`와 달리 데이터가 이미 제거된 상태이므로 주의가 필요합니다.

```python
from django.db.models.signals import post_delete
from django.dispatch import receiver
@receiver(post_delete, sender=ModelName)
def your_model_post_delete(sender, instance, **kwargs):
    # 삭제 후에 실행할 로직
    print(f"인스턴스가 삭제되었습니다: {instance}")
```

### m2m_changed

`m2m_changed`는 `ManyToManyField`에서 관계가 변경될 때 호출되는 `Signal`입니다. 객체 간 관계가 추가되거나 제거되거나 초기화될 때 발생하며, `action` 인자를 통해 어떤 종류의 변경이 발생했는지 구분할 수 있습니다. 이를 활용해 관계 변경 이벤트에 따른 후처리 작업을 수행할 수 있습니다.

```python
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
@receiver(m2m_changed, sender=ModelName.your_m2m_field.through)
def your_model_m2m_changed(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == "pre_add":
        print(f"관계가 추가되기 전: {pk_set}")
    elif action == "post_add":
        print(f"관계가 추가된 후: {pk_set}")
    elif action == "pre_remove":
        print(f"관계가 제거되기 전: {pk_set}")
    elif action == "post_remove":
        print(f"관계가 제거된 후: {pk_set}")
    elif action == "pre_clear":
        print("모든 관계가 제거되기 전")
    elif action == "post_clear":
        print("모든 관계가 제거된 후")
```

---

## Custom Signals

`Custom Signals`는 기본적으로 제공되는 `Signal` 외에, 개발자가 정의한 특정 이벤트를 처리할 때 사용됩니다. 비즈니스 로직에 맞는 독립적인 이벤트를 생성하고, `send()` 메서드를 통해 원하는 데이터를 전달하며, `receiver`에서 이를 받아 처리할 수 있습니다.

```python
from django.contrib.auth.models import User
from django.dispatch import Signal, receiver

custom_signal = Signal()

@receiver(custom_signal)
def custom_signal_receiver(sender, user, **kwargs):
    arg1 = kwargs.get("arg1")
    arg2 = kwargs.get("arg2")
    print(f"Custom signal received from sender: {sender.__name__}")
    print(f"user: {user.username}, arg1: {arg1}, arg2: {arg2}")

custom_signal.send(
    sender=User,  # User 클래스로 지정
    user=User(username="testuser"),
    arg1="value1",
    arg2="value2"
)

# Custom signal received from sender: User
# user: testuser, arg1: value1, arg2: value2
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
