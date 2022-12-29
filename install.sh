#!bin/bash
clear
sleep 1
printf "\033[0;92mInstalling...\n"
sleep 2
printf "Get required packages: "
sleep 0.5
printf "\033[0;93mpython"
sleep 0.5
printf "\033[0;93m openjdk-17\033[0;0m\n"
apt update -y
apt upgrade -y
apt install python openjdk-17 -y
printf "\033[0;95mInstallation Complete"
sleep 2
clear
printf "\033[0;92mdo you want to start program? [y/n]: \033[0;0m"
read ask
if [ $ask = "y" ]
then
printf "\033[0;92mStarting...\n"
sleep 1
chmod +x *
python main.py
rm -rf install.sh README.md
else
chmod +x *
rm -rf install.sh README.md
printf "\n\033[0;91mTo run program type \033[0;96mpython main.py\033[0;0m\n"
fi