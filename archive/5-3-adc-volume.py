#!/usr/bin/python3
import RPi.GPIO as GPIO
from mylib import dec2bin
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

MAX_DAC_VOLTAGE = 3.3
MAX_DAC_NUMBER = 255

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT)

def adc():
    ''' Return a decimal number proportional to voltage on S pin on troyka '''
    L, R = 0, MAX_DAC_NUMBER
    while L < R:
        x = L + (R - L) // 2
        GPIO.output(dac, dec2bin(x))
        time.sleep(0.01)
        comp_res = GPIO.input(comp)
        # print(f'{L}, {R}, {x}, {comp_res}')
        if comp_res == 0:
            R = x
        else:
            L = x + 1

    return L

def led_num(num):
    state = [0, 0, 0, 0, 0, 0, 0, 0]

    if num == 0: return state

    for i in range(7, 7 - num - 1, -1):
        state[i] = 1
    return state

print('Starting...')
try:
    while True:
        dec_voltage = adc()
        GPIO.output(leds, led_num(8 * dec_voltage // 255))
        voltage = dec_voltage * MAX_DAC_VOLTAGE / MAX_DAC_NUMBER
        print(f'Voltage on sig should be {voltage:.2f}V, and its correspomding dec number from dac is {dec_voltage}')
       # input("Go again?")
finally:
    [GPIO.output(pin, GPIO.LOW) for pin in dac]
    GPIO.output(troyka, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup()