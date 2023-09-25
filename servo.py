import RPi.GPIO as GPIO
import time
from servo import value_mapper

# Define the GPIO pin for the servo control
pwms = {}

def init(pins):
    global pwms
    # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Set up the GPIO pin as an output
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        # Create a PWM instance with a frequency of 50 Hz
        pwms[pin] = GPIO.PWM(pin, 50)
        # Start PWM with 0% duty cycle (servo at 0 degrees)
        pwms[pin].start(0)
    

def stop():
    # Clean up GPIO on exit
    global pwms
    for pwm in pwms.values():
      pwm.stop()
    pwms = {}
    GPIO.cleanup()

def move(pin, degrees):
    try:
        pos = mapped(degrees)
        global pwms
        pwms[pin].ChangeDutyCycle(pos)  # Adjust this value to move the servo
    except KeyboardInterrupt:
        stop()

def mapped(degrees):
    return value_mapper.map_value(degrees, 0, 180, 2.5, 12)