from random import randint
import pygame


class Pipe():
    def __init__(self):
        self.top = randint(-300, -50)
        self.bottom = self.top + 525

        self.x = 1000

        self.bottom_hitbox = pygame.Rect(self.x, self.bottom, 40, 400)
        self.top_hitbox = pygame.Rect(self.x, self.top, 40, 400)

    def reset(self):
        self.x = 560
        self.top = randint(-400, -100)
        self.bottom = self.top + 525

    def update(self, hit: bool):
        self.bottom_hitbox = pygame.Rect(self.x, self.bottom, 40, 400)
        self.top_hitbox = pygame.Rect(self.x, self.top, 40, 400)

        if not hit:
            self.x -= 5
        if(self.x < -40):
            self.reset()
