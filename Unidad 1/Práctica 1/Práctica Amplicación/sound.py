import os

import pygame

from constantes import RECURSOS, SOUND_ICON


class Sound:
    def __init__(self):
        """
        Constructor de la clase de los sonidos.
        Almacena los sonidos y 2 variables que se usan para cuando silencias el juego
        """
        self.sound = True
        self.collision_sound = pygame.mixer.Sound(os.path.join(RECURSOS, "Collision.ogg"))
        self.move_down_sound = pygame.mixer.Sound(os.path.join(RECURSOS, "Falling_putter.ogg"))
        self.move_up_sound = pygame.mixer.Sound(os.path.join(RECURSOS, "Rising_putter.ogg"))
        self.bullet_shot_sound = pygame.mixer.Sound(os.path.join(RECURSOS, "bullet_shot.mp3"))
        self.no_ammo_sound = pygame.mixer.Sound(os.path.join(RECURSOS, "no_ammo.ogg"))
        self.collect_item = pygame.mixer.Sound(os.path.join(RECURSOS, "collect_item.mp3"))
        self.hit = pygame.mixer.Sound(os.path.join(RECURSOS, "hit.mp3"))
        self.img = SOUND_ICON
