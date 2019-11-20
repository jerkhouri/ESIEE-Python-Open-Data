#/usr/bin/bash

sudo apt install python3 -y
sudo apt install python3-pip -y
pip3 install -r requirement.txt
python3 python/downloadfile.py
python3 python/histogen.py

