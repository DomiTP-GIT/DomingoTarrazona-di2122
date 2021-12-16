import math
import os
import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QKeySequence, QActionGroup, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout, QGridLayout, \
    QToolBar, QStackedLayout, QHBoxLayout, QMessageBox


class MainWindow(QMainWindow):

    def __init__(self):
        """
        Constructor de la ventana principal
        """
        super().__init__()
        widget = QWidget()

        self.setWindowTitle("Calculadora")

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.setMovable(False)

        close_action = QAction("&Salir", self)
        close_action.setStatusTip("Cerrar el programa")
        close_action.setShortcut(QKeySequence("Ctrl+Q"))
        close_action.triggered.connect(self.close)

        menu = self.menuBar()

        main_menu = menu.addMenu("&Menu")

        mode_menu = main_menu.addMenu("&Mode")

        self.basic_mode_action = QAction("&Normal", self)
        self.basic_mode_action.triggered.connect(self.change_to_normal)
        self.basic_mode_action.setCheckable(True)
        self.scientific_mode_action = QAction("&Científica", self)
        self.scientific_mode_action.triggered.connect(self.change_to_scientific)
        self.scientific_mode_action.setCheckable(True)

        modos = QActionGroup(self)
        modos.setExclusive(True)
        modos.addAction(self.basic_mode_action)
        modos.addAction(self.scientific_mode_action)

        mode_menu.addAction(self.basic_mode_action)
        mode_menu.addAction(self.scientific_mode_action)

        icon = os.path.join(os.path.dirname(__file__), "img/save.png")
        self.guardar = QAction(QIcon(icon), "&Guardar")
        self.guardar.setToolTip("Guardar las operaciones en un archivo")
        self.guardar.setShortcut(QKeySequence("Ctrl+S"))
        self.guardar.setCheckable(True)

        toolbar.addAction(self.guardar)

        main_menu.addAction(self.guardar)

        main_menu.addSeparator()

        main_menu.addAction(close_action)

        self.status_text = QLabel("Normal")

        status = self.statusBar()
        status.addWidget(self.status_text)

        self.label = QLabel("0")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setStyleSheet('border: 1px solid #0A86CC; border-radius: 4px; background-color: white; padding: 2px')

        self.error = QLabel("")
        self.error.setStyleSheet('color: red')

        self.stacked_layout = QStackedLayout()

        texto_botones_basica = ["AC", "π", "^", "<=",
                                "(", ")", "%", "/",
                                "7", "8", "9", "*",
                                "4", "5", "6", "-",
                                "1", "2", "3", "+",
                                "0", ".", "="]

        num_col = 4

        self.stacked_layout.addWidget(self.generar(num_col, texto_botones_basica))

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.error)
        layout.addLayout(self.stacked_layout)

        texto_botones_cient_left = ["N", "Hyp", "Mod",
                                    "Mea", "Sin", "1/x",
                                    "on", "Cos", "x!",
                                    "Med", "Tan", "x2",
                                    "Dat", "Log", "xy",
                                    "CSt", "Ln", "x3",
                                    "x-10y"]

        texto_botones_cient_mid = ["AC", "π", "^", "<=",
                                   "(", ")", "%", "/",
                                   "7", "8", "9", "*",
                                   "4", "5", "6", "-",
                                   "1", "2", "3", "+",
                                   "0", ".", "="]

        texto_botones_cient_right = ["C", "<=",
                                     "AC", "MS",
                                     "(", "MC",
                                     ")", "MR",
                                     "+/-", "M+",
                                     "Shift"]

        num_col_iz = 3
        num_col_med = 4
        num_col_de = 2

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.generar(num_col_iz, texto_botones_cient_left))
        h_layout.addWidget(self.generar(num_col_med, texto_botones_cient_mid))
        h_layout.addWidget(self.generar(num_col_de, texto_botones_cient_right))

        w2 = QWidget()
        w2.setLayout(h_layout)

        self.stacked_layout.addWidget(w2)

        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.stacked_layout.setCurrentIndex(0)

        self.basic_mode_action.setChecked(True)

    def button_clicked(self):
        """
        Detecta cuando un botón es pulsado
        """

        def add_num(text):
            """
            Añade un número
            :param text: Texto del botón seleccionado
            """
            text_in_label = self.label.text()
            if text_in_label.startswith("0"):
                self.label.setText(text)
            else:
                self.label.setText(text_in_label + text)

        def fun(text):
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
                    if self.guardar.isChecked():
                        operaciones = os.path.join(os.path.dirname(__file__), "operaciones.txt")
                        try:
                            with open(operaciones, 'a') as op:
                                op.write(f'{text_in_label} = {self.label.text()}' + "\n")
                        except PermissionError as e:
                            dlg = QMessageBox(self)
                            dlg.setWindowTitle("ERROR")
                            dlg.setText("Error al guardar la operación en el fichero:\n"
                                        "El programa no tiene permisos de escritura en el archivo\n"
                                        "No se guardarán los resultados en el archivo.")
                            dlg.setStandardButtons(QMessageBox.Close)
                            dlg.setIcon(QMessageBox.Warning)
                            dlg.exec()
                except Exception:
                    self.error.setText("ERROR!")

            is_empty()

        def add_op(text):
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

            is_empty()

        def is_empty():
            """
            Comprueba si el texto está vacío
            """
            if len(self.label.text()) == 0 or self.label.text() == " ":
                self.label.setText("0")

        self.error.setText("")
        btn_text = self.sender().text()

        especiales = ["AC", "<=", "="]

        if btn_text.isdigit():
            add_num(btn_text)
        elif btn_text in especiales:
            fun(btn_text)
        else:
            add_op(btn_text)

    def change_to_normal(self):
        """
        Cambia el modo de la calculadora a Normal
        """
        self.stacked_layout.setCurrentIndex(0)
        self.status_text.setText("Normal")
        self.label.setText("0")
        self.error.setText("")

    def change_to_scientific(self):
        """
        Cambia el modo de la calculador a Científica
        """
        self.stacked_layout.setCurrentIndex(1)
        self.status_text.setText("Científica")
        self.label.setText("0")
        self.error.setText("")

    def generar(self, num_col, texto_botones) -> QWidget:
        """
        Genera los botones con su texto, les añade la función para cuando se clican y les añade el shortcut.

        :param num_col: Número de columnas que tendrá.
        :param texto_botones: Array con el texto de los botones
        :return: QWidget con el QStackedLayout que contiene los botones
        """
        widget = QWidget()
        grid = QGridLayout()
        for i in range(len(texto_botones)):
            fil = i // num_col
            col = i % num_col
            btn = QPushButton(texto_botones[i])
            btn.clicked.connect(self.button_clicked)
            btn.setShortcut(QKeySequence(texto_botones[i]))
            if texto_botones[i] == "=":
                grid.addWidget(btn, fil, col, 1, 2)
                btn.setShortcut(QKeySequence('enter'))
            elif texto_botones[i] == "Shift":
                grid.addWidget(btn, fil, col, 1, 2, Qt.AlignCenter)
            else:
                grid.addWidget(btn, fil, col)
            if texto_botones[i] == "<=":
                btn.setShortcut(QKeySequence("Delete"))
            widget.setLayout(grid)
        return widget


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
