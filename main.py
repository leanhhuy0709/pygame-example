import sys

import pygame
from pygame.locals import *
import asyncio
from constant import PygameConfig, Color, DinoSprite

# Init constant
pygame.init()

fps = PygameConfig.FPS
fpsClock = pygame.time.Clock()

pygame.display.set_caption(PygameConfig.TITLE)
screen = pygame.display.set_mode((PygameConfig.WIDTH, PygameConfig.HEIGHT))


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dinoSprite = [DinoSprite.DINO_WALK_1, DinoSprite.DINO_WALK_2, DinoSprite.DINO_WALK_3, DinoSprite.DINO_WALK_4, DinoSprite.DINO_WALK_5,
                           DinoSprite.DINO_WALK_6, DinoSprite.DINO_WALK_7, DinoSprite.DINO_WALK_8, DinoSprite.DINO_WALK_9, DinoSprite.DINO_WALK_10]
        self.delay = 0
        self.image = None
        self.spriteIndex = 0

    def moveLeft(self):
        self.updateSpriteIndex()
        self.x -= 10
        self.x = (self.x + PygameConfig.WIDTH) % PygameConfig.WIDTH

    def moveRight(self):
        self.updateSpriteIndex()
        self.x += 10
        self.x = (self.x + PygameConfig.WIDTH) % PygameConfig.WIDTH

    def moveUp(self):
        self.updateSpriteIndex()
        self.y -= 10
        self.y = (self.y + PygameConfig.HEIGHT) % PygameConfig.HEIGHT

    def moveDown(self):
        self.updateSpriteIndex()
        self.y += 10
        self.y = (self.y + PygameConfig.HEIGHT) % PygameConfig.HEIGHT

    def drawRect(self):
        pygame.draw.rect(screen, Color.BLUE,
                         (self.x, self.y, self.width, self.height))

    def drawImage(self, screen):
        self.image = pygame.image.load(self.dinoSprite[self.spriteIndex])
        self.image = pygame.transform.scale(self.image, (640, 480))
        screen.blit(self.image, (self.x, self.y))
        pass

    def update(self):
        # self.moveRight()
        pass

    def updateSpriteIndex(self):
        self.spriteIndex += 1
        if self.spriteIndex >= len(self.dinoSprite):
            self.spriteIndex = 0


async def main():
    # Create player
    player = Player(100, 0, 50, 50)

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
                    player.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    player.moveRight()
                elif event.key == pygame.K_UP:
                    player.moveUp()
                elif event.key == pygame.K_DOWN:
                    player.moveDown()

        if running == False:
            break

        # Logic
        player.update()
        # Draw
        player.drawRect()
        player.drawImage(screen)

        pygame.display.flip()
        fpsClock.tick(fps)
        await asyncio.sleep(0)


asyncio.run(main())

pygame.quit()
sys.exit()
