import sys

import pygame
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 608
SCREEN_HEIGHT = 576

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill("white")
pygame.display.set_caption("Tetris")

# 1 Block = 8 * 8 In-Game Pixel
# 1 In-Game Pixel = 32 * 32 Real Pixel -> 4 Real pixel per block
# According to example image, Game will have (10 + 2 + 7) * 18 Blocks (608 * 576 Real Pixel)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x_axis):
        super().__init__()
        self.image = pygame.image.load("img/wall.png")
        self.surf = pygame.Surface((32, 576))
        self.rect = self.surf.get_rect(center = (x_axis, 288))


# Initial setup
DISPLAYSURF.fill("white")
left_wall = Wall(16)
right_wall = Wall(400)
DISPLAYSURF.blit(left_wall.image, left_wall.rect)
DISPLAYSURF.blit(right_wall.image, right_wall.rect)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
