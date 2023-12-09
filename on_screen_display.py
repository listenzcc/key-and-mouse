"""
File: on_screen_display.py
Author: Chuncheng Zhang
Date: 2023-12-09
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2023-12-09 ------------------------
# Requirements and constants
import os
import sys
import win32api
import win32con
import win32gui

from rich import print, inspect

from random import choice, randrange
from string import ascii_letters

import pygame as pg


# %% ---- 2023-12-09 ------------------------
# Function and class

background = (0, 0, 0)


def random_letters(n):
    """Pick n random letters."""
    return ''.join(choice(ascii_letters) for _ in range(n))


def main(screen):
    screen_rect = screen.get_rect()
    font = pg.font.Font(None, 45)
    clock = pg.time.Clock()
    color = (randrange(256), randrange(256), randrange(256))
    txt = font.render(random_letters(randrange(5, 21)), True, color)
    timer = 10
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    done = True

        timer -= 1
        # Update the text surface and color every 10 frames.
        if timer <= 0:
            timer = 10
            color = (randrange(256), randrange(256), randrange(256))
            txt = font.render(random_letters(randrange(5, 21)), True, color)

        screen.fill(background)  # (30, 30, 30))
        screen.blit(txt, txt.get_rect(center=screen_rect.center))

        pg.display.flip()
        clock.tick(30)


# %% ---- 2023-12-09 ------------------------
# Play ground
if __name__ == '__main__':
    pg.init()
    info = pg.display.Info()
    inspect(info)
    screen = pg.display.set_mode((500, 500), 32, pg.NOFRAME)

    # Create layered window
    hwnd = pg.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

    # Always on top
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,
                          0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    # Set window transparency color
    win32gui.SetLayeredWindowAttributes(
        hwnd, win32api.RGB(*background), 0, win32con.LWA_COLORKEY)

    #
    main(screen)
    pg.quit()
    sys.exit()


# %% ---- 2023-12-09 ------------------------
# Pending


# %% ---- 2023-12-09 ------------------------
# Pending
