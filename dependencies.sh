#!/bin/bash

sudo apt-get install python-dev
sudo apt-get install python2.7
if [ ! -d "mplayer" ]
	then
	git clone https://github.com/FSI-HochschuleTrier/mplayer.py.git
	cd mplayer.py
	mv mplayer ../mplayer
	cd ..
	sudo rm -rf mplayer.py
fi

git clone https://github.com/tylerwowen/RPIO.git
cd RPIO
sudo python setup.py install
cd ..
sudo rm -rf RPIO
sudo cp resources/swiss-911-ultra-compressed-bt.ttf /usr/share/fonts
