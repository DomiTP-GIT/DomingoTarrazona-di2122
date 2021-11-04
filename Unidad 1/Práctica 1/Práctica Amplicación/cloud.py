import os
import random

import pygame
from pygame.locals import (
    RLEACCEL
)

from constantes import RECURSOS, SCREEN_WIDTH, SCREEN_HEIGHT


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        """
        Constructor de la clase Cloud.
        Este constructor, tiene la imagen de la nube y almacena su velocidad.
        """
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(os.path.join(RECURSOS, "cloud.png")).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = -5

    def update(self):
        """
        Mueve el objeto en la pantalla y cuando se salga de ella lo borra.
        """
        self.rect.move_ip(self.speed, 0)
        if self.rect.right < 0:
            self.kill()
