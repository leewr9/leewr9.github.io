---
title: Common Widgets
category: PySide
tag: [Python, Qt, PySide]
---

> PySide를 활용한 GUI 애플리케이션 개발에서 가장 핵심이 되는 요소는 바로 위젯입니다. 버튼, 입력창, 리스트, 체크박스 등 다양한 위젯들은 사용자와 프로그램 간 상호작용을 구성하는 데 필수적인 역할을 하며, 직관적인 UI를 만드는 데 기반이 됩니다.

---

## Display

### QLabel

`QLabel`은 텍스트나 이미지를 화면에 출력하는 기본 위젯으로, 정렬·폰트·스타일·이미지·HTML 등을 지원하며 출력 용도에 최적화되어 있습니다.

```python
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap

label = QLabel("Hello, PySide6!")
label.setAlignment(Qt.AlignCenter)

img_label = QLabel(self)
img_label.setPixmap(QPixmap("./img.png"))
img_label.setAlignment(Qt.AlignCenter)
```

[![](/assets/posts/2025-07-13-Common Widgets.md/qlabel.png)](/assets/posts/2025-07-13-Common Widgets.md/qlabel.png)

### QProgressBar

`QProgressBar`은 진행률을 시각적으로 표시하는 위젯으로, `setValue`, `setRange`, `setMaximum`, `setMinimum` 등을 사용하며 자동 갱신됩니다.

```python
from PySide6.QtWidgets import QProgressBar

progress = QProgressBar()
progress.setValue(75)
```

[![](/assets/posts/2025-07-13-Common Widgets.md/qprogressbar.png)](/assets/posts/2025-07-13-Common Widgets.md/qprogressbar.png)

### QTableWidget

`QTableWidget`은 행과 열로 구성된 2차원 표 형식의 데이터를 표시하는 위젯으로, 각 셀에 직접 위젯 삽입이 가능하고 `cellClicked`, `itemChanged` 등으로 상태 변화를 감지할 수 있습니다.

```python
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

table = QTableWidget(3, 2)
table.setHorizontalHeaderLabels(["Name", "Age"])

table.setItem(0, 0, QTableWidgetItem("Alice"))
table.setItem(0, 1, QTableWidgetItem("29"))
table.setItem(1, 0, QTableWidgetItem("Bob"))
table.setItem(1, 1, QTableWidgetItem("34"))
```

[![](/assets/posts/2025-07-13-Common Widgets.md/qtablewidget.png)](/assets/posts/2025-07-13-Common Widgets.md/qtablewidget.png)

### QListWidget

`QListWidget`은 스크롤 가능한 리스트에 항목을 표시하는 위젯으로, 항목 클릭·선택·드래그 등이 가능하며 `itemClicked`, `itemSelectionChanged` 등의 시그널로 인터랙션을 감지할 수 있습니다.

```python
from PySide6.QtWidgets import QListWidget

list_widget = QListWidget()
list_widget.addItems(["Hello", "Bye"])
list_widget.itemClicked.connect(
    lambda item: label.setText(f"{item.text()}, PySide6!")
)
```

[![](/assets/posts/2025-07-13-Common Widgets.md/qlistwidget.png)](/assets/posts/2025-07-13-Common Widgets.md/qlistwidget.png)

---

## Input

### QLineEdit

`QLineEdit`은 한 줄 텍스트 입력용 위젯으로, 플레이스홀더, 입력 제한, 비밀번호 모드 설정이 가능하며 `textChanged`, `editingFinished` 등의 시그널로 변경 감지가 가능합니다.

```python
from PySide6.QtWidgets import QLineEdit

line_edit = QLineEdit()
line_edit.setPlaceholderText("PySide6")

pw_line_edit = QLineEdit()
pw_line_edit.setPlaceholderText("Password")
pw_line_edit.setEchoMode(QLineEdit.Password)
```

[![](/assets/posts/2025-07-13-Common Widgets.md/qlineedit.png)](/assets/posts/2025-07-13-Common Widgets.md/qlineedit.png)

### QTextEdit

`QTextEdit`은 여러 줄의 텍스트 입력 또는 출력이 가능한 위젯으로, 일반 텍스트와 HTML을 모두 지원하며 `textChanged` 등을 통해 실시간 입력 감지가 가능합니다.

```python
from PySide6.QtWidgets import QTextEdit

text_edit = QTextEdit()
text_edit.setPlainText("Hello,\nPySide6!")
```

[![](/assets/posts/2025-07-13-Common Widgets.md/qtextedit.png)](/assets/posts/2025-07-13-Common Widgets.md/qtextedit.png)

### QSlider

`QSlider`은 슬라이드 막대를 통해 정수 값을 조절할 수 있는 위젯으로, 수평/수직 방향 모두 지원하며 `valueChanged` 시그널로 실시간 값 변경을 감지할 수 있습니다.

```python
from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt

slider = QSlider(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(100)
slider.setValue(6)
slider.valueChanged.connect(
  lambda value: label.setText(f"Hello, PySide{value}!")
)
```

[![](/assets/posts/2025-07-13-Common Widgets.md/qslider.png)](/assets/posts/2025-07-13-Common Widgets.md/qslider.png)

---

## Selection

### QCheckBox

`QCheckBox`은 체크 여부로 참/거짓을 표현하는 위젯으로, 여러 개 동시 선택이 가능하며 `stateChanged` 시그널을 통해 상태 변화 감지가 가능합니다.

```python
from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Qt

checkbox = QCheckBox("Bye")
checkbox.stateChanged.connect(
  lambda state: label.setText(
    "Bye, PySide6!" if Qt.CheckState(state) == Qt.Checked else "Hello, PySide6!"
  )
)
```

[![](/assets/posts/2025-07-13-Common Widgets.md/qcheckbox.png)](/assets/posts/2025-07-13-Common Widgets.md/qcheckbox.png)

### QRadioButton

`QRadioButton`은 여러 항목 중 하나만 선택할 수 있는 위젯으로, 같은 부모 위젯 안에 두면 자동으로 배타적 동작을 하며, 필요에 따라 `QButtonGroup`으로 묶어 그룹 단위 제어나 시그널 처리를 할 수 있고, `toggled` 시그널로 선택 상태 변화를 감지할 수 있습니다.

```python
from PySide6.QtWidgets import QRadioButton

hello_radio = QRadioButton("Hello")
bye_radio = QRadioButton("Bye")
hello_radio.toggled.connect(
  lambda: label.setText("Hello, PySide6!" if hello_radio.isChecked() else "Bye, PySide6!")
)
```

[![](/assets/posts/2025-07-13-Common Widgets.md/qradiobutton.png)](/assets/posts/2025-07-13-Common Widgets.md/qradiobutton.png)

### QComboBox

`QComboBox`은 드롭다운 리스트에서 항목 하나를 선택하는 위젯으로, 항목 추가·삭제·검색이 가능하며 `currentIndexChanged`, `currentTextChanged` 시그널로 선택 변화 감지가 가능합니다.

```python
from PySide6.QtWidgets import QComboBox

combobox = QComboBox()
combobox.addItems(["Hello", "Bye"])
combobox.currentIndexChanged.connect(
    lambda i: label.setText(f"{combobox.currentText()}, PySide6!")
)
```

[![](/assets/posts/2025-07-13-Common Widgets.md/qcombobox.png)](/assets/posts/2025-07-13-Common Widgets.md/qcombobox.png)

---

## References

- [PySide 공식 문서](https://doc.qt.io/qtforpython-6/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
