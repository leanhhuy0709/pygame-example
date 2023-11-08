import sys

import pygame
from pygame.locals import *
import asyncio

# Init constant
pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))


async def main():
    running = True

    # Game loop.
    while running:
        screen.fill((0, 0, 0))
        # Events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        if running == False:
            break
        # Update Logic

        # Draw

        pygame.display.flip()
        fpsClock.tick(fps)
        await asyncio.sleep(0)


asyncio.run(main())

pygame.quit()
sys.exit()
