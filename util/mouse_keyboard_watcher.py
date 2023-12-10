"""
File: mouse_keyboard_watcher.py
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
import mouse
import keyboard
import contextlib

from rich import print, inspect

from . import LOGGER


# %% ---- 2023-12-09 ------------------------
# Function and class

class MouseKeyboardWatcher(object):
    events = []
    events_limit = 1e6
    xy = (0, 0)
    framerate = 20  # Hz
    interval = 1/framerate  # Seconds
    tic = time.time()

    def __init__(self):
        pass

    def get_event(self):
        """Get the latest event, if available

        The events are recorded as tuple,
        the meanings are (event_type, event, timestamp, position),
        where the event_type is one of ('key' for keyboard, 'button' for mouse)

        Returns:
            obj: The event
        """
        if not self.events:
            return '-' * 8

        evt = []

        for e in self.events[-8:]:
            if e[0] == 'key':
                c = e[1].name[:2]

            if e[0] == 'button':
                c = e[1].button[0].upper()

            evt.append(c)

        return ','.join(evt)

    def _safe_events(self):
        if len(self.events) > self.events_limit:
            self.events = self.events[:int(1e5)]
            LOGGER.warning(f'Events exceeds its limit({self.events_limit})')

    def on_key_event(self, event: keyboard.KeyboardEvent, record_flag: bool = True):
        if event.event_type != 'down':
            return

        if record_flag:
            t = time.time() - self.tic
            self.events.append(('key', event, t, self.xy))

    def on_mouse_event(self, event: mouse.MoveEvent, record_flag: bool = True):
        if isinstance(event, mouse.MoveEvent):
            # Update mouse position in realtime
            self.xy = (event.x, event.y)
            return

        if event.event_type != 'down':
            # Only record mouse key down event
            return

        # Record mouse-movement event
        # self.events.append(('mouse', event, t, self.xy))

        if record_flag:
            t = time.time() - self.tic
            if isinstance(event, mouse.ButtonEvent):
                self.events.append(('button', event, t, self.xy))

    @contextlib.contextmanager
    def safe_hook(self):
        try:
            mouse.hook(self.on_mouse_event)
            keyboard.hook(self.on_key_event)
            LOGGER.debug('Hooked mouse and keyboard')
            yield True
        finally:
            mouse.unhook_all()
            keyboard.unhook_all()
            LOGGER.debug('Unhooked mouse and keyboard')

    def loop(self):
        LOGGER.debug('Starts loop')
        with self.safe_hook():
            self.events = []
            self.running = True
            self.tic = time.time()
            while self.running:
                time.sleep(self.interval)
        LOGGER.debug('Stopped loop')


# %% ---- 2023-12-09 ------------------------
# Play ground


# %% ---- 2023-12-09 ------------------------
# Pending


# %% ---- 2023-12-09 ------------------------
# Pending
