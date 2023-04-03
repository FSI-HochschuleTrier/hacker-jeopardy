#!/bin/bash

echo "Installing system dependencies using 'apt'..."
sudo apt install -y ffmpeg fbi python3-gst-1.0 unclutter realvnc-vnc-server dialog

echo
echo "Installing python dependencies using 'pip'..."
pip install -r requirements.txt

sudo cp resources/swiss-911-ultra-compressed-bt.ttf /usr/share/fonts
sudo cp splashscreen.service /etc/systemd/system/
sudo cp resources/opener.png /etc/splash.png

sudo systemctl enable splashscreen.service

dialog --msgbox "Now please activate VNC under the 'Interfaces Options' menu point..." 10 30

sudo raspi-config

dialog --clear

echo "All depencies for Hacker Jeopardy should now be installed. Start the game using the start script: './start'"
