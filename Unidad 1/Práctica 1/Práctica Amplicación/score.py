class Score:
    def __init__(self):
        """
        Constructor de la clase Score.
        Almacena la puntuación.
        """
        self.score = 0

    def update(self, level):
        """
        Actualiza la puntuación y el nivel
        :param level: objeto level
        """
        self.score += 10
        if self.score > 500:
            level.set_level(int(self.score / 500) + 1)
