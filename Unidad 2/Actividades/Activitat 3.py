import argparse

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, args):
        super().__init__()

        if args.title:
            self.setWindowTitle(args.title)
        else:
            self.setWindowTitle("title")

        if args.button_text:
            button = QPushButton(args.button_text, self)
        else:
            button = QPushButton("button", self)

        if args.fixed_size:
            if args.size:
                self.setFixedSize(QSize(args.size[0], args.size[1]))
            else:
                print("Tienes que poner el parámetro -s SIZE SIZE para poder tener la ventana fija.")
        self.setCentralWidget(button)


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--title", help="Title of application", action='store')
parser.add_argument("-b", "--button-text", help="Button text", action='store')
parser.add_argument("-f", "--fixed-size", help="Window fixed size", action='store_true')
parser.add_argument("-s", "--size", help="Size of windows", action='store', nargs=2, type=int)
arguments = parser.parse_args()

app = QApplication()

window = MainWindow(arguments)

window.show()

app.exec()
