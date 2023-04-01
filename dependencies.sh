#!/bin/bash

sudo apt install ffmpeg fbi python3-gst-1.0 unclutter

git clone https://github.com/tylerwowen/RPIO.git
cd RPIO
sudo python setup.py install
cd ..
sudo rm -rf RPIO
sudo cp resources/swiss-911-ultra-compressed-bt.ttf /usr/share/fonts
sudo cp splashscreen.service /etc/systemd/system/
sudo cp resources/opener.png /etc/splash.png

sudo systemctl enable splashscreen.service
