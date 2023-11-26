from roboid import *
import keyboard

hamster = HamsterS()

while True:
    if keyboard.read_key() == "w":
        hamster.move_forward(1)
    elif keyboard.read_key() == "s":
        hamster.move_backward(1)
    elif keyboard.read_key() == "a":
        hamster.turn_left(10)
    elif keyboard.read_key() == "d":
        hamster.turn_right(10)