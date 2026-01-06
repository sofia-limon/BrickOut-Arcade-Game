# Wall

import pygame
import settings
from settings import WALL_TICKNS, WALL_HLN, WALL_VLN, WHITE, BLACK

class Wall:
    def __init__(self, direction=False, x=0, y=0, kill=False):
        self.direction = direction
        self.kill = kill
        if kill:
            self.color = BLACK
        else:
            self.color = WHITE
        if direction:
            self.rect = pygame.Rect(
                x,
                y, 
                WALL_TICKNS,
                WALL_VLN
            )
        else:
            self.rect = pygame.Rect(
                x,
                y, 
                WALL_HLN,
                WALL_TICKNS
            )
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

