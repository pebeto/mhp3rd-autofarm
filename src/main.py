import time

from utils import press_key
from utils import press_keys
from utils import collect_box
from utils import unpause_emulator

from controller import AnalogStick
from controller import ActionButtons
from controller import DirectionalPad


def move_to_farm():
    '''Moves the character to the farm'''
    print('Moving to farm...')
    press_keys([AnalogStick.UP, AnalogStick.LEFT],
               duration=2.8, pause=0.5, run=True)
    press_key(ActionButtons.SQUARE)
    press_key(AnalogStick.UP, duration=3)


def mine_minerals(times):
    '''Mine minerals from the vein'''
    for i in range(times):
        print(f"Mining counter: {i+1}")
        press_key(ActionButtons.SQUARE, pause=3)


def collect_minerals():
    '''Collects minerals from the farm'''
    print('Moving to mineral veins...')
    press_key(AnalogStick.UP, duration=5.5, run=True)
    press_keys([AnalogStick.UP, AnalogStick.RIGHT],
               duration=2.6, pause=0.5, run=True)
    mine_minerals(4)


def collect_bugs():
    '''Collects bugs from the farm'''
    print('Moving to insect trapper...')
    press_keys([AnalogStick.LEFT, AnalogStick.DOWN],
               duration=2.3, run=True)
    press_key(AnalogStick.LEFT, duration=2.9, pause=0.5, run=True)
    print("Opening insect trapper...")
    press_key(ActionButtons.SQUARE, pause=3.2)
    collect_box()


def collect_fishes():
    '''Collects fishes from the farm'''
    print('Moving to fishing spot...')
    press_keys([AnalogStick.LEFT, AnalogStick.DOWN], duration=3.6, run=True)
    press_keys([AnalogStick.LEFT, AnalogStick.UP],
               duration=4, pause=0.5, run=True)
    print("Opening fishing spot...")
    press_key(ActionButtons.SQUARE, pause=4.2)
    collect_box()


def open_crop_spot():
    '''Opens crop spot'''
    press_key(ActionButtons.SQUARE, pause=4.2)
    collect_box()


def collect_crops():
    '''Collects crops from the farm'''
    print('Moving to crops...')
    press_key(AnalogStick.RIGHT, duration=4.2, run=True)
    press_key(AnalogStick.DOWN, duration=0.7, pause=0.5)

    n_crop_spots = 3
    for i in range(n_crop_spots):
        open_crop_spot()
        press_key(
            AnalogStick.UP,
            duration=0.8 if i < 1 else 0.35,
            pause=1,
            run=True)


def do_farm_activities():
    '''Performs farm activities'''
    print('Starting farm activities...')
    collect_minerals()
    collect_bugs()
    collect_fishes()
    collect_crops()


def main():
    unpause_emulator()
    move_to_farm()
    time.sleep(4)
    do_farm_activities()


if __name__ == "__main__":
    main()
