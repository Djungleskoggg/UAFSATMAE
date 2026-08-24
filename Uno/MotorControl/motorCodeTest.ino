#include "CytronMotorDriver.h"

// All code is theoretical and untested until I can work with the motors directly.

/*
  In this little test code, 
  Motor 1 is Front left, Motor 2 is Front right
  Motor 3 is Back Left, Motor 4 is Back Right.
  This is because we will need 2 of the MDD10A, so in my head
  the first will be for the front wheels and the second will be the back wheels.

*/
// Pins were pre-determined on the Figma already so I just copied those pins.
CytronMD motor1(PWM_DIR, 8, 5); // Motor 1. PWM pin is 8, DIR pin is 5
CytronMD motor2(PWM_DIR, 9, 4);   // Motor 2. PWM pin is 9, DIR pin is 4
CytronMD motor3(PWM_DIR, 10, 3);   // Motor 3. PWM pin is 10, DIR pin is 3
CytronMD motor4(PWM_DIR, 11, 2);   // Motor 4. PWM pin is 11, DIR pin is 2

void setup() {
  Serial.begin(115200);
}

void loop() {
  // My big ol encompassing if statement that checks to see if the serial connection has any data coming through.
  if(Serial.available() > 0){
    // These next if statements are purposefully left with no condition for the purpose of being filled in.
    if(){ // straight forward
      motor1.setSpeed(128);
      motor2.setSpeed(128);
      motor3.setSpeed(128);
      motor4.setSpeed(128);
    }
    if(){ // straight backwards
      motor1.setSpeed(-128);
      motor2.setSpeed(-128);
      motor3.setSpeed(-128);
      motor4.setSpeed(-128);
    }
    if(){ // sideways right
      motor1.setSpeed(128);
      motor2.setSpeed(-128);
      motor3.setSpeed(-128);
      motor4.setSpeed(128);
    }
    if(){ // sideways left
      motor1.setSpeed(-128);
      motor2.setSpeed(128);
      motor3.setSpeed(128);
      motor4.setSpeed(-128);
    }
    if(){ // diagonal right
      motor1.setSpeed(128);
      motor2.setSpeed(0);
      motor3.setSpeed(0);
      motor4.setSpeed(128);
    }
    if(){ // diagonal left
      motor1.setSpeed(0);
      motor2.setSpeed(128);
      motor3.setSpeed(128);
      motor4.setSpeed(0);
    }
    if(){ // diagonal back-right 
      motor1.setSpeed(-128);
      motor2.setSpeed(0);
      motor3.setSpeed(0);
      motor4.setSpeed(-128);
    }
    if(){ // diagonal back-left 
      motor1.setSpeed(0);
      motor2.setSpeed(-128);
      motor3.setSpeed(-128);
      motor4.setSpeed(0);
    }
    if(){ // concerning right
      motor1.setSpeed(128);
      motor2.setSpeed(0);
      motor3.setSpeed(128);
      motor4.setSpeed(0);
    } 
    if(){ // concerning left
      motor1.setSpeed(0);
      motor2.setSpeed(128);
      motor3.setSpeed(0);
      motor4.setSpeed(128);
    } 
    if(){ // turn around right
      motor1.setSpeed(128);
      motor2.setSpeed(-128);
      motor3.setSpeed(128);
      motor4.setSpeed(-128);
    } 
    if(){ // turn around left
      motor1.setSpeed(-128);
      motor2.setSpeed(128);
      motor3.setSpeed(-128);
      motor4.setSpeed(128);
    } 
    if(){ // rear axis turn right
      motor1.setSpeed(128);
      motor2.setSpeed(-128);
      motor3.setSpeed(0);
      motor4.setSpeed(0);
    }
    if(){ // rear axis turn left
      motor1.setSpeed(-128);
      motor2.setSpeed(128);
      motor3.setSpeed(0);
      motor4.setSpeed(0);
    }
    

    if(){ // stop
      motor1.setSpeed(0);
      motor2.setSpeed(0);
      motor3.setSpeed(0);
      motor4.setSpeed(0);
    }
  }
}
