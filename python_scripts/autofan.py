#!/usr/bin/python3 

import RPi.GPIO as GPIO
import time 
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

pwm = GPIO.PWM(14, 100) 

# print("\nPress Ctrl+C to quit \n") 

dc = 0

pwm.start(dc) 

try:
    while True:
        temp = subprocess.getoutput("vcgencmd measure_temp|sed 's/[^0-9.]//g'")
        if round(float(temp)) >= 45:
            dc = 100
            pwm.ChangeDutyCycle(dc)
            # print("CPU Temp:", float(temp), "Fan duty cycle:", dc)
            time.sleep(180)

        if round(float(temp)) >= 40:
            dc = 85
            pwm.ChangeDutyCycle(dc)
            # print("CPU Temp:", float(temp), "Fan duty cycle:", dc)
            time.sleep(120)
        else:
            dc = 70
            pwm.ChangeDutyCycle(dc)
            # print("CPU Temp:", float(temp), "Fan duty cycle:", dc)
            time.sleep(60)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    # print("Ctrl+C pressed -- Ending program") 

