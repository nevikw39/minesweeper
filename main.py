import os
import random
import sys
import time

import pygame as pg
from pygame import *
from pygame.locals import MOUSEBUTTONDOWN, QUIT, USEREVENT, Color

from grid import *

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 475
FPS = 60

pg.init()

Cnt = 10
Lst = []
Tab = [[] for _ in range(9)]
Sprites = pg.sprite.Group()

Clock = pg.time.Clock()
Screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Background  = pg.Surface(Screen.get_size())
Background.convert()
Background.fill((0, 0, 0))
pg.display.set_caption("Simple Minesweeper by nevikw39")


def dfs(i, j):
    pass


def main():
    global Cnt, Lst
    Lst = random.sample(range(81), 10)
    for i, e in enumerate(Tab):
        for j in range(9):
            e.append(grid(i, j, i * 9 + j in Lst))
            Sprites.add(e[j])

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        btns = pg.mouse.get_pressed()
        i, j = pg.mouse.get_pos()[0] // 50, pg.mouse.get_pos()[1] // 50
        if btns[0]:
            dfs(i, j)
        elif btns[2]:
            if Tab[i][j].s == 0:
                Tab[i][j].s = 1
                Tab[i][j].image = img_flag
                Cnt -= 1
            elif Tab[i][j].s == 1:
                Tab[i][j].s = 0
                Tab[i][j].image = imgs[0]
                Cnt += 1
        Sprites.draw(Screen)
        pg.display.update()
        Clock.tick(FPS)
    pg.quit()


if __name__ == '__main__':
    main()
