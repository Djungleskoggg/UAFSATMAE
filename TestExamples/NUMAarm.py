from roarm_ik.arm import m2Arm
import time
import pygame 

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

class XboxController:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def get_axis(self, axis):
        pygame.event.pump()
        return self.controller.get_axis(axis)

def main():
    arm = m2Arm()
    arm.move_init()
    time.sleep(1)
    # Changes the X,Y,Z coordinate to match intended location
    arm.move_to_xyz(0, 0, 0)

if __name__ == "__main__":
    main()