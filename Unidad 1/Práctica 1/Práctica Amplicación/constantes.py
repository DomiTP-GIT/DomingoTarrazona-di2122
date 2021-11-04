import os

import pygame

pygame.font.init()

DIRECTORIO = os.path.dirname(__file__)
RECURSOS = os.path.join(DIRECTORIO, 'resources')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCORE_FONT = pygame.font.Font(os.path.join(RECURSOS, "Military Kid.ttf"), 20)
ROJO = (153, 0, 0)
ROJO_CLARO = (255, 0, 0)
VERDE = (0, 153, 0)
VERDE_CLARO = (0, 255, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROSA = (255, 51, 243)
MORADO = (184, 51, 255)
AZUL = (0, 31, 255)

DIA = (135, 206, 250)
NOCHE = (44, 45, 46)

MUTE_ICON = pygame.image.load(os.path.join(RECURSOS, "mute.png"))
SOUND_ICON = pygame.image.load(os.path.join(RECURSOS, "sound.png"))
FONDO = pygame.image.load(os.path.join(RECURSOS, "fondo.png"))

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
