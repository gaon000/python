import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import serial
import time

# cansatData = serial.Serial('COM17')
form_class = uic.loadUiType("C:\dd2.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)
        self.RIGHT.clicked.connect(self.right)
        self.LEFT.clicked.connect(self.left)
        self.UP.clicked.connect(self.up)

    def right(self):
        # cansatData.write('R')
        self.show_status()
        self.textEdit.setText('오른쪽으로 이동')
    def left(self):
        # cansatData.write('L')
        self.show_status()
        self.textEdit.setText('왼쪽으로 이동')
    def up(self):
        # cansatData.write('U')
        self.show_status()
        self.textEdit.setText('앞쪽으로 이동')

    def btn_clicked(self):
        self.textEdit.setText('정보 수신 확인')

    def btn2_clicked(self):
        self.textEdit.setText('수분 및 ph농도 측정')

    def show_ph(self):
        self.ph.display(self.DataSplit[0])

    def show_liquid(self):
        self.liquid.display(self.DataSplit[1])

    def show_status(self):
        self.status.setStyleSheet("QLabel { background-color : rgb(220, 220, 220); color : red; }");
        self.status.setText('ON')
        #status.setText, setStyleSheet를 이용한 ON,OFF 신호에 따른 색상과 텍스트 변화

app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()
app.exec_()
