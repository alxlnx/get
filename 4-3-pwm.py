#!/usr/bin/python3

import RPi.GPIO as GPIO
from small_lib import dec2bin

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MAX_DAC_VOLTAGE = 3.3
MAX_DAC_NUMBER = 255
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

PWM_PIN = 22
GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(PWM_PIN, 1000)

p.start(0.0)

try:
    while(True):
        D = float(input("Enter duty cycle: "))
        p.ChangeDutyCycle(D)


finally:
    [GPIO.output(pin, GPIO.LOW) for pin in dac]
    GPIO.cleanup()