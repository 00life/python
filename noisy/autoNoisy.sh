#!/bin/sh

# Variables
set -- $(mktemp) $(mktemp --suffix=".zip" ) $(mktemp config_xxxx);
curl -sL https://raw.githubusercontent.com/00life/python/refs/heads/master/noisy/noisy.py -o "$1";
curl -sL https://github.com/00life/python/raw/refs/heads/master/noisy/config.zip -o "${2}";
sudo unzip "${2}.zip" $3;


echo "\033[32m"

func_random(){
min=$1;
max=$(($2-$1+1));
x=`hexdump -n 2 -e '/2 "%u"' /dev/urandom`;
echo $(($x%$max+$min))
};

time_sleep1=$(func_random 1 2)m;
echo "[*] Sleeping for $time_sleep1 minutes"
sudo sleep $time_sleep1;

echo "[*] Running PyNoise"
#sudo python3 /home/pi/Automate/noisy/noisy.py --config /home/pi/Automate/noisy/config.json &
sudo python3 $1 --config $3 &

time_sleep2=$(func_random 60 120)m;
echo "[*] PyNoise Finishes in $time_sleep2 minutes";
sudo sleep $time_sleep2;

pid_python=$(ps -a|grep -i python|awk '{print $1}');
sudo kill -9 $pid_python;
set --;

echo "[*] Rebooting";

echo "\033[0m";

sudo init 6;
sudo reboot;
