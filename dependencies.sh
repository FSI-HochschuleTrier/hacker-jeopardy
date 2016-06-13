#!/bin/bash

sudo apt-get install python-dev
sudo apt-get install python2.7
git clone https://github.com/FSI-HochschuleTrier/mplayer.py.git
cd mplayer.py
mv mplayer ../mplayer
git https://github.com/tylerwowen/RPIO.git
cd RPIO
sudo python setup.py install
cd ..
sudo rm -rf mplayer.py
sudo rm -rf RPIO
cp resources/swiss-911-ultra-compressed-bt.ttf ~/.fonts/