import time
import pyautogui as pa
from contextlib import nullcontext

from controller import ActionButtons
from controller import DirectionalPad
from controller import ShoulderButtons


def press_key(button, duration=0.1, pause=0, run=False):
    '''Presses the given button for the given amount of time'''
    press_keys([button], duration=duration, pause=pause, run=run)


def press_keys(buttons, duration=0.1, pause=0, run=False):
    '''Presses the given button(s) for the given amount of time'''
    start_time = time.time()

    with pa.hold(ShoulderButtons.R) if run else nullcontext():
        while time.time() - start_time < duration:
            for button in buttons:
                pa.keyDown(button)
        for button in buttons:
            pa.keyUp(button)
    time.sleep(pause)


def unpause_emulator():
    '''Unpauses the emulator by clicking the mouse and pressing the escape key'''
    mouse_x, mouse_y = pa.position()
    pa.leftClick(mouse_x, mouse_y)
    press_key('esc')


def collect_box():
    '''Collects items from opened box'''
    box_rows = 5
    box_cols = 8

    print("Sending to item box...")
    press_key(DirectionalPad.DOWN, pause=0.3)
    press_key(ActionButtons.CIRCLE)

    for i in range(box_rows):
        print(f"Collecting row {i+1}...")
        for j in range(box_cols):
            press_key(ActionButtons.CIRCLE)
            press_key(DirectionalPad.RIGHT)
        press_key(DirectionalPad.DOWN)
    press_key(ActionButtons.CROSS)
    press_key(ActionButtons.CIRCLE)
