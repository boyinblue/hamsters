from roboid import *
from enum import Enum

class SoundMode(Enum):
    NULL = 0
    DARK = 1
    OBJ_LOST = 2

hamster = HamsterS()

proximity_threshold = 15
target_proximity = 40
weight = 2
last_mode = SoundMode.NULL

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
    hamster.wheels( 50 + target_proximity - hamster.right_proximity(), 50 )