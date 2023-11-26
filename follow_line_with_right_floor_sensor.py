from roboid import *
from enum import Enum

hamster = HamsterS()

while True:
    # 근접 센서 값이 너무 작으면 그냥 정지한다.
#    if hamster.left_proximity() < proximity_threshold and hamster.right_proximity() < proximity_threshold:
#        hamster.stop()
#        sound(SoundMode.OBJ_LOST)
#        continue

    # 너무 어두워지면 그냥 정지한다.
    if hamster.light() < 10:
        hamster.stop()
        continue

    print("Floor : ", hamster.left_floor(), hamster.right_floor())

    if hamster.right_floor() < 90:
        hamster.sound("beep")
        hamster.wheels(0,60)
    else:
        hamster.wheels(40,0)