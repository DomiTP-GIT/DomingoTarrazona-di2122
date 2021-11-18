import sys
import random

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    num_random = Signal(bool, int)
    def __init__(self):
        super().__init__()
        self.num_random.connect(self.imprimir)
        btn = QPushButton("Press me")
        btn.setCheckable(True)
        btn.clicked.connect(self.button_clicked)
        self.setCentralWidget(btn)
        
    def button_clicked(self, checked):
        self.num_random.emit(checked, random.randint(0, 10))
        
    def imprimir(self, checked, random):
        print(checked, random)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
