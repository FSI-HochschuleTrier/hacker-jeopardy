#!/bin/bash

git clone https://github.com/FSI-HochschuleTrier/mplayer.py.git
cd mplayer.py
mv mplayer ../mplayer
cd ..
rm -rf mplayer.py
