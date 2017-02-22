sudo mount /dev/sda1 /mnt/usb
sudo mv /mnt/usb/text.png ~/git/py-thermal-printer/
sudo umount /mnt/sda1

cd ~/git/py-thermal-printer/
./printer.py


