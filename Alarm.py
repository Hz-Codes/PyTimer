############################################
"""                                        #
                                           #
  __     _    _      [==< v1.14 >==]  __   #
 / /    / \  | | __ _ _ __ _ __ ___   \ \  #
/ /    / _ \ | |/ _` | '__| '_ ` _ \   \ \ #
\ \   / ___ \| | (_| | |  | | | | | |  / / #
 \_\ /_/   \_\_|\__,_|_|  |_| |_| |_| /_/  #
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
Author : Hz-Code                           #
FileType : Python  (.py)                   #
Requirements : - Linux (based on Debian)   #
               - MPG123                    #
               - python3                   #
                                           #
                           [127.0.0.1]     #
                          [192.168.1.1]    #
Copyright(c) 2020 Hz-Code                  #
                                           #
"""                                        #
############################################
'''
Thanks To :

* MPG123
* Hz-Code
* Kali.org
* Python.org
* Github.com
* Parrotsec.org

Developed Using :

* Mousepad (Kali Linux Code Editor)
* Notepad++
* Atom
* VSCode
* Python3

Notes :
- This script is using MPG123 to play the Audio
- If You found bugs in this program please report to https://github.com/Hz-Codes/Alarm/Issues
'''

import os
import platform
import sys
if sys.version_info<(3,0,0):
	print("Please run with Python 3 ! ")
	exit()
else :
	clear = os.system("clear")
#############################################################################################
# Starting for Alarm script #
#############################

### importing module ###
import os
import sys
import time
### Colors ###
Green="\033[1;32m"
Yellow="\033[1;33m"
Cyan="\033[0;36m"
DarkBlue="\033[0;34m"
Magenta="\033[0;35m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[1;37m"
Reset2="\033[0m"
Red="\033[1;31m"
##############
scs = "s"
mns = "m"
hrs = "h"
dys = "d"

def clear():
	os.system('clear')
##########################

def intro():
	os.system('clear')
	print("if you don't understand, enter the 'Help' command ")
	time.sleep(1)
	print("")
	next = input("Press Enter To Continue...")
	os.system('clear')
	start()



def ffx():
    os.chdir(os.path.dirname(__file__))
    os.system('./mgp123 DefaultAlarm.mp3')

def help():
	clear()
	print(Blue + "[==< Help >==]" + Green)
	print("Type Seconds for Second(s) alarm")
	print("Type Minutes for minute(s) alarm")
	print("Type Hours for Hour(s) alarm")
	print("Type Days for Day(s) alarm ")
	print("Type Exit for Exit from this script")
	print("")
	print("(if you didn't shut down your computer, this script will work) ")
	print("")
	time.sleep(5)
	next = input("Press Enter To Continue...")
	start()

def seconds():
	print("")
	hows = input("How long (Seconds) : ")
	print("")
	print(Yellow + "Alarm set for : " + hows + " Seconds")
	print("Press [CTRL + Z] To Exit" + Reset)
	os.system('sleep ' + hows + scs)
	ffx()

def minutes():
	print("")
	howm = input("How long (Minutes) : ")
	print("")
	print(Yellow + "Alarm set for : " + howm + " Minutes")
	print("Press [CTRL + Z] To Exit" + Reset)
	os.system('sleep ' + howm + mns)
	ffx()

def hours():
	print("")
	howh = input("How long (Hours) : ")
	print("")
	print(Yellow + "Alarm set for : " + howh + " Hours")
	print("Press [CTRL + Z] To Exit" + Reset)
	os.system('sleep ' + howh + hrs)
	ffx()


def days():
	print("")
	howd = input("How long (Days) : ")
	print("")
	print(Yellow + "Alarm set for : " + howd + " Days")
	print("Press [CTRL + Z] To Exit" + Reset)
	os.system('sleep ' + howd + dys)
	ffx()

def Exit():
	print("")
	print("Thanks for use this Alarm script")
	print("Don't be late !")
	print("")
	exit()


def start():
	clear()
	print(Yellow + "  __     _    _    [ ==< v1.14 >== ]  __  ")
	print(Grey + " / /    / \  | | __ _ _ __ _ __ ___   \ \ ")
	print(Yellow + "/ /    / _ \ | |/ _` | '__| '_ ` _ \   \ \ ")
	print(Grey + "\ \   / ___ \| | (_| | |  | | | | | |  / / ")
	print(Yellow + " \_\ /_/   \_\_|\__,_|_|  |_| |_| |_| /_/ ")
	print(Reset + "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print("")
	tts = input("Insert Option = ")
	if tts == "Help" :
		help()
	elif tts == "help" :
		help()
	elif tts == "Seconds" :
		seconds()
	elif tts == "Second" :
		seconds()
	elif tts == "seconds" :
		seconds()
	elif tts == "second" :
		seconds()
	elif tts == "Minutes" :
		minutes()
	elif tts == "Minute" :
		minutes()
	elif tts == "minutes" :
		minutes()
	elif tts == "minute" :
		minutes()
	elif tts == "Hours" :
		hours()
	elif tts == "Hour" :
		hours()
	elif tts == "hours" :
		hours()
	elif tts == "hour" :
		hours()
	elif tts == "Days" :
		days()
	elif tts == "Day" :
		days()
	elif tts == "days" :
		days()
	elif tts == "day" :
		days()
	elif tts == "Exit" :
		Exit()
	elif tts == "exit" :
		Exit()
	else:
		start()

##### START #####

intro()
start()
