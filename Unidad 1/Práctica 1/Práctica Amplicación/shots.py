import os
import random

import pygame
from pygame.locals import RLEACCEL

from constantes import RECURSOS, SCREEN_WIDTH


class Shots(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Constructor de las balas.
        Crea una nueva bala a partir de la posición de la nave cuando dispara.
        :param x: Centro de la nave
        :param y: Parte superior de la nave
        """
        super(Shots, self).__init__()
        self.speed = random.randint(5, 10)
        self.surf = pygame.image.load(os.path.join(RECURSOS, "bullet.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.centerx = x + 10
        self.rect.bottom = y

    def update(self):
        """
        Actualiza la posición de una bala y en caso de no darle a un enemigo y salirse de la pantalla, lo elimina.
        """
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()

    def speed_update(self, new_speed):
        """
        Modifica la velocidad de la bala.
        Se usa cuando obtienes una mejora de velocidad.
        :param new_speed: Nueva velocidad
        """
        self.speed = new_speed
