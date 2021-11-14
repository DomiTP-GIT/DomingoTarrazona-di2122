from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from config import max, nor, min, btn_x, btn_y


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Tamaño de la pantalla real
        self.my_screen = QScreen.availableGeometry(QApplication.primaryScreen())
        
        # Establecer tamaño máximo y mínimo
        self.setMaximumSize(max)
        self.setMinimumSize(min)

        # Crea los botones
        self.pybutton_max = QPushButton('Maximitza', self)
        self.pybutton_nor = QPushButton('Normalitza', self)
        self.pybutton_min = QPushButton('Minimitza', self)

        # Llama a las funciones cuando haces click
        self.pybutton_max.clicked.connect(self.maximitza)
        self.pybutton_nor.clicked.connect(self.normalitza)
        self.pybutton_min.clicked.connect(self.minimitza)

        # Establecer el tamaño de los botones
        self.pybutton_max.resize(btn_x, btn_y)
        self.pybutton_nor.resize(btn_x, btn_y)
        self.pybutton_min.resize(btn_x, btn_y)

        # Establece el tamaño de la pantalla a Normalitza, mueve los botones, cambia el título y centra la pantalla
        self.cambia_tamany(nor, "Normalitzat")
        
        # Deshabilita el botón de Normalitza
        self.pybutton_nor.setDisabled(True)

    def maximitza(self):
        """
        Cambia el tamaño a Maximizat y deshabilita el botón
        """
        self.cambia_tamany(max, "Maximizat")
        self.pybutton_max.setDisabled(True)

    def normalitza(self):
        """
        Cambia el tamaño a Normalitzat y deshabilita el botón
        """
        self.cambia_tamany(nor, "Normalitzat")
        self.pybutton_nor.setDisabled(True)

    def minimitza(self):
        """
        Cambia el tamaño a Minimitzat y deshabilita el botón
        """
        self.cambia_tamany(min, "Minimitzat")
        self.pybutton_min.setDisabled(True)

    def cambia_tamany(self, tamany, txt):
        """
        Cambia el tamaño al especificado, activa los botones, mueve la pantalla al centro, mueve los botones a sus
        posiciones y cambia el título de la pantalla.

        :param tamany: Tamaño
        :param txt: Título pantalla
        """
        self.pybutton_max.setEnabled(True)
        self.pybutton_nor.setEnabled(True)
        self.pybutton_min.setEnabled(True)
        self.setFixedSize(tamany)
        self.move((self.my_screen.width() - tamany.width()) / 2, (self.my_screen.height() - tamany.height()) / 2)
        self.pybutton_max.move((tamany.width() / 5) - (btn_x / 2), (tamany.height() / 2) - (btn_y / 2))
        self.pybutton_nor.move((tamany.width() / 2) - (btn_x / 2), (tamany.height() / 2) - (btn_y / 2))
        self.pybutton_min.move((tamany.width() / 1.25) - (btn_x / 2), (tamany.height() / 2) - (btn_y / 2))
        self.setWindowTitle(txt)


if __name__ == "__main__":
    app = QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    app.exec()
