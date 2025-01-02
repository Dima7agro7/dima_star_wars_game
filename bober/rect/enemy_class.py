import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        size_image = 0.05
        self.image = pygame.image.load(f'image/enemy.png')
        self.image = pygame.transform.rotozoom(self.image, 1, size_image)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(100, 600)
        self.rect.centery = random.randint(0, 200)
        self.speed = 0.5

#         задём скорость врагам ( 2 варинаты только в низ или вниз + в бок)
#
    def update(self):
        self.move()
        if self.rect.bottom > 800:
            self.kill()
        if self.rect.left < 0:
            self.kill()
        if self.rect.right > 800:
            self.kill()

    def move(self):
        self.rect.y += self.speed
        self.rect.x += self.speed * random.randint(-20, 20)
