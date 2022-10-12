#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
from mylib import dec2bin
from mylib import adc
from matplotlib import pyplot

# ---- SETUP ----
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

MAX_DAC_VOLTAGE = 3.3
MAX_DAC_NUMBER = 255

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)

# ---- AUX FUNCTIONS ----
# def adc():
#     ''' Return a decimal number proportional to voltage os S pin on troyka '''
#     L, R = 0, MAX_DAC_NUMBER
#     while L < R:
#         x = L + (R - L) // 2
#         GPIO.output(dac, dec2bin(x))
#         time.sleep(0.005)
#         comp_res = GPIO.input(comp)
#         if comp_res == 0:
#             R = x
#         else:
#             L = x + 1
#     return L

# ---- MAIN ----
print('Starting...')
try:
    # m_data_str = [str(item) for item in measured data]
    with open('data.txt', 'w') as outfile:
        # outfile.write('\n'.join(measure_data_str))
        pass
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()
