import pygame as pg
import serial as ser

serialCon = ser.Serial('/dev/ttyACM0', 9600)

pg.joystick.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
clock = pg.time.Clock()

x_joystick = 0
y_joystick = 0

def main():
    while(True):
        x_joystick = round((pg.joystick.Joystick(0).get_axis(0))*100)
        y_joystick = round((pg.joystick.Joystick(0).get_axis(1))*100)
        serialCon.write(f'{x_joystick} {y_joystick}'.encode("utf-8"))
        print(x_joystick +""+ y_joystick)
        clock.tick(60)
    



if __name__ == "__main__":
    main()