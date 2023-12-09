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

import random
import win32api
import win32con
import win32gui
import pygame as pg

from string import ascii_letters
from rich import print, inspect

from . import LOGGER


# %% ---- 2023-12-09 ------------------------
# Function and class
class onScreenDisplay(object):
    width = 600
    height = 400
    background = (0, 0, 0)
    fps = 30

    font_h1 = pg.font.Font(None, 45)
    color_h1 = tuple([random.randint(0, 256) for _ in ['r', 'g', 'b']])

    clock = pg.time.Clock()

    def __init__(self):
        self.init_screen()
        LOGGER.debug(f'Initialized {self.__class__}')

    def init_screen(self):
        pg.init()

        info = pg.display.Info()
        inspect(info)

        screen = pg.display.set_mode((self.width, self.height), 32, pg.NOFRAME)

        # Create layered window
        hwnd = pg.display.get_wm_info()["window"]
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                               win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

        # Always on top
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,
                              0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # Set window transparency color
        win32gui.SetLayeredWindowAttributes(
            hwnd, win32api.RGB(*self.background), 0, win32con.LWA_COLORKEY)

        self.screen = screen
        LOGGER.debug(f'Initialized screen: {screen}')
        return screen


# %% ---- 2023-12-09 ------------------------
# Play ground


# %% ---- 2023-12-09 ------------------------
# Pending


# %% ---- 2023-12-09 ------------------------
# Pending
