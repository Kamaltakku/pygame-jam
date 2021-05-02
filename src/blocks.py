import pygame
from pygame.locals import *
from pathlib import Path

ASSETS = Path("src/assets")

class Square(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ASSETS / "square.png")
        self.surf = pygame.Surface((1, 1))
        self.surf.convert_alpha()
        self.rect = self.surf.get_rect()


class GameBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.blocks = [Square(), Square(), Square(), Square()]
        self.rotation = "vertical"



class LineBlock(GameBlock):
    def __init__(self):

        super().__init__()
        self.blocks[0].rect = self.blocks[0].surf.get_rect(topleft=(0,0))
        self.blocks[1].rect = self.blocks[1].surf.get_rect(topleft=(0, 20))
        self.blocks[2].rect = self.blocks[2].surf.get_rect(topleft=(0, 40))
        self.blocks[3].rect = self.blocks[3].surf.get_rect(topleft=(0, 60)) 

    def draw(self, surface):
        for block in self.blocks:
            surface.blit(block.surf, block.rect)

class TBlock(GameBlock):
    def __init__(self):

        super().__init__()
        self.blocks[0].rect = self.blocks[0].surf.get_rect(topleft=(0,0))
        self.blocks[1].rect = self.blocks[1].surf.get_rect(topleft=(0, 20))
        self.blocks[2].rect = self.blocks[2].surf.get_rect(topleft=(20, 20))
        self.blocks[3].rect = self.blocks[3].surf.get_rect(topleft=(0, 40)) 

    def draw(self, surface):
        for block in self.blocks:
            surface.blit(block.surf, block.rect)

class ZBlock(GameBlock):
    def __init__(self):

        super().__init__()
        self.blocks[0].rect = self.blocks[0].surf.get_rect(topleft=(0,0))
        self.blocks[1].rect = self.blocks[1].surf.get_rect(topleft=(0, 20))
        self.blocks[2].rect = self.blocks[2].surf.get_rect(topleft=(20, 20))
        self.blocks[3].rect = self.blocks[3].surf.get_rect(topleft=(20, 40)) 

    def draw(self, surface):
        for block in self.blocks:
            surface.blit(block.surf, block.rect)

class SquareBlock(GameBlock):
    def __init__(self):

        super().__init__()
        self.blocks[0].rect = self.blocks[0].surf.get_rect(topleft=(0,0))
        self.blocks[1].rect = self.blocks[1].surf.get_rect(topleft=(0, 20))
        self.blocks[2].rect = self.blocks[2].surf.get_rect(topleft=(20, 0))
        self.blocks[3].rect = self.blocks[3].surf.get_rect(topleft=(20, 20)) 

    def draw(self, surface):
        for block in self.blocks:
            surface.blit(block.surf, block.rect)
    

