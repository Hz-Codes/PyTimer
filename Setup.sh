#!bin/bash/

cl=setterm

### START ###
clear
echo "Setup Started
"
sleep 1
if [ -f $cl ];
then 
echo "Processing...
"
sleep 1
cp alarm /bin
cp alarm.sh /bin
chmod 777 /bin/alarm.sh
chmod 777 /bin/alarm
echo "
                 Completed ! 
You Can Start By Typing 'alarm' On Your Terminal "
else
echo "Processing..."
echo "Installing util-linux
"
sudo apt-get install util-linux
cp alarm /bin
cp alarm.sh /bin
chmod 777 /bin/alarm.sh
chmod 777 /bin/alarm
echo "
                 Completed ! 
You Can Start By Typing 'alarm' On Your Terminal "
fi
