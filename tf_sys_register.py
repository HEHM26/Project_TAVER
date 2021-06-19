import sys
from PyQt5.QtWidgets import *
from PySide2 import QtUiTools, QtGui
# from PySide2.Qtwidgets import QApplication, QMainWindow, QMessageBox
import tf_firebase


class SubWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.result

        self.setWindowTitle('Sub Window')
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()
        layout.addStretch(1)

        label = QLabel("가게명, 테이블 수, 위도, 경도 순서대로 입력해주세요")
        self.label = label

        cafeName = QLineEdit()
        font = cafeName.font()
        font.setPointSize(10)
        cafeName.setFont(font)
        self.cafeName = cafeName
        
        allTable = QLineEdit()
        font = allTable.font()
        font.setPointSize(10)
        allTable.setFont(font)
        self.allTable = allTable

        latitude = QLineEdit()
        font = latitude.font()
        font.setPointSize(10)
        latitude.setFont(font)
        self.latitude = latitude

        longitude = QLineEdit()
        font = longitude.font()
        font.setPointSize(10)
        longitude.setFont(font)
        self.longitude = longitude


        layout.addWidget(label)

        layout.addWidget(cafeName)

        layout.addWidget(allTable)

        layout.addWidget(latitude)

        layout.addWidget(longitude)

        subLayout = QHBoxLayout()

        # 확인
        btnOK = QPushButton("확인")
        btnOK.clicked.connect(self.onOKButtonClicked)

        # 취소
        btnCancel = QPushButton("취소")
        btnCancel.clicked.connect(self.onCancelButtonClicked)

        subLayout.addWidget(btnOK)
        subLayout.addWidget(btnCancel)
        layout.addLayout(subLayout)
        layout.addStretch(1)

        self.setLayout(layout)


    def onOKButtonClicked(self):
        allTable = int(self.allTable.text())
        cafeName = self.cafeName.text()
        latitude = float(self.latitude.text())
        longitude = float(self.longitude.text())

        self.result = tf_firebase.register_firebase(allTable, cafeName, latitude, longitude, 0)
        self.accept()

    def onCancelButtonClicked(self):
        self.reject()

    def showModal(self):
        return super().exec_()

