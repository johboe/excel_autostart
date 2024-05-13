#!/bin/bash
sudo apt update
sudo apt install -y firefox-esr
sudo apt install -y python3-pip
pip3 install selenium

wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux-aarch64.tar.gz
sudo tar -xzvf geckodriver-v0.33.0-linux-aarch64.tar.gz -C /usr/local/bin
chmod +x /usr/local/bin/geckodriver

sudo cp firefox.desktop /etc/xdg/autostart/firefox.desktop