import copy
import os
import random
import sys
import time

import pygame as pg


pg.mixer.init()
snd_click = pg.mixer.Sound(os.path.join("assets", "click.wav"))
snd_flag = pg.mixer.Sound(os.path.join("assets", "flag.wav"))
snd_unflag = pg.mixer.Sound(os.path.join("assets", "unflag.wav"))
snd_wrong = pg.mixer.Sound(os.path.join("assets", "wrong.wav"))

imgs = [pg.image.load(os.path.join("assets", "%d.png" % i)) for i in range(6)]
img_flag = pg.image.load(os.path.join("assets", "flag.png"))
img_default = pg.image.load(os.path.join("assets", "default.png"))
img_click = pg.image.load(os.path.join("assets", "click.png"))

imgs_cft = list()
for i in imgs:
    t = copy.copy(i)
    pg.draw.rect(t, (25, 137, 100, 5), (0, 0, 50, 50), 0)
    imgs_cft.append(t)


class Grid(pg.sprite.Sprite):

    @staticmethod
    def init():
        for i in imgs:
            i.convert()
        for i in imgs_cft:
            i.convert()
        img_click.convert()
        img_default.convert()
        img_flag.convert()

    def __init__(self, i: int, j: int, n: int):
        super().__init__()
        self.i = i
        self.j = j
        self.n = n
        self.s = 0
        self.image = img_default
        self.rect = self.image.get_rect()
        self.rect.center = (i * 50 + 25, j * 50 + 25)

    def right_click(self):
        if self.s == 0:
            snd_flag.play()
            self.s = 1
            self.image = img_flag
            return -1
        elif self.s == 1:
            snd_unflag.play()
            self.s = 0
            self.image = img_default
            return 1
        return 0

    def left_click(self):
        snd_click.play()
        self.s = 2
        self.image = imgs[self.n]

    def click(self):
        t = self.image
        self.image = img_click
        pg.display.update()
        time.sleep(0.1)
        self.image = t

    # def check_conflict(self, n: int):
    #     if self.n < n:
    #         snd_wrong.play()
    #         self.image = imgs_cft[self.n]
    #     else:
    #         if self.s == 2:
    #             self.image = imgs[self.n]
    #         elif self.s == 1:
    #             self.image = img_flag
    #         elif self.s == 0:
    #             self.image = img_default
