#!/bin/bash 
# installation script 
# author: yoyojacky
# email: jacky.li@52pi.com
#

# init functions
if [ -e /lib/lsb/init-functions ]; then
	. /lib/lsb/init-functions 
	log_action_msg "Initializing functions..........[OK]"
fi 

# copy systemd files to /etc/systemd/system/ location 
#
sudo sh -c "cp ./systemd_files/*.service /etc/systemd/system/" && log_success_msg "Copy systemd files..............[OK]" || log_warning_msg "Copy systemd files [failed]"  

if [[ $? -eq 0 ]]; then
	sudo systemctl daemon-reload
	sudo systemctl enable 52piFan.service 
	sudo systemctl enable lights.service 
	sudo systemctl enable oled.service 
	sudo systemctl start 52piFan.service 
	sudo systemctl start lights.service 
	sudo systemctl start oled.service 
fi

log_success_msg "Installation finished...........[OK]"

