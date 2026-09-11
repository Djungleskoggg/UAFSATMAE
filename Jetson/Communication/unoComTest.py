#
# Test Script to communicate with Arduino via serial port
# Will add sending command to arduino , then make a new file thats the complete package done right
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

def main():
    if(ser.is_open):
        while True:
            data = ser.readline().decode('utf-8').strip()
            print("Received:", data)
            ser.write(b'hello\n')
            time.sleep(0.5)
            

if __name__ == "__main__":
    main()