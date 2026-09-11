import time

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
    while(True):
        for event in pg.event.get(): # passing events so that the joystick updates and doesnt freeze. - jerick
            pass
        x_joystick = round((pg.joystick.Joystick(0).get_axis(0)) * 100)  
        y_joystick = round((pg.joystick.Joystick(0).get_axis(1)) * -100)
        # serialCon.write(f'{x_joystick} {y_joystick} '.encode("utf-8"))
        print(f"{x_joystick} {y_joystick}")
        time.sleep(0.1)
    



if __name__ == "__main__":
    main()