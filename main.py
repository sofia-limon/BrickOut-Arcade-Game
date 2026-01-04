#main

import pygame

from settings import WIDTH, HEIGHT, FPS

pygame .init()

def play():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brick Out")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

def main():
    play()

    print("Brick Out ended successfully")

if __name__ == "__main__":
    main()