import os
import random

import pygame
from pygame.locals import (
    RLEACCEL
)

from constantes import RECURSOS, SCREEN_WIDTH, SCREEN_HEIGHT


class Shield(pygame.sprite.Sprite):
    def __init__(self):
        """
        Constructor de la clase Shield
        Esta clase genera un objeto que al obtenerlo te salva de un cohete y se rompe.
        """
        super(Shield, self).__init__()
        self.surf = pygame.transform.scale(pygame.image.load(os.path.join(RECURSOS, "Shield.png")).convert(), (25, 30))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    def update(self):
        """
        Mueve el objeto en la pantalla y en caso de que se salga de ella lo borra.
        """
        self.rect.move_ip(-2.5, 0)
        if self.rect.right < 0:
            self.kill()
