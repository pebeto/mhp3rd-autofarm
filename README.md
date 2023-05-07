# mhp3rd-autofarm
A simple python script to automate farming in Monster Hunter Portable 3rd (MHp3rd) in PPSSPP emulator.

## Implemented features
- [x] Generic interface for automating movement in all the releases of the game (e.g. MHFU)
- [x] Automatic box collection
- [x] Mining
    - [x] Point 1
    - [ ] Point 2
    - [ ] Point 3
    - [ ] Point 4
- [x] Bug catching
- [x] Fishing
    - [x] Pier 1
    - [ ] Pier 2
    - [ ] Pier 3
- [x] Crop gathering (all the rows)
- [ ] Mushroom gathering
- [ ] Honey gathering

## Requirements
- Python 3.10 or above
- PyAutoGUI 0.9.53 or above
- PPSSPP emulator with default controls settings

## How to use
1. Open PPSSPP emulator and load MHp3rd game
2. Place your character in the village entrance (as loaded by default)
3. Press escape and with the mouse pointing to the emulator window, run the script with `python3 ./src/main.py`. Stop using the computer until the script finishes.

## Limitations
- The script works only with the original framerate of the game (30 FPS). Also, speeding up the game will make the script fail.
- Due to the use of an external way to automate movement, the character won't have smooth movement (which means it may become sluggish).
- The script doesn't have a time optimization, so you will see the character waiting for a few seconds before doing the next action.
- Having lag in the game could make the script fail.

## Future improvements
- Autofocus the emulator window
- Optimize time between actions
- **A better way to automate movement**
    - A built-in way in the emulator to automate movement (it doesn't exist nowadays)
    - Using a memory editor to change the character position and execute actions
    - Creating a plugin that allows automating movement (and it should work in the PSP console too)
