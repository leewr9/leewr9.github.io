---
title: Interface Structure
category: PySide
tag: [Python, Qt, PySide]
---

> PySide를 활용한 GUI 애플리케이션 개발에서 가장 핵심이 되는 요소는 UI와 레이아웃입니다. 버튼, 입력창, 리스트, 체크박스 등 위젯들은 사용자와 프로그램 간의 상호작용을 담당하며, 이러한 위젯들을 어떻게 배치하고 구성할지는 애플리케이션의 사용성과 직결되는 중요한 설계 요소입니다. 

---

## UI 
PySide에서는 메인 UI를 구성하기 위해 여러 클래스가 제공됩니다. 목적에 맞는 클래스를 선택하면 구조적으로도 깔끔하고 유지보수하기 쉬운 앱을 만들 수 있습니다.

### QMainWindow
`QMainWindow`는 메뉴바, 툴바, 상태바, 중앙 위젯을 포함한 전형적인 데스크탑 애플리케이션을 만들 때 사용하는 클래스입니다. 중앙에는 `setCentralWidget()`을 사용해 실제 콘텐츠를 배치합니다.

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMainWindow")
        self.resize(300, 150)
        self.setCentralWidget(QLabel("Hello, World!"))

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
```

[![](/assets/posts/2025-07-20-Interface Structure.md/qmainwindow.png)](/assets/posts/2025-07-20-Interface Structure.md/qmainwindow.png)

### QWidget
`QWidget`은 가장 기본이 되는 UI 클래스로, 모든 위젯의 기반입니다. 단순한 구조나 메뉴/툴바 없이 직접 UI를 설계하고 싶은 경우에 적합합니다.

```python
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget")
        self.resize(300, 150)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Hello, World!"))
        self.setLayout(layout)

app = QApplication([])
window = MainWidget()
window.show()
app.exec()
```

[![](/assets/posts/2025-07-20-Interface Structure.md/qwidget.png)](/assets/posts/2025-07-20-Interface Structure.md/qwidget.png)

### QDialog
`QDialog`는 팝업 창, 설정 창, 알림 창 등 모달 또는 비모달 대화창을 만들 때 사용합니다. `exec()`를 통해 모달 형태로 표시할 수 있고, `show()`로 비모달 창으로도 사용할 수 있습니다.

```python
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog")
        self.resize(300, 150)
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Hello, World!"))
        self.setLayout(layout)

app = QApplication([])
dialog = MyDialog()
dialog.exec()
```

[![](/assets/posts/2025-07-20-Interface Structure.md/qdialog.png)](/assets/posts/2025-07-20-Interface Structure.md/qdialog.png)

### QStackedWidget
`QStackedWidget`은 여러 개의 위젯을 하나의 스택처럼 쌓아두고 하나씩 전환해서 보여주는 UI 구조를 만들 때 사용합니다. 메인 화면 전환, 단계별 화면 이동 등에 자주 쓰입니다.

```python
from PySide6.QtWidgets import QApplication, QWidget, QStackedWidget, QPushButton, QVBoxLayout

app = QApplication([])

page1 = QWidget()
layout1 = QVBoxLayout()

button1 = QPushButton("Page 1")
button1.clicked.connect(lambda: stack.setCurrentIndex(1))

layout1.addWidget(button1)
page1.setLayout(layout1)

page2 = QWidget()
layout2 = QVBoxLayout()

button2 = QPushButton("Page 2")
button2.clicked.connect(lambda: stack.setCurrentIndex(0))

layout2.addWidget(button2)
page2.setLayout(layout2)

stack = QStackedWidget()
stack.setWindowTitle("QStackedWidget")
stack.resize(300, 150)

stack.addWidget(page1)
stack.addWidget(page2)

stack.show()
app.exec()
```

[![](/assets/posts/2025-07-20-Interface Structure.md/qstackedwidget.png)](/assets/posts/2025-07-20-Interface Structure.md/qstackedwidget.png)

---

## Layout
PySide에서 레이아웃 클래스는 위젯들을 정렬하는 데 사용됩니다. 고정 위치를 사용하는 것보다 유연하게 창 크기에 맞춰 배치가 가능합니다.

### QVBoxLayout
`QVBoxLayout`은 위젯들을 수직 방향으로 정렬하는 레이아웃입니다. 단순히 위에서 아래로 쌓아 올리는 구조를 만들 때 사용합니다.

```python
from PySide6.QtWidgets import QVBoxLayout, QLabel

layout = QVBoxLayout()
layout.addWidget(QLabel("Top"))
layout.addWidget(QLabel("Bottom"))
```

[![](/assets/posts/2025-07-20-Interface Structure.md/qvboxlayout.png)](/assets/posts/2025-07-20-Interface Structure.md/qvboxlayout.png)

### QHBoxLayout
`QHBoxLayout`은 위젯들을 수평 방향으로 나란히 배치하는 레이아웃입니다. 가로로 메뉴 버튼이나 필드를 나열하고 싶을 때 유용합니다.

```python
from PySide6.QtWidgets import QHBoxLayout, QLabel

layout = QHBoxLayout()
layout.addWidget(QLabel("Left"))
layout.addWidget(QLabel("Right"))
```

[![](/assets/posts/2025-07-20-Interface Structure.md/qhboxlayout.png)](/assets/posts/2025-07-20-Interface Structure.md/qhboxlayout.png)

### QGridLayout
`QGridLayout`은 위젯들을 행과 열 단위로 배치하는 레이아웃입니다. 격자 모양의 배치가 필요할 때 사용하며, 다양한 크기의 위젯을 자연스럽게 조정할 수 있습니다.

```python
from PySide6.QtWidgets import QGridLayout, QLabel

layout = QGridLayout()
layout.addWidget(QLabel("Top Left\n0, 0"), 0, 0)
layout.addWidget(QLabel("Top Right\n0, 1"), 0, 1)
layout.addWidget(QLabel("Bottom Left\n0, 0"), 1, 0)
layout.addWidget(QLabel("Bottom Right\n0, 1"), 1, 1)
```

[![](/assets/posts/2025-07-20-Interface Structure.md/qgridlayout.png)](/assets/posts/2025-07-20-Interface Structure.md/qgridlayout.png)

### QFormLayout
`QFormLayout`은 레이블과 입력 필드를 나란히 배치할 때 사용하는 레이아웃입니다. 주로 설정 화면이나 사용자 정보 입력 폼에서 사용됩니다.

```python
from PySide6.QtWidgets import QFormLayout, QLineEdit

layout = QFormLayout()
layout.addRow("Name:", QLineEdit())
layout.addRow("Email:", QLineEdit())
layout.addRow("Phone:", QLineEdit())
layout.addRow("Address:", QLineEdit())
layout.addRow("Date of Birth:", QLineEdit())
```

[![](/assets/posts/2025-07-20-Interface Structure.md/qformlayout.png)](/assets/posts/2025-07-20-Interface Structure.md/qformlayout.png)

---

## References
- [PySide 공식 문서](https://doc.qt.io/qtforpython-6/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
