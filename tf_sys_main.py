
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from tf_sys_register import SubWindow

import tf_yolo
import tf_firebase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()
        layout.addStretch(1)

        label = QLabel("TAVER")
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        self.label = label

        code = QLabel("미지정")
        code.setAlignment(Qt.AlignCenter)
        font = code.font()
        font.setPointSize(10)
        code.setFont(font)
        self.code = code

        btn1 = QPushButton("등록")
        btn1.clicked.connect(self.onButtonClicked)

        btn2 = QPushButton("실행")
        btn2.clicked.connect(self.onButtonPlay)

        layout.addWidget(label)
        layout.addWidget(code)
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        layout.addStretch(1)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def onButtonClicked(self):
        win = SubWindow()
        win.showModal()

        self.code.setText(win.result)

    def onButtonPlay(self):
        saturation = tf_yolo.load_yolo()
        try:
            tf_firebase.update_firebase(str(self.code.text()), saturation)
        except Exception as e:
            print(e)


    def show(self):
        super().show()


