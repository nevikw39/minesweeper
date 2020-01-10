import os
import random
import sys
import time

import pygame as pg

imgs = [pg.image.load(os.path.join("assets", "%d.png" % i)) for i in range(6)]
img_flag = pg.image.load(os.path.join("assets", "flag.png"))
img_default = pg.image.load(os.path.join("assets", "default.png"))
img_click = pg.image.load(os.path.join("assets", "click.png"))


class Grid(pg.sprite.Sprite):

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

    def right_click(self, n):
        if self.n < n:
            pass
            # pg.draw.rect(self.image, (25, 137, 100, 10), (0, 0, 50, 50), 0)
        if self.s == 0:
            self.s = 1
            self.image = img_flag
            return -1
        elif self.s == 1:
            self.s = 0
            self.image = img_default
            return 1
        return 0

    def left_click(self):
        self.s = 2
        self.image = imgs[self.n]

    def click(self):
        t = self.image
        self.image = img_click
        time.sleep(0.1)
        self.image = t
