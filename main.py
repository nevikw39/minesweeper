#!/usr/local/opt/python/bin/python3.7
import os
import random
import sys
import time
from datetime import datetime
from tkinter import *
from tkinter import messagebox

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
Grid.init()
Background = pg.Surface(Screen.get_size())
Background.convert()
Background.fill((0, 0, 0))


# 數地雷與 dfs 所需之八個方向分量
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def init():
    """遊戲初始化．"""
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


def dfs(i: int, j: int):
    """以「深度優先搜尋」找出連通的無雷區．

    Args:
        i: 從第幾列開始
        j: 從第幾行開始

    Returns:
        True，當沒踩到雷．
        False，當踩到雷．
    """
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
                    if not dfs(x, y):
                        return False
    return True


def gg(win: bool):
    """詢問是否再來一局．

    Args:
        win: 是輸或贏．
    
    Returns:
        True，當使用者要再來一局．
        False，當使用者不要再來一局．
    """
    global Time
    strs = [['GG', '你超爛ＱＱ\n\n再來一局ㄇ？？', 'error'], ['Win', '你贏惹 o\'_\'o\n費時：' +
                                                  datetime.fromtimestamp(time.time() - Time).strftime("%M:%S") + '\n再來一局ㄇ？？', 'info']]
    if messagebox.askyesno(strs[win][0], strs[win][1], icon=strs[win][2]):
        init()
        return True
    else:
        return False


def main():
    """遊戲主函式．"""
    global Cnt, Lst
    init()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            elif event.type == pg.MOUSEBUTTONUP:
                i, j = event.pos[0] // 50, event.pos[1] // 50
                if not 0 <= i < 9 or not 0 <= j < 9:
                    continue
                if event.button == 1:
                    if not dfs(i, j):
                        if gg(False):
                            continue
                        else:
                            return
                elif event.button == 3:
                    Cnt += Map[i][j].right_click()

        text = Font.render("Cnt: %2d   Time: " % Cnt + datetime.fromtimestamp(time.time() - Time).strftime("%M:%S     "), True,
                           (192, 192, 192), (0, 0, 0))
        Screen.blit(text, (15, 465))
        Sprites.draw(Screen)
        pg.display.update()

        if Lst == Mines:
            if gg(True):
                continue
            else:
                return

        Clock.tick(FPS)


if __name__ == '__main__':
    main()
    pg.quit()
