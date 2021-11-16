import random
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Press me")
        btn.setCheckable(True)
        btn.clicked.connect(lambda checked: self.button_clicked(checked))
        self.setCentralWidget(btn)

    def button_clicked(self, checked):
        print(checked, random.randint(0, 10))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
