import os

import pygame
from pygame.locals import (
    K_ESCAPE,
    K_q,
    K_p
)

from cloud import Cloud
from constantes import DIA, SCREEN_WIDTH, SCREEN_HEIGHT, ROJO, VERDE_CLARO, VERDE, ROJO_CLARO, SCREEN, CLOCK, \
    RECURSOS, AZUL
from utils import text_objects, button, right_text


def inicio(juego, db):
    """
    Pantalla de inicio

    :param juego: función del juego
    :param db: base de datos
    """
    ini = True

    # Icon & title
    pygame.display.set_caption("PyShip")
    icon = pygame.image.load(os.path.join(RECURSOS, "icon.png"))
    pygame.display.set_icon(icon)

    clouds = pygame.sprite.Group()
    ADDCLOUD = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDCLOUD, 2000)

    high_score = db.get_score()

    while ini:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:  # ESC o Q
                    pygame.quit()
                    quit()
                elif event.key == K_p:
                    juego(db)
                    break
            elif event.type == ADDCLOUD:
                new_cloud = Cloud()
                clouds.add(new_cloud)

        clouds.update()

        SCREEN.fill(DIA)

        for cloud in clouds:
            SCREEN.blit(cloud.surf, cloud.rect)

        inicio_font = pygame.font.Font(os.path.join(RECURSOS, "AlphaWood.ttf"), 135)
        inicio_text_surf, inicio_text_rect = text_objects("START", inicio_font, ROJO)
        inicio_text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 60)
        SCREEN.blit(inicio_text_surf, inicio_text_rect)

        # high_score_font = pygame.font.Font(os.path.join(RECURSOS, "Military Kid.ttf"), 40)
        # high_score_txt = high_score_font.render("High Score: {}".format(high_score), True, VERDE_CLARO)
        # high_score_rect = (SCREEN_WIDTH - high_score_txt.get_width() - 30, 10)
        # SCREEN.blit(high_score_txt, high_score_rect)

        high_score_txt, high_score_rect = right_text(
            "High Score: {}".format(high_score),
            SCREEN_WIDTH, 5,
            -10, 0,
            "NEON.ttf", 40,
            AZUL
        )
        SCREEN.blit(high_score_txt, high_score_rect)

        button("JUGAR", 150, 450, 100, 50, VERDE, VERDE_CLARO, juego)
        button("SALIR", 550, 450, 100, 50, ROJO, ROJO_CLARO, salir)

        pygame.display.update()
        CLOCK.tick(30)


def salir():
    """
    Cierra pygame y luego el programa
    """
    pygame.quit()
    quit()
