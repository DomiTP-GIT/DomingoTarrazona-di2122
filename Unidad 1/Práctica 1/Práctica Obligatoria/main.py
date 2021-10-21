import os
import random

import pygame
from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	K_q,
	KEYDOWN,
	QUIT,
	RLEACCEL
)

pygame.font.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

directorio = os.path.dirname(__file__)
recursos = os.path.join(directorio, 'resources')

collision_sound = pygame.mixer.Sound(os.path.join(recursos, "Collision.ogg"))
move_down_sound = pygame.mixer.Sound(os.path.join(recursos, "Falling_putter.ogg"))
move_up_sound = pygame.mixer.Sound(os.path.join(recursos, "Rising_putter.ogg"))


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.surf = pygame.image.load(os.path.join(recursos, "jet.png")).convert()
		self.surf.set_colorkey((255, 255, 255), RLEACCEL)
		self.rect = self.surf.get_rect()

	def update(self, pressed_keys):
		if pressed_keys[K_UP]:
			self.rect.move_ip(0, -5)
			move_up_sound.play()
		if pressed_keys[K_DOWN]:
			self.rect.move_ip(0, 5)
			move_down_sound.play()
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(-5, 0)
		if pressed_keys[K_RIGHT]:
			self.rect.move_ip(5, 0)

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super(Enemy, self).__init__()
		self.surf = pygame.image.load(os.path.join(recursos, "missile.png")).convert()
		self.surf.set_colorkey((255, 255, 255), RLEACCEL)
		self.rect = self.surf.get_rect(
			center=(
				random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
				random.randint(0, SCREEN_HEIGHT),
			)
		)
		self.speed = random.randint(5, 20)

	def update(self):
		self.rect.move_ip(-self.speed, 0)
		if self.rect.right < 0:
			self.kill()


class Cloud(pygame.sprite.Sprite):
	def __init__(self):
		super(Cloud, self).__init__()
		self.surf = pygame.image.load(os.path.join(recursos, "cloud.png")).convert()
		self.surf.set_colorkey((0, 0, 0), RLEACCEL)
		self.rect = self.surf.get_rect(
			center=(
				random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
				random.randint(0, SCREEN_HEIGHT),
			)
		)

	def update(self):
		self.rect.move_ip(-5, 0)
		if self.rect.right < 0:
			self.kill()


# Mixer movido para poder usar las canciones
pygame.init()

pygame.mixer.music.load(os.path.join(recursos, "Apoxode_-_Electric_1.ogg"))
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.2)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

player = Player()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:  # Teclas
			if event.key == K_ESCAPE or event.key == K_q:  # ESC o Q
				running = False
		elif event.type == QUIT:  # btn cerrar
			running = False
		elif event.type == ADDENEMY:
			new_enemy = Enemy()
			enemies.add(new_enemy)
			all_sprites.add(new_enemy)
		elif event.type == ADDCLOUD:
			new_cloud = Cloud()
			clouds.add(new_cloud)
			all_sprites.add(new_cloud)

	pressed_keys = pygame.key.get_pressed()

	player.update(pressed_keys)

	enemies.update()

	clouds.update()

	screen.fill((135, 206, 250))

	for entity in all_sprites:
		screen.blit(entity.surf, entity.rect)

	if pygame.sprite.spritecollideany(player, enemies):
		collision_sound.play()
		player.kill()
		running = False

	pygame.display.flip()

	clock.tick(30)

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
