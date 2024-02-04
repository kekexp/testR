from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit 
from instr.py import *
from finalwin_app.py import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(Title1) 
        self.resize(W, H) 
    def initUI(self):
        self.St = QLabel(welctxt) 
        self.tx = QLabel(txtest) 
        self.bt = QPushButton(startxt) 
        self.vl = QVBoxLayout() 
 
        self.vl.addWidget(self.St, alignment = Qt.AlignTop) 
        self.vl.addWidget(self.tx, alignment = Qt.AlignTop) 
        self.vl.addWidget(self.bt, alignment = Qt.AlignCenter) 
        self.setLayout(self.vl) 
    def connects(self):
        self.bt.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()

class TestWin(QWidget):
     def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(Title2) 
        self.resize(W, H)
    def initUI(self):
        self.St2 = QLabel('Введите Ф.И.О.:') 
        self.st1 = QLineEdit('Ф.И.О.') 
        self.lfl = QLabel('Полных лет:') 
        self.tx1 = QLineEdit('0') 
        self.lol = QLabel(texting) 
        self.but = QPushButton('Начать первый тест') 
        self.st3 = QLineEdit('0') 
        self.kek = QLabel(exercises) 
        self.exer = QPushButton('Нач делать') 
        self.sld = QLabel('другие дела') 
        self.fin = QPushButton('Нач фин тест') 
        self.st4 = QLineEdit('0') 
        self.st5 = QLineEdit('0')
        self.nextbt = QPushButton('Отправить результаты')
        self.timer = QLabel = (Time)

        self.vl = QVBoxLayout() 
        self.vl2 = QVBoxLayout()
        self.hl = QHBoxLayout()

        self.vl.addWidget(St2, alignment= Qt.AlignTop)
        self.vl.addWidget(st1, alignment= Qt.AlignTop)
        self.vl.addWidget(lfl, alignment= Qt.AlignTop)
        self.vl.addWidget(tx1, alignment= Qt.AlignTop)
        self.vl.addWidget(lol, alignment= Qt.AlignTop)
        self.vl.addWidget(but, alignment= Qt.AlignTop)
        self.vl.addWidget(st3, alignment= Qt.AlignTop)
        self.vl.addWidget(kek, alignment= Qt.AlignTop)
        self.vl.addWidget(exer, alignment= Qt.AlignTop)
        self.vl.addWidget(sld, alignment= Qt.AlignTop)
        self.vl.addWidget(fin, alignment= Qt.AlignTop)
        self.vl.addWidget(st4, alignment= Qt.AlignTop)
        self.vl.addWidget(st5, alignment= Qt.AlignTop)
        self.vl.addWidget(nextbt, alignment= Qt.AlignCenter)
        self.vl.addWidget(St2, alignment= Qt.AlignTop)
        self.vl1.addWidget(timer, alignment= Qt.AlignCenter)

        self.hl.addLayout(vl)
        self.hl.addLayout(vl1)
        self.setLayout(hl)
    def connect(self):
        self.hide()
        self.fw = FinalWin()
