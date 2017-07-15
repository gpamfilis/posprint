#!/usr/bin/env bash
cd /
echo "I AM ALIIIIIIIVE //n//n//n///n//n//n" > /dev/ttyAMA0
cd home/pi/git/posprint
git fetch --all
git reset --hard origin/master
sudo python posprint_v4.py
cd /
