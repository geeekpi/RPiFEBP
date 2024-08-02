import RPi.GPIO as GPIO
import time


LED1 = 19 # BCM naming system
LED2 = 13
LED3 = 6
LED4 = 5
interval = 0.2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

while True:
    for i in range(10):
        GPIO.output(LED1, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(LED2, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(LED3, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(LED4, GPIO.HIGH)
        time.sleep(interval)

    time.sleep(1)

    for i in range(10):
        GPIO.output(LED1, GPIO.LOW)
        time.sleep(interval)
        GPIO.output(LED2, GPIO.LOW)
        time.sleep(interval)
        GPIO.output(LED3, GPIO.LOW)
        time.sleep(interval)
        GPIO.output(LED4, GPIO.LOW)
        time.sleep(interval)

GPIO.cleanup()


