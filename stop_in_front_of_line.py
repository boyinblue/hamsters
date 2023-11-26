from roboid import *

hamster = HamsterS()

hamster.wheels(100,100)
while True:
    if hamster.right_floor() < 80:
        hamster.wheels(0,0)
        hamster.move_backward(2)
        break
