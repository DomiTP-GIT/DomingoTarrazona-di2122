import os

import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    RLEACCEL
)

from constantes import RECURSOS, SCREEN_WIDTH, SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self):
        """
        Constructor de la clase Player.
        El constructor, tiene la imagen principal del jet, el máximo de balas que puede tener un
        jugador, las balas iniciales, si el jugador está protegido, la velocidad, el tiempo del juego,
        una variable para saber si la velocidad está cambiada y el número de vidas.
        """
        super(Player, self).__init__()
        self.surf = pygame.image.load(os.path.join(RECURSOS, "jet.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.max_bullets = 10
        self.bullets = 5
        self.protected = False
        self.speed = 5
        self.speed_time = pygame.time.get_ticks()
        self.modified_speed = False
        self.lives = 3

    def update(self, pressed_keys, sound):
        """
        Actualiza los movimientos de la nave y reproduce los sonidos al subir y bajar.
        También controla que la nave no se salga de la pantalla

        :param pressed_keys: Conjunto de teclas presionadas en cada ciclo
        :param sound: objeto de sonido
        """
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
            if sound.sound:
                sound.move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            if sound.sound:
                sound.move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def protect(self, activate):
        """
        Cambia la imagen de la nave entre la nave normal y la nave protegida.
        """
        if activate:
            self.surf = pygame.image.load(os.path.join(RECURSOS, "jet_shield.png")).convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.protected = True
        else:
            self.surf = pygame.image.load(os.path.join(RECURSOS, "jet.png")).convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.protected = False
