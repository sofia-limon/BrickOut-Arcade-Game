# Paddle

import pygame
from settings import PAD_HEIGHT, PAD_WIDTH, PAD_SPEED, WHITE, WIDTH, W_LX, W_RX, WALL_TICKNS

class Paddle: 
    def __init__(self, x, y, color = WHITE):
        self.rect = pygame.Rect(
            x, 
            y, 
            PAD_WIDTH,
            PAD_HEIGHT
        )
        self.speed = PAD_SPEED
        self.color = color
        
    def move(self, direction):
        dif = self.rect.x
        self.rect.x += direction * self.speed
        self.rect.x = max(W_LX+WALL_TICKNS, min(self.rect.x, W_RX - self.rect.width))
        dif = abs(dif-self.rect.x)
        if dif == 0 and direction != 0:
            dif =- 100
        return dif

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
