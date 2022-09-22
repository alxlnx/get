#!/usr/bin/python3

import RPi.GPIO as GPIO
from small_lib import dec2bin
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
MAX_DAC_VOLTAGE = 3.3
MAX_DAC_NUMBER = 255

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

T = float(input("Enter T: ")) / 2;

try:
    while (True):
        print("--- ONE T: ---")
        print("UP T/4!")
        for i in range(MAX_DAC_NUMBER // 2, MAX_DAC_NUMBER):
            for pin, state in zip(dac, dec2bin(i)):
                GPIO.output(pin, state)
            time.sleep(T / MAX_DAC_NUMBER)
        
        print("DOWN! T/2")
        for i in range(MAX_DAC_NUMBER, 0, -1):
            for pin, state in zip(dac, dec2bin(i)):
                GPIO.output(pin, state)
            time.sleep(T / MAX_DAC_NUMBER)

        print("UP T/4!")
        for i in range(0, MAX_DAC_NUMBER // 2):
            for pin, state in zip(dac, dec2bin(i)):
                GPIO.output(pin, state)
            time.sleep(T / MAX_DAC_NUMBER)
        print("--- DONE! ---")
finally:
    [GPIO.output(pin, GPIO.LOW) for pin in dac]
    GPIO.cleanup()