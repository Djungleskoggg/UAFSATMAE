import time
from roarm_ik import m2Arm
import pygame as pg
import serial as ser

pg.init() # initializing pygame so that events exist or somtin - jerick
#serialCon = ser.Serial('/dev/ttyACM0', 9600)

pg.joystick.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
print(joysticks)
clock = pg.time.Clock()

x_joystick = 0.0
y_joystick = 0.0

def main():
    arm = m2Arm(port = "/dev/ttyUSB0")
    arm.move_init()
    time.sleep(1)

    x = 0.0
    y = 10.0
    z = 10.0

    while(True):
        for event in pg.event.get():
            pass
        x_joystick = round((pg.joystick.Joystick(0).get_axis(0)))  
        y_joystick = round((pg.joystick.Joystick(0).get_axis(1)) * -1)

        # serialCon.write(f'{x_joystick* 100} {y_joystick* 100} '.encode("utf-8"))
        print(f"{x_joystick* 100} {y_joystick* 100} {x} {y} {z}")

        x1_joystick = round((pg.joystick.Joystick(0).get_axis(2)) ,1)*-1  
        y1_joystick = round((pg.joystick.Joystick(0).get_axis(3)) ,1)

        if(pg.joystick.Joystick(0).get_button(4)):
            z = z + .25
        if(pg.joystick.Joystick(0).get_button(3)):
            z = z - .25

        if(x1_joystick > 0.25 or x1_joystick < -0.25):
            x += x1_joystick
        if(y1_joystick > 0.25 or y1_joystick < -0.25):
            y += y1_joystick

        arm.move_to_xyz(y,x,z)
        time.sleep(.025)

if __name__ == "__main__":
    main()
