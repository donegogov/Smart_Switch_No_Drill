from gpiozero import Device, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as GPIO
from time import sleep

# setting up
Device.pin_factory = PiGPIOFactory()

servo = AngularServo(18, min_pulse_width=0.6/1000, max_pulse_width=2.3/1000)

pir_pin = 17

GPIO.setmode( GPIO.BCM )

GPIO.setup( pir_pin, GPIO.IN )

motion_mode = False

def turnSwitchOnOff(onOff):
    if onOff == True:
        servo.angle = -64 #Turn ON Lamp
    elif onOff == False:
        servo.angle = 43 #Turn OFF Lamp
    sleep(2)
    servo.angle = 0
    sleep(1)
        
def motionDetectOnOff(onOff):
    global motion_mode
    if onOff == True:
        motion_mode = True
    elif onOff == False:
        motion_mode = False
        
    while motion_mode:
        print(GPIO.input(pir_pin))
        sleep(0.1)
        if GPIO.input(pir_pin) == 1:
            servo.angle = -64 #Turn On Lamp 
            sleep(10)
            servo.angle = 43 #Turn Off Lamp
            sleep(1)
            servo.angle = 0
            sleep(1)


