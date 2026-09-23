import time
from roarm-ik import m2Arm
import pygame as pg
import serial as ser

pg.init() # initializing pygame so that events exist or somtin - jerick
serialCon = ser.Serial('/dev/ttyACM0', 9600)

pg.joystick.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
print(joysticks)
clock = pg.time.Clock()

x_joystick = 0
y_joystick = 0

def main():
    arm = m2Arm(port = "/dev/ttyUSB0")
    arm.move_init()
    time.sleep(1)

    x = 0.0
    y = 0.0
    z = 0.0

    while(True):
        for event in pg.event.get():
            pass
        x_joystick = round((pg.joystick.Joystick(0).get_axis(0)))  
        y_joystick = round((pg.joystick.Joystick(0).get_axis(1)) * -1)

        serialCon.write(f'{x_joystick* 100} {y_joystick* 100} '.encode("utf-8"))
        print(f"{x_joystick* 100} {y_joystick* 100}")

        x1_joystick = round((pg.joystick.Joystick(0).get_axis(2)) * .25)  
        y1_joystick = round((pg.joystick.Joystick(0).get_axis(3)) * -.25)

        if(pg.joystick.Joystick(0).get_button(4)):
            z = z + .25
        if(pg.joystick.Joystick(0).get_button(5)):
            z = z - .25

        x = x + x1_joystick
        y = y + y1_joystick

        arm.move_to_xyz(x,y,z)
        time.sleep(.1)

if __name__ == "__main__":
    main()
