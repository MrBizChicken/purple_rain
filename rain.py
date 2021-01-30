from constants import *
import pygame
import random

class Rain:
    def __init__(self):
        self.height = 50
        self.width = 5
        self.x = 5
        self.y = 5
        self.speed = 3

        self.color = (128,0,128)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rnd = random.randint(0, 400)

    def update(self):
        self.fall()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def fall(self):

        if self.rect.y >= GAME_HEIGHT:
            self.rect.bottom = 0

            self.rect.x = self.rnd
        else:
            self.rect = self.rect.move(0, self.speed)
