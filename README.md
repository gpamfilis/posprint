The Journey Begins...


Setting up Raspberry Pi B+


sudo apt-get update
sudo apt-get upgrade

### extend the filesystem
sudo raspi-config


### setup the cmdline

/boot/cmdline.txt 

dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 rootwait


### setup the config

sudo nano /boot/printer_config.txt

contents....

### shutdown

sudo shutdown -h now

### simething

sudo usermod -a -G dialout pi


### shutdown

sudo shutdown -h now

### packages needed

sudo apt-get install python-serial
sudo apt-get install python-imageing-tk
sudo apt-get install git-core

### optional (baud rate)

stty -F /dev/ttyAMA0 19200  

### clone the repository

.....

### crontab (add this line at the bottom)

@reboot sh /home/pi/git/posprint/launcher.sh >/home/pi/logs/cronlog 2>&1









