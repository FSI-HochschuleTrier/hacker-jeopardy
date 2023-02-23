#!/bin/bash

sudo apt install ffmpeg fbi

git clone https://github.com/tylerwowen/RPIO.git
cd RPIO
sudo python setup.py install
cd ..
sudo rm -rf RPIO
sudo cp resources/swiss-911-ultra-compressed-bt.ttf /usr/share/fonts
sudo cp splashscreen.service /etc/systemd/system/

sudo systemctl enable splashscreen.service
