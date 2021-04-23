import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill("white")
pygame.display.set_caption("Tetris")


class Square(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()


class GameBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.list_of_blocks = [Square(1), Square(2), Square(3), Square(4)]


class LineBlock(GameBlock):
    def __init__(self):
        super().__init__()
        self.arranged_squares = ArrangedSquares(self.list_of_blocks, "LineBlock")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill("white")

    pygame.display.update()
    FramePerSec.tick(FPS)
