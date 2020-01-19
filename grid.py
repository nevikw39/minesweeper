import copy
import os
import random
import sys
import time

import pygame as pg


# 聲音檔載入
pg.mixer.init()
snd_click = pg.mixer.Sound(os.path.join("assets", "click.wav"))
snd_flag = pg.mixer.Sound(os.path.join("assets", "flag.wav"))
snd_unflag = pg.mixer.Sound(os.path.join("assets", "unflag.wav"))
snd_wrong = pg.mixer.Sound(os.path.join("assets", "wrong.wav"))

# 圖片檔載入
imgs = [pg.image.load(os.path.join("assets", "%d.png" % i)) for i in range(6)]
img_flag = pg.image.load(os.path.join("assets", "flag.png"))
img_default = pg.image.load(os.path.join("assets", "default.png"))
img_click = pg.image.load(os.path.join("assets", "click.png"))


class Grid(pg.sprite.Sprite):

    """格子類別

    踩地雷中每個格子的基本類別．繼承自 pygame.sprite.Sprite．

    Attributes:
        i: 第幾列
        J: 第幾行
        n: 周遭地雷數
        s: 狀態．0 表預設，1 表被放置旗子，2 表被打開
    """

    @staticmethod
    def init():
        """初始化工作

        將圖片加速預先繪製．因為必須等到主程式載入 Screen 後才可以執行，因此寫成靜態方法．
        """
        for i in imgs:
            i.convert()
        img_click.convert()
        img_default.convert()
        img_flag.convert()

    def __init__(self, i: int, j: int, n: int):
        """建構式．以行數、列數及地雷數初始化 Grid．"""
        super().__init__()
        self.i = i
        self.j = j
        self.n = n
        self.s = 0
        self.image = img_default
        self.rect = self.image.get_rect()
        self.rect.center = (i * 50 + 25, j * 50 + 25)

    def right_click(self):
        """右鍵點擊，切換旗子狀態．"""
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
        """左鍵點擊，展開格子．"""
        snd_click.play()
        self.s = 2
        self.image = imgs[self.n]

    def click(self):
        """一般點擊．"""
        t = self.image
        self.image = img_click
        pg.display.update()
        time.sleep(0.1)
        self.image = t
