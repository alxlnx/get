#!/usr/bin/python3

import RPi.GPIO as GPIO
from mylib import dec2bin

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MAX_DAC_VOLTAGE = 3.3
MAX_DAC_NUMBER = 255
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    while(True):
        n = input("Please enter a number between 0 and 255: ")

        if n == 'q': 
            print('\nBye!')
            break
        elif ('.' in n):
            print("\nEntered value is not a whole number!")
            break
        elif not n.isdigit():
            print("\n Entered value is not a number!")
            break
        elif int(n) < 0:
            print("\nEntered value is negative!")
            break
        elif int(n) > 255: 
            print("\nEntered number is too big!")
            break
        else: n = int(n)

        voltage = n * MAX_DAC_VOLTAGE / MAX_DAC_NUMBER
        for pin, state in zip(dac, dec2bin(n)):
            GPIO.output(pin, state)
        print(f"Expected voltage on DAC is {voltage:.2f}V")
except KeyboardInterrupt:
    print("\nBye!")
finally:
    [GPIO.output(pin, GPIO.LOW) for pin in dac]
    GPIO.cleanup()