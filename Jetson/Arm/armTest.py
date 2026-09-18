import time

import roarm_ik.arm as arm

import pygame as pg
import serial as ser

#maybe i should put the joystick in its own class too... idk lol :(
pg.init() # initializing pygame so that events exist or somtin - jerick
serialCon = ser.Serial('/dev/ttyACM0', 9600)

pg.joystick.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
print(joysticks)
clock = pg.time.Clock()

class Arm: #handles all the arm stuff i think lol :)
    def __init__(self):
        self.arm = arm.m2Arm()
        self.arm.move_init()
        self.currentX = 0
        self.currentY = 0
        self.currentZ = 0
    def moveArm(self, x_speed: int, y_speed: int, z_speed: int): 
        self.currentX += x_speed
        self.currentY += y_speed
        self.currentZ += z_speed
        self.arm.move_to_xyz(self.currentX, self.currentY, self.currentZ)

x_joystick = 0
y_joystick = 0
z_joystick = 0

def main():
    arm = Arm()
    while(True):
        for event in pg.event.get(): # passing events so that the joystick updates and doesnt freeze. - jerick
            pass
        x_joystick = round((pg.joystick.Joystick(0).get_axis(0)))  
        y_joystick = round((pg.joystick.Joystick(0).get_axis(1)))
        z_joystick = round((pg.joystick.Joystick(1).get_axis(0)))
        # serialCon.write(f'{x_joystick} {y_joystick} '.encode("utf-8"))
        # print(f"{x_joystick} {y_joystick}")

        arm.moveArm(x_joystick, y_joystick, z_joystick)

        time.sleep(0.1)

if __name__ == "__main__":
    main()