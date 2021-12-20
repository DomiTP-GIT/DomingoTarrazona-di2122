import math
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout, QGridLayout, \
    QHBoxLayout


class MainWindow(QMainWindow):

    def __init__(self):
        """
        Constructor de la ventana principal
        """
        super().__init__()
        widget = QWidget()

        self.setWindowTitle("Calculadora")

        self.label = QLabel("0")
        self.label.setAlignment(Qt.AlignRight)

        self.error = QLabel("")

        grid = QGridLayout()

        self.texto_botones = ["AC", "π", "^", "<=",
                              "(", ")", "%", "/",
                              "7", "8", "9", "*",
                              "4", "5", "6", "-",
                              "1", "2", "3", "+",
                              "0", ".", "="]

        self.botones = list()

        num_col = 4

        for i in range(len(self.texto_botones)):
            fil = i // num_col
            col = i % num_col
            btn = QPushButton(self.texto_botones[i])
            btn.setFixedSize(40, 40)
            btn.clicked.connect(self.button_clicked)
            self.botones.append(btn)
            if self.texto_botones[i] == "=":
                grid.addWidget(btn, fil, col, fil, col + 1, Qt.AlignCenter)
                btn.setFixedSize(80, 40)
            else:
                grid.addWidget(btn, fil, col)

        layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.error)
        h_layout.addWidget(self.label)
        layout.addLayout(h_layout)
        layout.addLayout(grid)
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def button_clicked(self):
        """
        Detecta cuando un botón es pulsado
        """
        self.error.setText("")
        btn_text = self.sender().text()

        especiales = ["AC", "<=", "="]

        if btn_text.isdigit():
            self.add_num(btn_text)
        elif btn_text in especiales:
            self.fun(btn_text)
        else:
            self.add_op(btn_text)

    def add_num(self, text):
        """
        Añade un número
        :param text: Texto del botón seleccionado
        """
        text_in_label = self.label.text()
        if text_in_label.startswith("0"):
            self.label.setText(text)
        else:
            self.label.setText(text_in_label + text)

    def fun(self, text):
        """
        Controla los botones especiales
        :param text: Texto del botón seleccionado
        """
        text_in_label = self.label.text()
        if text == "AC":
            self.label.setText("0")
        elif text == "<=":
            if len(text_in_label) > 0:
                if text_in_label[-1] == " ":
                    self.label.setText(text_in_label[:-3])
                else:
                    self.label.setText(text_in_label[:-1])

        elif text == "=":
            try:
                text_in_label = text_in_label.replace("π", str(math.pi))
                text_in_label = text_in_label.replace("^", "**")
                self.label.setText(str(eval(text_in_label)))
            except Exception as e:
                self.error.setText("ERROR!")

        self.is_empty()

    def add_op(self, text):
        """
        Añade la operación
        :param text: Texto del botón seleccionado
        """
        text_in_label = self.label.text()

        if text_in_label.startswith("0"):
            self.label.setText("")

        text_in_label = self.label.text()

        if text == "." or text == "^":
            self.label.setText(f'{text_in_label}{text}')
        else:
            self.label.setText(f'{text_in_label} {text} ')

        self.is_empty()

    def is_empty(self):
        """
        Comprueba si el texto está vacío
        """
        if len(self.label.text()) == 0 or self.label.text() == " ":
            self.label.setText("0")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
