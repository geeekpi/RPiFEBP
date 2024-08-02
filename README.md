# RPiFEBP
## Revision
* 2021-09-26:V1.0
## Software update date 
* 2024-08-02:V1.0 
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
 - SSD1306 library for OLED - recommended using "luma.oled" library  
 - SMBUS library for I2C device control
 - wiringPi library for LED indicators control(Deprecated)
 - RPi.GPIO library for LED indicators control(Recommended) 
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

### LED indicators Pin out
There are 4 LED under the PCB board.
 - LED1 - nearby the GPIO pins and fan on left corner, connect to `GPIO 24` (BCM 19)
 - LED2 - under LED1, connect to `GPIO 23` (BCM 13)
 - LED3 - on the right of LED2, connect to `GPIO 22` (BCM 6) 
 - LED4 - on the top of LED3, connect to `GPIO 21` (BCM 5) 

### Installation 
* Please refer to: [52Pi wiki](https://wiki.52pi.com/index.php?title=EP-0152)

### Install by copy paste
* Enable I2C 
* Install dependencies libraries. 

```bash
sudo apt update 
sudo apt upgrade -y
sudo apt -y install python3 python3-dev python3-pip python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 
sudo pip install --upgrade luma.oled --break-system-packages
sudo usermod -a -G gpio,i2c pi  
git clone https://github.com/rm-hull/luma.examples.git 
cd luma.examples/
sudo -H pip install -e . --break-system-packages
sudo -H pip installl psutil --break-system-packages 
```
* clone the repository: 
```bash
cd ~
git clone https://github.com/geeekpi/RPiFEBP.git
cd RPiFEBP/
sudo cp -Rvf systemd_files/*.service /etc/systemd/system/ 
sudo systemctl daemon-reload
sudo systemctl enable  52piFan.service
sudo systemctl enable  lights.service
sudo systemctl enable  oled.service
sudo systemctl start 52piFan.service
sudo systemctl start lights.service
sudo systemctl start oled.service
```
* That's it,have fun! 
