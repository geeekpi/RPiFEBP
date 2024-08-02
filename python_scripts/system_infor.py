#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import subprocess
from demo_opts import get_device
from luma.core.render import canvas


def system_infor(device, draw):
    # First define some constants to allow easy resizing of shapes
    # Move left to right keeping track of the current x position for drawing shapes
    x = 2
    
    # grap temperature of CPU 
    temp =subprocess.getoutput("vcgencmd measure_temp | sed 's/[^0-9.*]//g'")
    # grap capacity of disk usage of /
    disk_usage = subprocess.getoutput("df -Th / | awk '{print $6}' | tail -n1") 
    # grap memory infor 
    free_mem = subprocess.getoutput("free -g |grep Mem | awk '{print $4}'")
    # Network Status
    IP = subprocess.getoutput("hostname -I | awk '{print $1}'")
    draw.rectangle((x, 0, 128, 32), fill="black")
    # draw.text((device.width - padding - w, top + 4), temp, fill="cyan")
    # draw.text((device.width - padding - w, top + 16), 'haha', fill="purple")
    draw.text((x, 0),'CPU TEMP:', fill="white")
    draw.text((56, 0), temp, fill="white")
    draw.text((82, 0), '°C', fill="white")
    draw.text((x, 8),'IP ADDR:', fill="white")
    draw.text((52, 8), IP, fill="white")
    draw.text((x, 16),'SD USAGE:', fill="white")
    draw.text((58, 16), disk_usage, fill="white")
    draw.text((78, 16), 'MEM:', fill="white")
    draw.text((100, 16), free_mem, fill="white")
    draw.text((104, 16), ' GB', fill="white")

    # Draw a rectangle of the same size of screen
    draw.rectangle(device.bounding_box, outline="white")


device = get_device() 

while True:
    with canvas(device) as draw:
        system_infor(device, draw)
        time.sleep(5)

