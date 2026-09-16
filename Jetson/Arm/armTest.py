from roarm-ik import m2Arm
import time

def main():
    arm = m2Arm(port = "/dev/ttyUSB0") # change port to match arms com.
    arm.move_init()
    time.sleep(1)
    # Changes the X,Y,Z coordinate to match intended location
    arm.move_to_xyz(10,10,10)


if __name__ == "__main__":
    main()
