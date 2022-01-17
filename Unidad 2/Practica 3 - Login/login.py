import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFormLayout, \
    QLineEdit


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOGIN - PyLogin")
        self.main = None
        layout = QVBoxLayout()
        form = QFormLayout()
        self.user = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        form.addRow("Usuario", self.user)
        form.addRow("Contraseña", self.password)
        btn = QPushButton("Login")
        btn.clicked.connect(self.login)
        btn.setShortcut(QKeySequence('enter'))
        self.aviso = QLabel()
        layout.addLayout(form)
        layout.addWidget(btn)
        layout.addWidget(self.aviso)
        self.setLayout(layout)

    def login(self):
        self.aviso.setText("")
        if self.user.text() == "admin" and self.password.text() == "1234":
            self.main = MainWindow("admin")
            self.main.show()
            self.close()
        elif self.user.text() == "admin" and self.password.text() != "1234":
            self.aviso.setText("Contraseña incorrecta")
        elif self.user.text() == "user" and self.password.text() == "1234":
            self.main = MainWindow("user")
            self.main.show()
            self.close()
        elif self.user.text() == "user" and self.password.text() != "1234":
            self.aviso.setText("Contraseña incorrecta")
        elif self.user.text() != "user" or self.user.text() != "admin":
            self.aviso.setText("Ese usuario no existe")


class MainWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.setWindowTitle("PyLogin")
        self.login = None
        label = QLabel(f"Sesión iniciada como {user}")
        status = self.statusBar()
        status.addWidget(label)
        self.cerrar_sesion = QAction("&Cerrar sesión")
        self.salir = QAction("&Salir")
        self.cerrar_sesion.triggered.connect(self.cerrar)
        self.salir.triggered.connect(self.close)
        menu = self.menuBar()
        menu_principal = menu.addMenu("&Menu")
        menu_principal.addAction(self.cerrar_sesion)
        menu_principal.addAction(self.salir)
        self.setCentralWidget(label)

    def cerrar(self):
        self.login = LoginWindow()
        self.login.show()
        self.close()


app = QApplication(sys.argv)
w = LoginWindow()
w.show()
app.exec()
