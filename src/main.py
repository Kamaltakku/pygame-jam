import pygame, sys
from pygame.locals import *

from blocks import GameBlock, LineBlock, Square, SquareBlock, TBlock, ZBlock

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill("white")

pygame.display.set_caption("Tetris")


line = LineBlock()
zblock = ZBlock()
tblock = TBlock()
square = SquareBlock()

if __name__ == "__main__":

    while True:
        DISPLAYSURF.fill("white")

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        square.draw(DISPLAYSURF)
        

        pygame.display.update()
        FramePerSec.tick(FPS)
