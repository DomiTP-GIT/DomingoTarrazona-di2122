import os
import random

import pygame
from pygame.locals import (
    K_ESCAPE,
    K_q,
    K_m,
    K_SPACE,
    KEYDOWN,
    QUIT
)

from cloud import Cloud
from constantes import RECURSOS, SCREEN_WIDTH, SCREEN_HEIGHT, MUTE_ICON, SOUND_ICON, DIA, FONDO, SCORE_FONT, SCREEN, \
    CLOCK, ROJO_CLARO
from database import Database
from enemy import Enemy
from extend_time import Extend
from heal import Heal
from level import Levels
from pantalla_final import final
from pantalla_inicio import inicio
from player import Player
from score import Score
from shield import Shield
from shots import Shots
from sound import Sound
from speed import Speed
from utils import left_text, text


def juego(db):
    """
    Función del juego. Dentro contiene el bucle del juego.

    :param db: base de datos
    """

    # Inicialización del mixer y de pygame
    pygame.mixer.init()
    pygame.init()

    # Reproducir la canción de fondo en bucle y le bajo el volumen a la mitad
    pygame.mixer.music.load(os.path.join(RECURSOS, "Apoxode_-_Electric_1.ogg"))
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.5)

    # Inicio los objetos que necesito y los asigno a constantes
    PLAYER = Player()
    SCORE = Score()
    SOUND = Sound()
    LEVEL = Levels()

    # Creación de eventos
    ADDENEMY = pygame.USEREVENT + 1

    ADDCLOUD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCLOUD, 1000)

    ADDBULLET = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDBULLET, 5000)

    ADDSHIELD = pygame.USEREVENT + 4
    pygame.time.set_timer(ADDSHIELD, 10000)

    ADDSPEED = pygame.USEREVENT + 5
    pygame.time.set_timer(ADDSPEED, 12000)

    EXTENDTIME = pygame.USEREVENT + 6
    pygame.time.set_timer(EXTENDTIME, 25000)

    ADDHEAL = pygame.USEREVENT + 7
    pygame.time.set_timer(ADDHEAL, 40000)

    # Creación de grupos
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    shields = pygame.sprite.Group()
    speed_upgrades = pygame.sprite.Group()
    extend_time = pygame.sprite.Group()
    heals = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(PLAYER)

    # Variables
    running = True
    x = 0
    last_vc = 0
    power_up_time = 5000

    # Bucle del juego
    while running:
        # Velocidades
        ve = random.randint(2 * LEVEL.level, 10 + 3 * LEVEL.level)
        vc = int(50 + (450 / LEVEL.level))
        if last_vc != vc:
            last_vc = vc
            pygame.time.set_timer(ADDENEMY, vc)

        # Eventos del juego
        for event in pygame.event.get():
            if event.type == KEYDOWN:  # Teclas
                if event.key == K_ESCAPE or event.key == K_q:  # ESC o Q
                    running = False
                    pygame.quit()
                    quit()
                elif event.key == K_m:  # La tecla m activa o desactiva el sonido
                    if SOUND.sound:
                        pygame.mixer.music.set_volume(0)
                        SOUND.img = MUTE_ICON
                        SOUND.sound = False
                    else:
                        pygame.mixer.music.set_volume(1)
                        SOUND.img = SOUND_ICON
                        SOUND.sound = True
                elif event.key == K_SPACE:  # Dispara con la tecla espacio
                    if PLAYER.bullets > 0:
                        new_bullet = Shots(PLAYER.rect.centerx, PLAYER.rect.bottom)
                        bullets.add(new_bullet)
                        all_sprites.add(new_bullet)
                        SOUND.bullet_shot_sound.play()
                        PLAYER.bullets -= 1
                    else:
                        SOUND.no_ammo_sound.play()
            elif event.type == QUIT:  # btn cerrar
                running = False
                pygame.quit()
                quit()
            elif event.type == ADDENEMY:  # Añadir enemigos
                new_enemy = Enemy(ve)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDCLOUD:  # Añadir nubes
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)
            elif event.type == ADDSHIELD:  # Añadir escudos
                new_shield = Shield()
                shields.add(new_shield)
                all_sprites.add(new_shield)
            elif event.type == ADDSPEED:  # Añadir mejoras velocidad
                new_speed_upgrade = Speed()
                speed_upgrades.add(new_speed_upgrade)
                all_sprites.add(new_speed_upgrade)
            elif event.type == EXTENDTIME:  # Añadir mejoras de tiempo
                new_extend_time_upgrade = Extend()
                extend_time.add(new_extend_time_upgrade)
                all_sprites.add(new_extend_time_upgrade)
            elif event.type == ADDHEAL:  # Añadir vidas
                new_heal = Heal()
                heals.add(new_heal)
                all_sprites.add(new_heal)
            elif event.type == ADDBULLET:  # Añadir balas
                if PLAYER.bullets < PLAYER.max_bullets:
                    PLAYER.bullets += 1

        pressed_keys = pygame.key.get_pressed()

        # Actualizar los movimientos
        PLAYER.update(pressed_keys, SOUND)

        enemies.update(SCORE, LEVEL)

        bullets.update()

        clouds.update()

        shields.update()

        speed_upgrades.update()

        extend_time.update()

        heals.update()

        # Color del fondo de pantalla y sistema de fondo dinámico
        SCREEN.fill(DIA)

        xr = x % FONDO.get_rect().width
        SCREEN.blit(FONDO, (xr - FONDO.get_rect().width + 500, 0))
        if xr < SCREEN_WIDTH:
            SCREEN.blit(FONDO, (xr, 0))

        x -= 1

        # Dibujar en pantalla todas las entidades
        for entity in all_sprites:
            SCREEN.blit(entity.surf, entity.rect)

        # Dibujar textos e imágenes en pantalla
        score_text = SCORE_FONT.render("Level: " + str(LEVEL.level) + "   Score: " + str(SCORE.score), True, ROJO_CLARO)
        SCREEN.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 20, 10))

        SCREEN.blit(SOUND.img, (SCREEN_WIDTH - SOUND.img.get_width() - 10, SCREEN_HEIGHT - SOUND.img.get_height() - 10))

        bullet_txt, bullet_rect = left_text(
            "Bullets: {}".format(PLAYER.bullets),
            10, 10,
            0, 0,
            "Military Kid.ttf", 20,
            ROJO_CLARO
        )
        SCREEN.blit(bullet_txt, bullet_rect)

        # Colisiones
        if pygame.sprite.groupcollide(bullets, enemies, True, True):
            SCORE.update(LEVEL)

        if pygame.sprite.spritecollide(PLAYER, shields, True):
            PLAYER.protect(True)
            SOUND.collect_item.play()

        if pygame.sprite.spritecollide(PLAYER, speed_upgrades, True):
            PLAYER.speed_time = pygame.time.get_ticks()
            PLAYER.speed = PLAYER.speed * random.uniform(1.5, 2.5)
            PLAYER.modified_speed = True
            SOUND.collect_item.play()

        if pygame.sprite.spritecollide(PLAYER, extend_time, True):
            power_up_time += 2000
            SOUND.collect_item.play()

        if pygame.sprite.spritecollide(PLAYER, heals, True):
            PLAYER.lives += 1
            SOUND.collect_item.play()

        # Velocidad
        if PLAYER.modified_speed:

            speed_txt, speed_rect = left_text(
                "Speed: {}".format(round(PLAYER.speed, 2)),
                10, 30,
                0, 0,
                "Military Kid.ttf", 20,
                ROJO_CLARO
            )

            SCREEN.blit(speed_txt, speed_rect)

            now = pygame.time.get_ticks()
            if now - PLAYER.speed_time > power_up_time:
                PLAYER.speed = 5
                PLAYER.modified_speed = False

        health_text, health_rect = text(
            "Health: " + "^ " * PLAYER.lives,
            SCREEN_WIDTH / 2, 20,
            0, 0,
            "hearth.ttf", 30,
            ROJO_CLARO
        )

        SCREEN.blit(health_text, health_rect)

        if pygame.sprite.spritecollide(PLAYER, enemies, True):
            if PLAYER.protected:
                PLAYER.protect(False)
                SOUND.hit.play()
            elif PLAYER.lives > 1:
                PLAYER.lives -= 1
                SOUND.hit.play()
            else:
                SOUND.collision_sound.play()
                PLAYER.kill()
                running = False
                final(db, SCORE.score, LEVEL.level, check_high_score(SCORE, db))

        # Actualizar la pantalla
        pygame.display.flip()

        # FPS
        CLOCK.tick(30)


def check_high_score(score, db):
    """
    Comprueba si la puntuación de la partida es mayor que la almacenada en la base de datos.
    En caso de que sea mayor, actualizará los datos de la base de datos.

    :param score: objeto del score
    :param db: objeto de la base de datos
    :return: true si se ha actualizado o false si no se ha actualizado
    """
    saved_high_score = db.get_score()
    if score.score > saved_high_score:
        db.update_score(score.score)
        return True
    return False


if __name__ == '__main__':
    DB = Database()
    inicio(juego, DB)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()
