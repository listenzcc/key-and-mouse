"""
File: replay.py
Author: Chuncheng Zhang
Date: 2023-12-07
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Automatic keyboard and mouse operation for quickly KP. in Diablo II.

How to use:
    1. Start the script;
    2. Start Diablo II;
    3 (loop). Choose my Sor char and enter into the game of Act V in the hell level;
    4 (loop). Press '[' to start the script;
    5 (loop). Wait for the script to complete, the Sor char will automatically KP;
    6. Back to 3 to another KP round.

Requirements:
    The record.csv is used to make the operations.
    The record.csv is made by the main.py,
    which records the operations in a game.
    

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2023-12-07 ------------------------
# Requirements and constants
import time
import mouse
import keyboard
import pandas as pd

from threading import Thread

from rich import print


# %% ---- 2023-12-07 ------------------------
# Function and class

k = 15


def click_on(button, delay: float, x: int, y: int):
    y += k
    x -= k
    time.sleep(delay)
    mouse.move(x, y)
    mouse.click(button)


def key_press(name: str, delay: float, x: int, y: int):
    y += k
    x -= k
    time.sleep(delay)
    mouse.move(x, y)
    keyboard.press_and_release(name)


# %% ---- 2023-12-07 ------------------------
# Play ground
if __name__ == '__main__':
    df = pd.read_csv('record.csv')
    print(df)
    select = df[df['event'].map(lambda e: e in ['button', 'key'])]
    select.index = range(len(select))
    print(select)

    while True:
        keyboard.wait('[')
        for i in select.index:
            value = select.loc[i, 'value']
            delay = select.loc[i, 'time']
            x, y = eval(select.loc[i, 'pos'])
            if select.loc[i, 'event'] == 'button' and "event_type='down'" in value:

                if "button='left'" in value:
                    button = mouse.LEFT
                elif "button='right'" in value:
                    button = mouse.RIGHT

                t = Thread(target=click_on,
                           args=(button, delay, x, y),
                           daemon=True)
                t.start()

            if select.loc[i, 'event'] == 'key' and 'down)' in value:
                name = value[-7]
                t = Thread(target=key_press,
                           args=(name, delay, x, y),
                           daemon=True)
                t.start()

        time.sleep(10)

        # keyboard.wait(']')
        # break

    # keyboard.wait('[')

    # keyboard.wait('[')
    # time.sleep(0.93)
    # keyboard.press_and_release('d')
    # time.sleep(2.06)
    # mouse.move(x=919, y=1108)
    # mouse.click()


# %% ---- 2023-12-07 ------------------------
# Pending


# %% ---- 2023-12-07 ------------------------
# Pending
