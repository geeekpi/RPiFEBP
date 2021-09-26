# RPiFEBP
## Revision
* 2021-09-26:V1.0
## Descriptions
RPiFEBP stands for Raspberry Pi Fan Expansion Board Plus.
It is a fan expansion board with 0.91 OLED Display and 4007 PWM Fan onboard, 4 programable LED indicators under the PCB board.
## Features
* 0.91 inch OLED Display(support I2C protocol) 
* Speed Adjustable Fan (PWM FAN)
* Programable LED Indicator 
* Raspberry Pi Hat Style
## How to Assemble.
* Just insert it into Raspberry Pi 40Pin Header.
## How to Setup Fan 
* Recommend OS: Raspberry Pi OS (Buster) or later.
* Requirements:
 - SSD1306 library for OLED 
 - SMBUS library for I2C device control
 - wiringPi library for LED indicators control
* Open a terminal and typing:
```
sudo raspi-config
```
Navigate to `4 Performance Options` -> `Fan` -> `YES` -> `14`(to which GPIO is the fan connected) -> `60` (Temprature trigger) -> `yes` -> `reboot` 
* Or you can write C code or python script to generate `PWM` wave and send it to `GPIO 14`(BCM14) to control the Fan speed as your will. 
## How to Setup OLED Display
* Enable I2C interface 
```
sudo raspi-config`
```
Navigate to `Interface Options` -> `I2C` -> `Enable` -> `YES`.
* Detect If OLED has been recognized.
```
i2cdetect -y 1
```
It will shows an address: `0x3c`
* Download SSD1306 library:

```
sudo python -m pip install --upgrade pip setuptools wheel
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python setup.py install
pip install Adafruit-BBIO
```
* Download Demo Code:
``` 
git clone https://github.com/geeekpi/RPiFEBP.git
cd RPiFEBP/
python oled.py & 
```
## How to Setup LED indicator
* Reinstall wiringPi library.
```
sudo apt -y purge wiringpi
hash -r 
cd /tmp
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio readall

```
* LED indicators Pin out
There are 4 LED under the PCB board.
 - LED1 - nearby the GPIO pins and fan on left corner, connect to `GPIO 24` (BCM 19)
 - LED2 - under LED1, connect to `GPIO 23` (BCM 13)
 - LED3 - on the right of LED2, connect to `GPIO 22` (BCM 6) 
 - LED4 - on the top of LED3, connect to `GPIO 21` (BCM 5) 
* Demo code in shell:
```
for i in `seq 21 24`
 do 
    gpio mode $i out
 done 

while true
do 
  for i in `seq 21 24`
  do
	gpio write $i 1 
  	sleep 0.01
  	gpio write $i 0
  done
done

```
* Demo code in Python:
```
import RPi.GPIO as GPIO
import time 


# BCM Number of LED indicators
leds = [5, 6, 13, 19]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in range(len(leds)):
    GPIO.setup(leds[i], GPIO.OUT)



try:
    while True:
	for led in leds:
       	    GPIO.output(led, GPIO.HIGH)
	    time.sleep(0.01)
            GPIO.output(led, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("BYE")
```
