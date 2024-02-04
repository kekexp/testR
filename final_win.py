from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit 
from inst import*
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.appear()
        self.initUI()
        self.connect
        self.show()
    def set_appear(self):
        self.setWindowTitle(Title3)
        self.resize(W, H)

    def initUI(self):
        text = QLable('Индекс Руфье:', Fin)
        text2 = QLable('Работоспособностье сердца:', ind)

        line = QVBoxLayout()

        line.addWidget(text, alignment = Qt.AlignCenter)
        line.addWidget(winner, alignment = Qt.AlignCenter)
