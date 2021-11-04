import os
import random

import pygame
from pygame.locals import (
    RLEACCEL
)

from constantes import RECURSOS, SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        """
        Constructor de la clase Enemy.
        Este constructor, tiene la imagen del misil y almacena su velocidad.
        """
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(os.path.join(RECURSOS, "missile.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = speed

    def update(self, score, level):
        """
        Mueve el misil por la pantalla, en caso de que se salga de la pantalla, lo elimina y le suma 10 puntos al jugador.
        :param score: objeto score
        :param level: objeto level
        """
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            score.update(level)
