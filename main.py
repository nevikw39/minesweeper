#!/usr/bin/python3
import os
import random
import sys
import time
from datetime import datetime
from tkinter import *

import pygame as pg

from grid import Grid

Tk().wm_withdraw()

pg.init()
pg.display.set_caption("Simple Minesweeper by nevikw39")


Clock = pg.time.Clock()
Font = pg.font.Font(None, 24)
FPS = 60
Sprites = pg.sprite.Group()
Screen = pg.display.set_mode((450, 500))
Background = pg.Surface(Screen.get_size())
Background.convert()
Background.fill((0, 0, 0))


dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def init():
    global Cnt, Map, Mines, Lst, Time
    Cnt = 10
    Map = [[] for _ in range(9)]
    Mines = set(random.sample(range(81), 10))
    Lst = set(range(81))
    Time = time.time()
    for i, e in enumerate(Map):
        for j in range(9):
            n = 0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if not 0 <= x < 9 or not 0 <= y < 9:
                    continue
                elif x * 9 + y in Mines:
                    n += 1
            e.append(Grid(i, j, n))
            Sprites.add(e[j])
    print("Mines =", Mines)


def dfs(i, j):
    if Map[i][j].s == 1:
        return True
    elif i * 9 + j in Mines:
        return False
    elif i * 9 + j in Lst:
        Lst.remove(i * 9 + j)
    Map[i][j].left_click()
    if not Map[i][j].n:
        for k in range(8):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < 9 and 0 <= y < 9 and Map[x][y].s == 0:
                dfs(x, y)
    elif Map[i][j].s == 2:
        n = 0
        for k in range(8):
            x = i + dx[k]
            y = j + dy[k]
            n += 0 <= x < 9 and 0 <= y < 9 and Map[x][y].s == 1
        if Map[i][j].n == n:
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < 9 and 0 <= y < 9 and Map[x][y].s == 0:
                    dfs(x, y)
    return True


def gg():
    global Time
    if messagebox.askyesno('GG', '你超爛ＱＱ\n\n再來一局ㄇ？？', icon='error'):
        init()
        return True
    else:
        return False


def win():
    global Time
    if messagebox.askyesno('Win', '你贏惹 o\'_\'o\n費時：' + datetime.fromtimestamp(time.time() - Time).strftime("%M:%S") + '\n再來一局ㄇ？？', icon='info'):
        init()
        return True
    else:
        return False


def main():
    global Cnt, Lst
    init()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            elif event.type == pg.MOUSEBUTTONDOWN:
                i, j = event.pos[0] // 50, event.pos[1] // 50
                if not 0 <= i < 9 or not 0 <= j < 9:
                    continue
                Map[i][j].click()

            elif event.type == pg.MOUSEBUTTONUP:
                i, j = event.pos[0] // 50, event.pos[1] // 50
                if not 0 <= i < 9 or not 0 <= j < 9:
                    continue
                if event.button == 1:
                    if not dfs(i, j):
                        if gg():
                            continue
                        else:
                            return
                elif event.button == 3:
                    Cnt += Map[i][j].right_click()
                    for k in range(8):
                        x = i + dx[k]
                        y = j + dy[k]
                        n = 0
                        if 0 <= x < 9 and 0 <= y < 9:
                            if Map[x][y].s == 2:
                                m = 0
                                for l in range(8):
                                    p = x + dx[l]
                                    q = y + dy[l]
                                    m += 0 <= p < 9 and 0 <= q < 9 and Map[p][q].s == 1
                                Map[x][y].check_conflict(m)
                            elif Map[x][y].s == 1:
                                n += 1
                    Map[i][j].check_conflict(n)

        text = Font.render("Cnt: %2d   Time: " % Cnt + datetime.fromtimestamp(time.time() - Time).strftime("%M:%S     "), True,
                           (192, 192, 192), (0, 0, 0))
        Screen.blit(text, (15, 465))
        Sprites.draw(Screen)
        pg.display.update()

        if Lst == Mines:
            if win():
                continue
            else:
                return

        Clock.tick(FPS)


if __name__ == '__main__':
    main()
    pg.quit()
