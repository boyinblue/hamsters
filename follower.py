from roboid import *

hamster = HamsterS()

while True:
    # 근접 센서 값이 너무 작으면 그냥 정지한다.
    if hamster.left_proximity() < 15 and hamster.right_proximity() < 15:
        hamster.stop()
        continue

#    if hamster.left_proximity() > 40 and hamster.right_proximity() > 40:
#        hamster.stop()
#        continue
    
    hamster.wheels( ( 50 - hamster.left_proximity() ) * 2, ( 50 - hamster.right_proximity() ) * 2)