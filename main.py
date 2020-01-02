import os
import random
import sys
import time

import pygame as pg
from pygame import *
from pygame.locals import MOUSEBUTTONDOWN, QUIT, USEREVENT, Color

from grid import *

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450
FPS = 60

pg.init()

Tab = [[] for _ in range(9)]
Sprites = pg.sprite.Group()

Clock = pg.time.Clock()
Screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Background  = pg.Surface(Screen.get_size())
Background.convert()
pg.display.set_caption("Simple Minesweeper by nevikw39")


def dfs(i, j):
    pass


def main():

    lst = random.sample(range(81), 10)
    for i, e in enumerate(Tab):
        for j in range(9):
            e.append(grid(i, j, i * 9 + j in lst))
            Sprites.add(e[j])

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        btns = pg.mouse.get_pressed()
        if btns[0]:
            dfs(pg.mouse.get_pos()[0] // 50, pg.mouse.get_pos()[1] // 50)
        elif btns[2]:
            Tab[pg.mouse.get_pos()[0] // 50][pg.mouse.get_pos()[1] // 50].s = 1
            Tab[pg.mouse.get_pos()[0] // 50][pg.mouse.get_pos()[1] // 50].image = pg.image.load(os.path.join("assets", "flag.png"))
        Sprites.draw(Screen)
        pg.display.update()
        Clock.tick(FPS)
    pg.quit()


if __name__ == '__main__':
    main()
