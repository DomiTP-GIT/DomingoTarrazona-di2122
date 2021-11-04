import os

import pygame

from constantes import NEGRO, SCREEN, RECURSOS


def text_objects(text, font, color=NEGRO):
    """
    Retorna un texto con la fuente y el color especificados.

    :param text: Texto que quieres escribir
    :param font: Nombre de la fuente
    :param color: Color de la fuente
    :return: superficie de pygame y el rect de la superficie
    """
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def button(msg, x, y, w, h, color, hold_color, action=None):
    """
    Crea un botón con los parámetros que le pasemos.

    :param msg: Mensaje que tendrá el botón
    :param x: Coordenada X
    :param y: Coordenada Y
    :param w: Ancho
    :param h: Alto
    :param color: Color del botón
    :param hold_color: Color al pasar el ratón por encima del botón
    :param action: Acción que realiza si se presiona el botón
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(SCREEN, hold_color, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(SCREEN, color, (x, y, w, h))

    btn_text = pygame.font.Font(os.path.join(RECURSOS, "Vintages.ttf"), 30)
    text_surf, text_rect = text_objects(msg, btn_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    SCREEN.blit(text_surf, text_rect)


def text(msg, w, h, x=0, y=0, font_name="roboto", size=20, color=NEGRO):
    """
    Crea un texto y lo posiciona en la pantalla.

    :param msg: Mensaje que contendrá el texto
    :param w: Ancho
    :param h: Alto
    :param x: X
    :param y: Y
    :param font_name: Nombre de la fuente
    :param size: Tamaño de la fuente
    :param color: Color del texto
    :return: pygame surface, pygame rect
    """
    font = pygame.font.Font(os.path.join(RECURSOS, font_name), size)
    text_surf, text_rect = text_objects(msg, font, color)
    text_rect.center = (w + x, h + y)
    return text_surf, text_rect


def right_text(msg, w, h, x=0, y=0, font_name="roboto", size=20, color=NEGRO):
    """
    Crea un texto y lo posiciona en la pantalla.
    Preparado específicamente para que esté situado en la parte superior derecha de la pantalla
    ya que se ajusta al tamaño del texto.

    :param msg: Mensaje que contendrá el texto
    :param w: Ancho
    :param h: Alto
    :param x: X
    :param y: Y
    :param font_name: Nombre de la fuente
    :param size: Tamaño de la fuente
    :param color: Color del texto
    :return: pygame surface, pygame rect
    """
    font = pygame.font.Font(os.path.join(RECURSOS, font_name), size)
    text_surf, text_rect = text_objects(msg, font, color)
    text_rect = (w - text_surf.get_width() + x, h + y)
    return text_surf, text_rect


def left_text(msg, w, h, x=0, y=0, font_name="roboto", size=20, color=NEGRO):
    """
    Crea un texto y lo posiciona en la pantalla.
    Preparado específicamente para que esté situado en la parte superior izquierda de la pantalla
    ya que se ajusta al tamaño del texto.

    :param msg: Mensaje que contendrá el texto
    :param w: Ancho
    :param h: Alto
    :param x: X
    :param y: Y
    :param font_name: Nombre de la fuente
    :param size: Tamaño de la fuente
    :param color: Color del texto
    :return: pygame surface, pygame rect
    """
    font = pygame.font.Font(os.path.join(RECURSOS, font_name), size)
    text_surf, text_rect = text_objects(msg, font, color)
    text_rect = (w + x, h + y)
    return text_surf, text_rect


def bottom_left_text(msg, w, h, x=0, y=0, font_name="roboto", size=20, color=NEGRO):
    """
    Crea un texto y lo posiciona en la pantalla.
    Preparado específicamente para que esté situado en la parte inferior izquierda de la pantalla
    ya que se ajusta al tamaño del texto.

    :param msg: Mensaje que contendrá el texto
    :param w: Ancho
    :param h: Alto
    :param x: X
    :param y: Y
    :param font_name: Nombre de la fuente
    :param size: Tamaño de la fuente
    :param color: Color del texto
    :return: pygame surface, pygame rect
    """
    font = pygame.font.Font(os.path.join(RECURSOS, font_name), size)
    text_surf, text_rect = text_objects(msg, font, color)
    text_rect = (w + x, h - text_surf.get_height() + y)
    return text_surf, text_rect
