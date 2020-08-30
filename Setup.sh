#!bin/bash/

cl=setterm

### START ###
if [ -a $cl ];
then 
cp alarm /bin
cp alarm.sh /bin
chmod 777 alarm.sh
chmod 777 alarm
else
sudo apt-get install util-linux
cp alarm /bin
cp alarm.sh /bin
chmod 777 alarm.sh
chmod 777 alarm
