from roboid import *

hamster = HamsterS()

target_proximity = 100

hamster.wheels(100,100)

def stop_method1():
    while True:
        if hamster.left_proximity() > 85 or hamster.right_proximity() > 85:
            hamster.wheels(0,0)
            hamster.sound("beep")
            wait(1000)
            return

def stop_method2():
    while True:
        if hamster.left_proximity() > 87 or hamster.right_proximity() > 87:
            hamster.stop()
            hamster.sound("beep")
            hamster.move_forward(1.8)
            hamster.note("C4", 0.095)
            hamster.note("off", 0.005)
            hamster.note("E4", 0.095)
            hamster.note("off", 0.005)
            hamster.note("G4", 0.095)
            hamster.note("off", 0.005)
            hamster.note("C5", 0.095)
            hamster.note("off")
            return
        hamster.wheels( ( target_proximity - hamster.left_proximity() ), ( target_proximity - hamster.right_proximity() ) )

#stop_method1()
stop_method2()