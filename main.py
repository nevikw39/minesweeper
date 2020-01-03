from grid import *
from pygame.locals import MOUSEBUTTONDOWN, QUIT, USEREVENT, Color
from pygame import *
import pygame as pg
import os
import random
import sys
import time
import threading
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw()


WINDOW_WIDTH = 450
WINDOW_HEIGHT = 500
FPS = 60

pg.init()

Font = pg.font.Font(None, 24)
Sprites = pg.sprite.Group()

Clock = pg.time.Clock()
Screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Background = pg.Surface(Screen.get_size())
Background.convert()
Background.fill((0, 0, 0))
pg.display.set_caption("Simple Minesweeper by nevikw39")


def init():
    global Cnt, Map, Mines, Flags, Time, Timer
    Cnt = 10
    Map = [[] for _ in range(9)]
    Mines = set(random.sample(range(81), 10))
    Flags = set()
    Time = time.time()
    Timer = threading.Thread(target = timer)
    for i, e in enumerate(Map):
        for j in range(9):
            e.append(grid(i, j, i * 9 + j in Mines))
            Sprites.add(e[j])
    print("Mines =", Mines)
    Timer.start()


dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(i, j):
    Map[i][j].s = 2
    n = 0

    for k in range(8):
        x = i + dx[k]
        y = j + dy[k]
        if not 0 <= x < 9 or not 0 <= y < 9:
            continue
        elif Map[x][y].is_mine:
            n += 1

    if not n:
        for k in range(8):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < 9 and 0 <= y < 9 and Map[x][y].s == 0:
                dfs(x, y)

    Map[i][j].left_click(n)


def gg():
    global Time, Timer
    duration = time.time() - Time
    Time = 0
    threading.Event().set()
    if messagebox.askyesno('GG', '你超爛ＱＱ\n\n再來一局ㄇ？？', icon='error'):
        init()
        return True
    else:
        return False


def win():
    global Time, Timer
    duration = time.time() - Time
    Time = 0
    threading.Event().set()
    if messagebox.askyesno('Win', '你贏惹 o\'_\'o\n\n再來一局ㄇ？？', icon='info'):
        init()
        return True
    else:
        return False


def timer():
    while True:
        text = Font.render("Cnt = %d" % Cnt, True, (192, 192, 192))
        Screen.blit(Background, (0, 0))
        Screen.blit(text, (15, 465))
        time.sleep(1)


def main():
    global Cnt
    init()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            elif event.type == pg.MOUSEBUTTONDOWN:
                i, j = event.pos[0] // 50, event.pos[1] // 50
                if not 0 <= i < 9 or not 0 <= j < 9:
                     continue
                Map[i][j].image = img_click

            elif event.type == pg.MOUSEBUTTONUP:
                i, j = event.pos[0] // 50, event.pos[1] // 50
                if not 0 <= i < 9 or not 0 <= j < 9:
                     continue
                if event.button == 1:
                    if (i * 9 + j in Mines):
                        if gg():
                            continue
                        else:
                            return
                    dfs(i, j)
                elif event.button == 3:
                    if Map[i][j].s == 2:
                        continue
                    elif Map[i][j].s == 1:
                        Flags.remove(i * 9 + j)
                        Cnt += 1
                    elif Map[i][j].s == 0:
                        Flags.add(i * 9 + j)
                        Cnt -= 1
                    Map[i][j].right_click()
                    if not Cnt and Flags == Mines:
                        if win():
                            continue
                        else:
                            return

        Sprites.draw(Screen)
        pg.display.update()
        Clock.tick(FPS)


if __name__ == '__main__':
    main()
    pg.quit()
