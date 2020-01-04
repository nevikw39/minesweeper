import os
import random
import sys
import time

import pygame as pg

imgs = [pg.image.load(os.path.join("assets", "%d.png" % i)) for i in range(6)]
img_flag = pg.image.load(os.path.join("assets", "flag.png"))
img_default = pg.image.load(os.path.join("assets", "default.png"))
img_click = pg.image.load(os.path.join("assets", "click.png"))


class grid(pg.sprite.Sprite):

    def __init__(self, i, j, n, is_mine):
        super().__init__()
        self.i = i
        self.j = j
        self.n = n
        self.s = 0
        self.image = img_default
        self.is_mine = is_mine
        self.rect = self.image.get_rect()
        self.rect.center = (i * 50 + 25, j * 50 + 25)
    
    def right_click(self):
        if self.s == 0:
            self.s = 1
            self.image = img_flag
        elif self.s == 1:
            self.s = 0
            self.image = img_default
    
    def left_click(self):
        self.s = 2
        self.image = imgs[self.n]
