from roboid import *
from enum import Enum

class SoundMode(Enum):
    NULL = 0
    DARK = 1
    OBJ_LOST = 2

class DriveMode(Enum):
    STRIGHT = 0
    TURN_LEFT = 1
    TURN_RIGHT = 2

hamster = HamsterS()

proximity_threshold = 15
target_proximity = 40
weight = 10
last_mode = SoundMode.NULL
prev_floor = [0, 0]
drive_mode = DriveMode.STRIGHT

def sound(mode):
    global last_mode

    if last_mode == mode:
        return

    if mode == SoundMode.NULL:
#        hamster.sound("beep")
        hamster.note("C4")
        wait(50)
        hamster.note("off", 0.05) # break for the same notes
        hamster.note("G4")
        wait(50)
        hamster.note("off", 0.05) # break for the same notes
    elif mode == SoundMode.DARK:
        hamster.sound("robot")
    elif mode == SoundMode.OBJ_LOST:
#        hamster.sound("siren")
        hamster.note("G4")
        wait(50)
        hamster.note("off", 0.05) # break for the same notes
        hamster.note("C4")
        wait(50)
        hamster.note("off", 0.05) # break for the same notes

    last_mode = mode

while True:
    # 근접 센서 값이 너무 작으면 그냥 정지한다.
#    if hamster.left_proximity() < proximity_threshold and hamster.right_proximity() < proximity_threshold:
#        hamster.stop()
#        sound(SoundMode.OBJ_LOST)
#        continue

    # 너무 어두워지면 그냥 정지한다.
    if hamster.light() < 10:
        hamster.stop()
        sound(SoundMode.DARK)
        continue

    sound(SoundMode.NULL)
    print("Floor : ", hamster.left_floor(), hamster.right_floor())
#    continue

    if hamster.right_floor() < 35 or hamster.left_floor() < 35:
        if drive_mode == DriveMode.STRIGHT:
            if hamster.right_floor() < hamster.left_floor():
                drive_mode == DriveMode.TURN_LEFT
            elif hamster.right_floor() > hamster.left_floor():
                drive_mode == DriveMode.TURN_RIGHT
    else:
        if drive_mode != DriveMode.STRIGHT:
            drive_mode = DriveMode.STRIGHT

    if drive_mode == DriveMode.STRIGHT:
        hamster.wheels(20,20)
    elif drive_mode == DriveMode.TURN_LEFT:
        hamster.wheels(0, 40)
    else:
        hamster.wheels(40,0)