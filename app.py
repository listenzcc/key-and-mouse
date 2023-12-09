"""
File: app.py
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
import time

from threading import Thread
from util.on_screen_display import OnScreenDisplay
from util.mouse_keyboard_watcher import MouseKeyboardWatcher


# %% ---- 2023-12-09 ------------------------
# Function and class


# %% ---- 2023-12-09 ------------------------
# Play ground
if __name__ == '__main__':
    mkw = MouseKeyboardWatcher()
    osd = OnScreenDisplay()

    Thread(target=mkw.loop, daemon=True).start()
    Thread(target=osd.loop, daemon=True).start()

    def loop():
        interval = 1/30

        while True:
            x, y = mkw.xy
            evt = mkw.get_event()
            osd.update_content(dict(h1=f'{x}, {y}', p=f'|{evt}|'))

            time.sleep(interval)

    Thread(target=loop, daemon=True).start()

    input('Enter to escape.')
    mkw.running = False


# %% ---- 2023-12-09 ------------------------
# Pending


# %% ---- 2023-12-09 ------------------------
# Pending
