import os
import random
import sys
import time

import pygame as pg
from pygame import *
from pygame.locals import MOUSEBUTTONDOWN, QUIT, USEREVENT, Color

imgs = [pg.image.load(os.path.join("assets", "%d.png" % i)) for i in range(6)]

class grid(pg.sprite.Sprite):

    def __init__(self, i , j, is_mine):
        super().__init__()
        self.i = i
        self.j = j
        self.n = 0
        self.image = imgs[0]
        self.is_mine = is_mine
        self.rect = self.image.get_rect()
        self.rect.center = (i * 50 + 25, j * 50 + 25)
    
    def draw(self):
        self.image = imgs[n]