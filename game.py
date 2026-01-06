# Game

import pygame
from settings import (
    BLACK, WHITE, WIDTH, HEIGHT, 
    PAD_WIDTH, PAD_Y, PAD_X,
    W_UX, W_UY, W_DX, W_DY, W_LX, W_LY, W_RX, W_RY
    )

from objects.paddle import Paddle
from objects.wall import Wall

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.paddle = Paddle(x=PAD_X, y=PAD_Y)
        self.dir = 0
        self.walls = [
            Wall(direction=False,  x=W_DX, y=W_DY, kill=True),
            Wall(direction=True,   x=W_LX, y=W_LY),
            Wall(direction=True,   x=W_RX, y=W_RY),
            Wall(direction=False,  x=W_UX, y=W_UY),
            ]

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.dir = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.dir = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dir = 1

    def update(self):
        self.paddle.move(self.dir)

    def draw(self):
        self.screen.fill(BLACK)
        self.paddle.draw(self.screen)
        for w in self.walls:
            w.draw(self.screen)