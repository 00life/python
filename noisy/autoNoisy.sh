#!/bin/sh

#\ Variables

path_noisy=$(mktemp);
path_zip=$(mktemp --suffix=".zip");
path_dir=$(mktemp -d);
path_req=$(mktemp);

curl -sL https://raw.githubusercontent.com/00life/python/refs/heads/master/noisy/noisy.py -o $path_noisy;
curl -sL https://github.com/00life/python/raw/refs/heads/master/noisy/config.zip -o $path_zip;
curl -sL https://raw.githubusercontent.com/00life/python/refs/heads/master/noisy/requirements.txt -o $path_req

echo "[+] Installing python requirments.txt";

python3 -m pip install -r  $path_req --break-system-packages 2>&1 > /dev/null;
sudo unzip -o $path_zip -d $path_dir 2>&1 > /dev/null;
path_config=$(echo "${path_dir}/config.json");

#/ Function that generates a random number

func_random_number(){
  local min=$1;
  local max=$(($2-$1+1));
  local x=`hexdump -n 2 -e '/2 "%u"' /dev/urandom`;
  echo $(($x%$max+$min));
};

time_sleep1=$(func_random_number 1 2)m;
echo "[*] Sleeping for $time_sleep1 minutes"
sudo sleep $time_sleep1;

echo "[+] Running PyNoise";
sudo python3 $path_noisy --config $path_config &

time_sleep2=$(func_random_number 60 120)m;
echo "[*] PyNoise Finishes in $time_sleep2 minutes";
sudo sleep $time_sleep2;

echo "[+] Cleanup program..."
pid_python=$(ps -a|grep -i python|awk '{print $1}');
echo "1";
sudo kill -9 $pid_python;
echo "2";
sudo rm -rf /tmp/*;
echo "3";
unset path_noisy path_zip path_dir path_req path_config pid_python;

echo "[*] Rebooting";
#sudo init 6;
#sudo reboot;
#exit 0
