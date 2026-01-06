# Ball

import pygame

from settings import BALL_X, BALL_Y, BALL_SPEED, BALL_RADIUS, WHITE

class Ball:
    def __init__(self, x = BALL_X, y = BALL_Y, direction = pygame.Vector2(0, 1), speed = BALL_SPEED, radius = BALL_RADIUS, color = WHITE):
        self.pos = pygame.Vector2(x, y)
        self.direction = direction
        self.radius = radius
        self.color = color
        self.speed = speed

    def move(self):
        self.pos += self.direction * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, radius=self.radius)

"""struct Ball{
    pair<float, float> pos, direction;
    float speed, radius;

    Ball(int _x, int _y, pair<float, float> _direction, float _speed, float _radius, vector<float> _color):{
        pos = {_x, _y};
        direction = _direction;
        speed = _speed;
        radius = _radius;
    }
};"""