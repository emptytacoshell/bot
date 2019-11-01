from adafruit_crickit import crickit
from varspeed import Vspeed
import board
import time
import pulseio
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A3)
lastsensor = 0

crickit.servo_1.throttle = 0
crickit.servo_2.throttle = -0.05

servo3_position = Vspeed(False)
servo4_position = Vspeed(False)

#crickit.servo_3.angle = 60  #white
#crickit.servo_4.angle = 100  #black

servo1 = crickit.continuous_servo_1
servo2 = crickit.continuous_servo_2

moved = False

def tongue():

    for i in range(0, 5):
        crickit.servo_3.angle = 40
        crickit.servo_4.angle = 125

        time.sleep(.1)

        crickit.servo_3.angle = 125
        crickit.servo_4.angle = 40

        time.sleep(.1)

def right():
        servo1.throttle = 0
        servo2.throttle = 0.1
def left():
        servo1.throttle = -0.9
        servo2.throttle = 0
def lefthalf():
        servo1.throttle = -0.5
        servo2.throttle = 0
def straight():
        servo1.throttle =-0.1
        servo2.throttle = 0.1
while True:
    try:
        print((sonar.distance))
        if (sonar.distance>=45.5) & (sonar.distance <55): #annoying
            print("someone is here")
            right()
            time.sleep(1)
            left()
            time.sleep(1)
            right()
            time.sleep(1)
            left()
            time.sleep(1)
            right()
            time.sleep(1)
            lefthalf()
            time.sleep(1)
            straight()
            servo1.throttle = 0 # stop
            servo2.throttle = -0.05
            moved = True

            tongue()

        if (sonar.distance>=56) and moved == True: #backward & pretend didn't do anything
            print("I didn't do anything!")
            servo1.throttle = -1 #turn around
            servo2.throttle = -1
            time.sleep(2.5)
            servo1.throttle = 0 # stop
            servo2.throttle = -0.05
            moved = False
            crickit.servo_3.angle = 40
            crickit.servo_4.angle = 140

    except RuntimeError:
        print ("error")


        #backward in x shape, avoid face, one more action, active ignoring : show purpose