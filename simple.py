import sys

import pygame
from pygame.locals import *
import asyncio
from constant import PygameConfig, Color, DinoSprite

# Init constant
pygame.init()

fps = 60
fpsClock = pygame.time.Clock()
RED = (255, 0, 0)

pygame.display.set_caption('Game')
screen = pygame.display.set_mode((500, 500))

x = 100
y = 100

running = True

# Game loop.
while running:
    screen.fill(Color.WHITE)
    # Events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                x = x - 10
            elif event.key == pygame.K_RIGHT:
                x = x + 10
            elif event.key == pygame.K_UP:
                y = y - 10
            elif event.key == pygame.K_DOWN:
                y = y + 10

    if running == False:
        break

    # Logic

    # Draw
    pygame.draw.rect(screen, RED, (x, y, 50, 50))

    pygame.display.flip()
    fpsClock.tick(fps)
