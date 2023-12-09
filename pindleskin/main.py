"""
File: main.py
Author: Chuncheng Zhang
Date: 2023-12-07
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


# %% ---- 2023-12-07 ------------------------
# Requirements and constants
import time
import mouse
import keyboard
import contextlib
import pandas as pd

from rich import print, inspect


# %% ---- 2023-12-07 ------------------------
# Function and class

class Recorder(object):
    events = []
    xy = (0, 0)
    tic = time.time()

    def __init__(self):
        pass

    def on_keyevent(self, event):
        t = time.time() - self.tic
        self.events.append(('key', event, t, self.xy))

    def on_mouseevent(self, event):
        t = time.time() - self.tic

        # Update mouse position in realtime
        if isinstance(event, mouse.MoveEvent):
            self.xy = (event.x, event.y)

        # Not record mouse-movement event
        # self.events.append(('mouse', event, t, self.xy))

        if isinstance(event, mouse.ButtonEvent):
            self.events.append(('button', event, t, self.xy))

    @contextlib.contextmanager
    def safe_hook(self):
        try:
            mouse.hook(self.on_mouseevent)
            keyboard.hook(self.on_keyevent)
            yield True
        finally:
            mouse.unhook_all()
            keyboard.unhook_all()

    def loop(self):
        print('Loop starts')
        with self.safe_hook():
            keyboard.wait('[')
            self.events = []
            self.running = True
            self.tic = time.time()
            while self.running:
                keyboard.wait(']')
                self.running = False
                time.sleep(0.00001)
        print('Loop ends')


# %% ---- 2023-12-07 ------------------------
# Play ground
if __name__ == '__main__':
    recorder = Recorder()
    recorder.loop()

    df = pd.DataFrame(recorder.events,
                      columns=['event', 'value', 'time', 'pos'])
    df.to_csv('record.csv')
    print(df)


# %% ---- 2023-12-07 ------------------------
# Pending


# %% ---- 2023-12-07 ------------------------
# Pending
