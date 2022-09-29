#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
from small_lib import dec2bin

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

MAX_DAC_VOLTAGE = 3.3
MAX_DAC_NUMBER = 255

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    ''' Return a decimal number proportional to voltage on S pin on troyka '''
    for num in range(256):
        # for dac_pin, state in zip(dac, dec2bin(num)):
        #     GPIO.output(dac_pin, state)
        GPIO.output(dac, dec2bin(num))
        time.sleep(0.01)
        comp_res = GPIO.input(comp)
        if comp_res == 0:
            return num

print('Starting...')
try:
    while True:
        dec_voltage = adc()
        voltage = dec_voltage * MAX_DAC_VOLTAGE / MAX_DAC_NUMBER
        print(f'Voltage on sig should be {voltage:.2f}V, and its correspomding dec number from dac is {dec_voltage}')
        input("Go again?")
finally:
    [GPIO.output(pin, GPIO.LOW) for pin in dac]
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()