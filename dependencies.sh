#!/bin/bash

git clone https://github.com/FSI-HochschuleTrier/mplayer.py.git
cd mplayer.py
mv mplayer ../mplayer
git clone https://github.com/metachris/RPIO.git
cd RPIO
sudo python setup.py install
cd ..
rm -rf mplayer.py
rm -rf RPIO
cp resources/swiss-911-ultra-compressed-bt.ttf ~/.fonts/
