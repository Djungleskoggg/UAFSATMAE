import time
from roarm_ik import m2Arm
import pygame as pg
import serial as ser

pg.init() # initializing pygame so that events exist or somtin - jerick
serialCon = ser.Serial('/dev/ttyACM0', 115200)

pg.joystick.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
print(joysticks)


x_joystick = 0.0
y_joystick = 0.0

def main():
    arm = m2Arm(port = "/dev/ttyUSB0")
    arm.move_init()

    alignment = 0.0
    latch = False
    
    clock = pg.time.Clock()
    
    x = 0.0
    y = 10.0
    z = 10.0

    angle_grip = 10.0

    while(True):
        for event in pg.event.get():
            pass
        pg.event.pump()
        x_joystick = round((pg.joystick.Joystick(0).get_axis(0)))  
        y_joystick = round((pg.joystick.Joystick(0).get_axis(1)))

        if(pg.joystick.Joystick(0).get_button(13)): # button 13 is the start button on the xbox controller
            latch = not latch

            if latch:
                alignment = 1
            else:  
                alignment = 0

        serialCon.write(f'{x_joystick* 100} {y_joystick* 100} {alignment*1}'.encode("utf-8"))
        print(f"{x_joystick* 100} {y_joystick* 100} {x} {y} {z} {alignment} {angle_grip}")

        x1_joystick = round((pg.joystick.Joystick(0).get_axis(2)) ,1)*-1
        y1_joystick = round((pg.joystick.Joystick(0).get_axis(3)) ,1)*-1

        if(pg.joystick.Joystick(0).get_hat(0)==(0,1)):  #control z axis movement
            z = z + .25
        if(pg.joystick.Joystick(0).get_hat(0)==(0,-1)):
            z = z - .25

        if(pg.joystick.Joystick(0).get_hat(0)==(1,0)):  #control gripper angle
            angle_grip = angle_grip + .25
        if(pg.joystick.Joystick(0).get_hat(0)==(-1,0)):
            angle_grip = angle_grip - .25

        if(x1_joystick > 0.25 or x1_joystick < -0.25):
            x += x1_joystick
        if(y1_joystick > 0.25 or y1_joystick < -0.25):
            y += y1_joystick

        arm.gripper_angle_ctrl(angle_grip,10,3)
        arm.move_to_xyz(y,x,z)
        clock.tick(60)
if __name__ == "__main__":
    main()
