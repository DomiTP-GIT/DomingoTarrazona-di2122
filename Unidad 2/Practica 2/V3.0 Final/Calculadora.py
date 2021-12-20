import math
import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QKeySequence, QActionGroup, QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout, QGridLayout, \
    QToolBar, QStackedLayout, QHBoxLayout, QMessageBox, QDialog, QDialogButtonBox, QFileDialog


class MainWindow(QMainWindow):

    def __init__(self):
        """
        Constructor de la ventana principal
        """
        super().__init__()
        widget = QWidget()

        self.setWindowTitle("Calculadora")
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "img/calculator.png")))

        # Crea la toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.setMovable(False)

        # Acción de salir, con un shortcut que es Ctrl+Q
        close_action = QAction(QIcon(os.path.join(os.path.dirname(__file__), "img/cross.png")), "&Salir", self)
        close_action.setStatusTip("Cerrar el programa")
        close_action.setShortcut(QKeySequence("Ctrl+Q"))
        close_action.triggered.connect(self.close)

        # Crear el menú principal
        menu = self.menuBar()

        # Añadir el primer menú
        main_menu = menu.addMenu("&Menu")

        # Añadir al menú principal el submenú de modos
        mode_menu = main_menu.addMenu("&Mode")

        # Acción básica para cambiar a la calculadora normal
        self.basic_mode_action = QAction(QIcon(os.path.join(os.path.dirname(__file__), "img/calculator.png")),
                                         "&Normal", self)
        self.basic_mode_action.triggered.connect(self.change_to_normal)
        self.basic_mode_action.setCheckable(True)

        # Acción científica para cambiar a la calculadora científica
        self.scientific_mode_action = QAction(QIcon(os.path.join(os.path.dirname(__file__), "img/calculator_c.png")),
                                              "&Científica", self)
        self.scientific_mode_action.triggered.connect(self.change_to_scientific)
        self.scientific_mode_action.setCheckable(True)

        # Creo el QActionGroup para agrupar las accione de cambiar de calculadora
        modos = QActionGroup(self)

        # Hace que solo una de las acciones del grupo pueda estar seleccionada
        modos.setExclusive(True)

        # Añado las 2 opciones
        modos.addAction(self.basic_mode_action)
        modos.addAction(self.scientific_mode_action)

        # Añado las 2 opciones también al menú de modos
        mode_menu.addAction(self.basic_mode_action)
        mode_menu.addAction(self.scientific_mode_action)

        # Ruta de las imágenes
        self.guardando = os.path.join(os.path.dirname(__file__), "img/guardando.png")
        self.no_guardando = os.path.join(os.path.dirname(__file__), "img/no-guardando.png")

        # Acción de guardar, tiene un tooltip para que al pasar el ratón te muestre información.
        self.guardado = QAction(QIcon(self.no_guardando), "&Guardado")
        self.guardado.setToolTip("Guardar las operaciones en un archivo")
        self.guardado.setShortcut(QKeySequence("Ctrl+S"))
        self.guardado.setCheckable(True)
        self.guardado.triggered.connect(self.change_guardar)

        # Acción para seleccionar donde se guardará el archivo
        self.guardar = QAction(QIcon(os.path.join(os.path.dirname(__file__), "img/folders.png")), "&Ruta Guardado")
        self.guardar.setShortcut(QKeySequence("Ctrl+G"))
        self.guardar.setToolTip("Selecciona un archivo para guardar los resultados")
        self.guardar.triggered.connect(self.seleccionar_ruta)

        # Almacena la ruta de almacenado, por defecto crea un archivo en el mismo directorio llamado operaciones.txt
        self.ruta = os.path.join(os.path.dirname(__file__), "operaciones.txt")
        self.ruta_label = QLabel(self.ruta)

        # Añado la acción de guardar a la toolbar
        toolbar.addAction(self.guardado)

        # Añado la acción de guardar al menú principal
        main_menu.addAction(self.guardado)
        main_menu.addAction(self.guardar)

        # Añado un separador entre guardar y salir
        main_menu.addSeparator()

        # Añado la opción de salir
        main_menu.addAction(close_action)

        # Crea el texto de modo que se muestra en la barra inferior
        self.mode_label = QLabel("Normal")
        self.mode_label.setAlignment(Qt.AlignCenter)

        # Label que contiene una imagen, se situará en la toolbar y servirá para indicar el estado de guardado
        self.saving = QLabel()
        self.saving.setPixmap(QPixmap(self.no_guardando))
        self.saving.setAlignment(Qt.AlignCenter)

        # Recupera la barra de estado del QMainWindow para poder añadir el label del estado
        status = self.statusBar()
        status.addWidget(self.mode_label, 1)
        status.addWidget(self.saving, 1)
        status.addWidget(self.ruta_label, 1)

        # Cuadro de texto principal donde se muestran las operaciones y resultados
        self.label = QLabel("0")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setStyleSheet('border: 1px solid #0A86CC; border-radius: 4px; background-color: white; padding: 2px')

        # Label para mostrar un mensaje de Error en caso de que de error el cálculo de la operación
        self.error = QLabel("")
        self.error.setStyleSheet('color: red')

        # StackedLayout para almacenar la calculadora científica y normal
        self.stacked_layout = QStackedLayout()

        # Botones de la calculadora normal
        texto_botones_basica = ["AC", "π", "^", "<=",
                                "(", ")", "%", "/",
                                "7", "8", "9", "*",
                                "4", "5", "6", "-",
                                "1", "2", "3", "+",
                                "0", ".", "="]

        # Número de columnas de la calculadora normal
        num_col = 4

        # Genera los botones con los parámetros pasados y añade el widget que retorna al StackedLayout
        self.stacked_layout.addWidget(self.generar(num_col, texto_botones_basica))

        # Layout principal que tiene el label de las operaciones, el de error y el stacked layout que cambia
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.error)
        layout.addLayout(self.stacked_layout)

        # Texto de los botones de la parte izquierda de la calculadora científica
        texto_botones_cient_left = ["N", "Hyp", "Mod",
                                    "Mea", "Sin", "1/x",
                                    "on", "Cos", "x!",
                                    "Med", "Tan", "x2",
                                    "Dat", "Log", "xy",
                                    "CSt", "Ln", "x3",
                                    "x-10y"]

        # Texto de los botones de la parte central de la calculadora científica
        texto_botones_cient_mid = ["AC", "π", "^", "<=",
                                   "(", ")", "%", "/",
                                   "7", "8", "9", "*",
                                   "4", "5", "6", "-",
                                   "1", "2", "3", "+",
                                   "0", ".", "="]

        # Texto de los botones de la parte derecha de la calculadora científica
        texto_botones_cient_right = ["C", "DA",
                                     "VC", "MS",
                                     "(", "MC",
                                     ")", "MR",
                                     "+/-", "M+",
                                     "Shift"]

        # Número de columnas que tendrá cada parte de la calculadora científica
        num_col_iz = 3
        num_col_med = 4
        num_col_de = 2

        # Layout horizontal para almacenar los 3 widgets con los botones
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.generar(num_col_iz, texto_botones_cient_left))
        h_layout.addWidget(self.generar(num_col_med, texto_botones_cient_mid))
        h_layout.addWidget(self.generar(num_col_de, texto_botones_cient_right))

        # Creo un widget para meter el layout y poder introducirlo en el stacked layout
        w2 = QWidget()
        w2.setLayout(h_layout)
        self.stacked_layout.addWidget(w2)

        # Establezco el layout principal como el layout de widget
        widget.setLayout(layout)

        # Establezco widget como el widget central del QMainWindow
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

            # Si empieza por 0, reemplaza el texto por el número, ya que yo siempre pongo un 0 para que no esté vacío
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
                    # Al añadir espacios antes y después de las operaciones, al borrar tengo en cuenta si tengo que
                    # borrar más o menos caracteres
                    if text_in_label[-1] == " ":
                        self.label.setText(text_in_label[:-3])
                    else:
                        self.label.setText(text_in_label[:-1])

            elif text == "=":
                try:
                    # Reemplaza los caracteres especiales
                    text_in_label = text_in_label.replace("π", str(math.pi))
                    text_in_label = text_in_label.replace("^", "**")

                    # Calcula la operación
                    self.label.setText(str(eval(text_in_label)))

                    # Si está seleccionada la parte de guardar, guarda la operación y el resultado en un fichero
                    if self.guardado.isChecked():
                        try:
                            with open(self.ruta, 'a') as op:
                                op.write(f'{text_in_label} = {self.label.text()}' + "\n")
                        except PermissionError as e:
                            # Creo un popup en caso de que no tenga permisos para modificar el fichero
                            dlg = QMessageBox(self)
                            dlg.setWindowIcon(
                                QIcon(os.path.join(os.path.dirname(__file__), "img/calculator-warning.png")))
                            dlg.setWindowTitle("ERROR")
                            dlg.setText("Error al guardar la operación en el fichero:\n"
                                        "El programa no tiene permisos de escritura en el archivo\n"
                                        "No se guardará el historial.")
                            dlg.setStandardButtons(QMessageBox.Close)
                            dlg.setIcon(QMessageBox.Warning)
                            dlg.exec()
                except Exception:
                    self.error.setText("ERROR!")

            # Compruebo si está vacío el label para asignarle un 0 y que no esté en blanco
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

            # Compruebo si está vacío el label para asignarle un 0 y que no esté en blanco
            is_empty()

        def is_empty():
            """
            Comprueba si el texto está vacío
            """
            if len(self.label.text()) == 0 or self.label.text() == " ":
                self.label.setText("0")

        # Cada vez que se aprieta un botón borro el error, de esta forma, el error permanece en pantalla mientras no
        # se modifica nada, y al borrar o añadir se quita
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
        self.mode_label.setText("Normal")
        self.label.setText("0")
        self.error.setText("")

    def change_to_scientific(self):
        """
        Cambia el modo de la calculadora a Científica
        """
        self.stacked_layout.setCurrentIndex(1)
        self.mode_label.setText("Científica")
        self.label.setText("0")
        self.error.setText("")

    def change_guardar(self):
        """
        Cambia la imagen del statusbar y el icono
        """
        if self.guardado.isChecked():
            self.guardado.setIcon(QIcon(self.guardando))
            self.saving.setPixmap(QPixmap(self.guardando))
        else:
            self.guardado.setIcon(QIcon(self.no_guardando))
            self.saving.setPixmap(QPixmap(self.no_guardando))

    def seleccionar_ruta(self):
        """
        Muestra un diálogo para seleccionar un archivo
        """
        nueva_ruta = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "Text Files (*.txt)")
        if nueva_ruta:
            self.ruta = nueva_ruta[0]
            self.ruta_label.setText(self.ruta)

    def generar(self, num_col, texto_botones) -> QWidget:
        """
        Genera los botones con su texto, les añade la función para cuando se clican y les añade el shortcut.
        :param num_col: Número de columnas que tendrá.
        :param texto_botones: Array con el texto de los botones
        :return: QWidget con el QStackedLayout que contiene los botones
        """
        # Creo el widget que almacenará el QGridLayout
        widget = QWidget()

        # Creo el QGridLayout que almacenará los botones
        grid = QGridLayout()
        for i in range(len(texto_botones)):
            fil = i // num_col
            col = i % num_col

            # Crea el botón y le añade la función al hacer click y el shortcut
            btn = QPushButton(texto_botones[i])
            btn.clicked.connect(self.button_clicked)
            btn.setShortcut(QKeySequence(texto_botones[i]))
            btn.setStatusTip(texto_botones[i])
            if texto_botones[i] == "=":
                grid.addWidget(btn, fil, col, 1, 2)
                btn.setShortcut(QKeySequence('enter'))
                btn.setStatusTip("Enter")
            elif texto_botones[i] == "Shift":
                grid.addWidget(btn, fil, col, 1, 2, Qt.AlignCenter)
            else:
                grid.addWidget(btn, fil, col)
            if texto_botones[i] == "<=":
                btn.setShortcut(QKeySequence("Backspace"))
                btn.setStatusTip("Backspace")
            if texto_botones[i] == "AC":
                btn.setShortcut(QKeySequence("Esc"))
                btn.setStatusTip("Esc")

            # Añade el grid al widget
            widget.setLayout(grid)
        return widget

    def closeEvent(self, event):
        """
        Sobreescribo el método closeEvent del QMainWindow para que cuando cierre la ventana desde la X o llame a
        self.close, ejecute mi código personalizado.

        :param event: Evento
        """

        # Crea un diálogo, le pone un título y le añade 2 botones con sus funciones al hacer click
        exit_dlg = QDialog(self)
        exit_dlg.setWindowTitle("Cerrar Programa")
        btns = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        button_box = QDialogButtonBox(btns)

        # En caso de que se presione el botón Ok, cierra el programa
        button_box.accepted.connect(quit)

        # En caso de que se presione el botón Cancel, cierra el diálogo
        button_box.rejected.connect(exit_dlg.reject)

        # Layout para poner el mensaje y los botones
        layout = QVBoxLayout()
        message = QLabel("¿Quieres salir?")
        message.setAlignment(Qt.AlignCenter)
        layout.addWidget(message)
        layout.addWidget(button_box)

        exit_dlg.setLayout(layout)
        exit_dlg.exec()

        # Ignora el evento ya que si no, cierra siempre la ventana aunque le des a Cancel, y en caso de que le des a
        # Ok, cierro el programa
        event.ignore()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
