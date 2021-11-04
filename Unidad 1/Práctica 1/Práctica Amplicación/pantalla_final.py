import os

import pygame
from pygame.locals import (
    K_ESCAPE,
    K_q
)

from constantes import SCREEN, NOCHE, ROJO, SCREEN_WIDTH, SCREEN_HEIGHT, ROJO_CLARO, CLOCK, ROSA, VERDE_CLARO, BLANCO, \
    RECURSOS, MORADO
from utils import text_objects, button, text, bottom_left_text


def final(db, score, level, new_high_score):
    """
    Pantalla final
    :param db: base de datos
    :param score: objeto score
    :param level: objeto level
    :param new_high_score: nuevo record
    """
    ini = True
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

        SCREEN.fill(NOCHE)

        if new_high_score:
            text_surface, text_rect = text(
                "NEW HIGH SCORE",
                (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2),
                0, -175,
                "REWARD.ttf", 50,
                MORADO
            )
            SCREEN.blit(text_surface, text_rect)

            felicitaciones_surface, felicitaciones_rect = bottom_left_text(
                "Felicidades, tienes el nuevo record",
                10, SCREEN_HEIGHT,
                0, 0,
                "SugarpunchDEMO.otf", 40,
                VERDE_CLARO
            )
            SCREEN.blit(felicitaciones_surface, felicitaciones_rect)

        high_score_font = pygame.font.Font(os.path.join(RECURSOS, "Military Kid.ttf"), 40)
        high_score_txt = high_score_font.render("High Score: {}".format(high_score), True, VERDE_CLARO)
        high_score_rect = (SCREEN_WIDTH - high_score_txt.get_width() - 30, 10)
        SCREEN.blit(high_score_txt, high_score_rect)

        score_font = pygame.font.Font(os.path.join(RECURSOS, "Military Kid.ttf"), 40)
        score_txt = score_font.render("Last Score: {}".format(score), True, BLANCO)
        score_rect = (10, 10)
        SCREEN.blit(score_txt, score_rect)

        level_font = pygame.font.Font(os.path.join(RECURSOS, "Military Kid.ttf"), 40)
        level_txt = level_font.render("Level: {}".format(level), True, BLANCO)
        level_rect = (10, score_txt.get_height() + 10)
        SCREEN.blit(level_txt, level_rect)

        final_font = pygame.font.Font(os.path.join(RECURSOS, "AlphaWood.ttf"), 135)
        final_text_surf, final_text_rect = text_objects("Game Over", final_font, ROSA)
        final_text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 20)
        SCREEN.blit(final_text_surf, final_text_rect)

        button("SALIR", 350, 450, 100, 50, ROJO, ROJO_CLARO, salir)

        pygame.display.update()
        CLOCK.tick(15)


def salir():
    """
    Cierra pygame y luego el programa
    """
    pygame.quit()
    quit()
