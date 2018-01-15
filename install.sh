#!/bin/bash

echo 'Updating...'
sudo apt-get update -y
cd ~/
echo

echo 'Starting Hologram installation...'
cd ~/
git clone https://github.com/hologram-io/hologram-python.git
cd ~/hologram-python
sudo pip install -r requirements.txt
echo 'Installing Hologram now...'
sudo python3 setup.py install 
cd ~/
curl -L hologram.io/python-install | bash
echo 'DONE installing Hologram!'
echo

echo 'DONE!'
