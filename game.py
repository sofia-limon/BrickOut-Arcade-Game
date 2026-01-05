# Game

import pygame
from settings import BLACK, WHITE, WIDTH, HEIGHT, PAD_WIDTH, PAD_Y


from objects.paddle import Paddle

class Game:
    def __init__(self, screen):
        self.screen = screen
        start_x = WIDTH/2 - PAD_WIDTH/2
        self.paddle = Paddle(x=start_x, y=PAD_Y)
        self.dir = 0

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