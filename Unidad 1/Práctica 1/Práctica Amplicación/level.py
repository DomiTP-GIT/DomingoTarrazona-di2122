class Levels:
    def __init__(self):
        """
        Constructor de la clase Levels.
        Almacena los niveles
        """
        self.level = 1

    def set_level(self, new_level):
        """
        Cambia el nivel al que se le pasa por parámetros
        :param new_level: nuevo nivel
        """
        self.level = new_level
