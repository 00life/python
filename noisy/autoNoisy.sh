#!/bin/bash

PATH_NOISY=$(mktemp); 
curl -sL https://raw.githubusercontent.com/00life/python/refs/heads/master/noisy/noisy.py -o $PATH_NOISY;

PATH_ZIP=$(mktemp --suffix=".zip"); 
curl -sL https://github.com/00life/python/raw/refs/heads/master/noisy/config.zip -o $PATH_ZIP;

PATH_REQ=$(mktemp); 
curl -sL https://raw.githubusercontent.com/00life/python/refs/heads/master/noisy/requirements.txt -o $PATH_REQ

echo "[+] Installing python requirments.txt";

python3 -m pip install -r  $PATH_REQ --break-system-packages 2>&1 > /dev/null;

PATH_DIR=$(mktemp -d); 
sudo unzip -o $PATH_ZIP -d $PATH_DIR 2>&1 > /dev/null;

echo "[*] Sleeping for 1 minutes"
sudo sleep 1m;

echo "[+] Running PyNoise";
sudo python3 $PATH_NOISY --config "${PATH_DIR}/config.json" --timeout 3600 --log debug &

sudo sleep 3600;
echo "[+] Cleanup program..."

PID_PYTHON=$(ps -a|grep -i python|awk '{print $1}');
sudo kill -9 $PID_PYTHON;
sudo rm -rf /tmp/*;
unset PATH_NOISY PATH_ZIP PATH_DIR PATH_REQ PATH_CONFIG PID_PYTHON;

echo "[*] Rebooting";
#sudo init 6;
#sudo reboot;
#exit 0
