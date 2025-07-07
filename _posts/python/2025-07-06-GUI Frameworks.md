---
title: GUI Frameworks
category: Python
tag: [Kivy, Tkinter, PySide, PyQt, Qt, Python]
---

> Python으로 데스크탑 애플리케이션을 개발할 때, 어떤 GUI 프레임워크를 선택하느냐는 개발 생산성과 사용자 경험, 그리고 배포 전략에 큰 영향을 미칩니다. 각 프레임워크는 고유한 기능과 철학을 가지고 있으며, 용도와 목적에 따라 적절한 선택이 필요합니다.

---

## Qt
`Qt`는 C++로 개발된 크로스플랫폼 애플리케이션 프레임워크로, 풍부한 GUI 위젯과 다양한 기능을 제공합니다.
Windows, macOS, Linux 등 여러 운영체제를 지원하며, Python에서는 Qt를 바인딩한 `PyQt`와 `PySide`를 통해 Qt의 강력한 기능을 활용할 수 있습니다.

### PyQt 
`PyQt`는 방대한 커뮤니티와 튜토리얼을 갖춘 안정적인 Qt 바인딩이지만, `GPL` 라이선스로 인해 상업용 소프트웨어에서는 라이선스 구매가 필요하다는 단점이 있습니다.

```python
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
app.setApplicationName("PyQt Hello World")

label = QLabel("Hello, World!")
label.setAlignment(Qt.AlignCenter)
label.resize(300, 50)
label.show()

app.exec()
```

[![](/assets/posts/2025-07-06-GUI Frameworks.md/pyqt.png)](/assets/posts/2025-07-06-GUI Frameworks.md/pyqt.png)

### PySide
`PySide`는 `LGPL` 라이선스를 적용해 상업용으로 자유롭게 사용 가능하며, Qt 공식 바인딩으로 최신 기능을 빠르게 지원하지만, PyQt보다 상대적으로 자료와 커뮤니티가 적은 편입니다.

```python
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])
app.setApplicationName("PySide Hello World")

label = QLabel("Hello, World!")
label.resize(300, 50)
label.show()

app.exec()
```

[![](/assets/posts/2025-07-06-GUI Frameworks.md/pyside.png)](/assets/posts/2025-07-06-GUI Frameworks.md/pyside.png)

---

## Tkinter
`Tkinter`는 Python 표준 라이브러리에 포함되어 있어 별도 설치 없이 바로 사용할 수 있는 기본 GUI 툴킷입니다. 간단한 UI를 빠르게 만들기에 적합하지만, 디자인과 기능이 다소 제한적입니다.

```python
import tkinter as tk

root = tk.Tk()
root.title("Tkinter Hello World")
root.geometry("300x50")

label = tk.Label(root, text="Hello, World!")
label.pack()

root.mainloop()
```

[![](/assets/posts/2025-07-06-GUI Frameworks.md/tkinter.png)](/assets/posts/2025-07-06-GUI Frameworks.md/tkinter.png)

---

## Kivy
`Kivy`는 터치 및 제스처를 지원하며, 모바일 및 멀티터치 앱 개발에 최적화된 크로스 플랫폼 프레임워크입니다. GPU 가속을 활용하여 성능이 뛰어나며, Android 및 iOS 앱 개발에도 사용됩니다.

```python
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (300, 50)

class HelloWorldApp(App):
    def build(self):
        self.title = 'Kivy Hello World'
        return Label(text='Hello, World!')

if __name__ == '__main__':
    HelloWorldApp().run()
```

[![](/assets/posts/2025-07-06-GUI Frameworks.md/kivy.png)](/assets/posts/2025-07-06-GUI Frameworks.md/kivy.png)

---

## References
- [Python 공식 문서](https://docs.python.org/3/)
- [Qt 공식 문서](https://doc.qt.io/qtforpython-6/)
- [Kivy 공식 문서](https://kivy.org/doc/stable/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
