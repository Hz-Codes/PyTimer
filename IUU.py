############################################
"""                                        #
                                           #
  __     _    _      [==< v1.14 >==]  __   #
 / /    / \  | | __ _ _ __ _ __ ___   \ \  #
/ /    / _ \ | |/ _` | '__| '_ ` _ \   \ \ #
\ \   / ___ \| | (_| | |  | | | | | |  / / #
 \_\ /_/   \_\_|\__,_|_|  |_| |_| |_| /_/  #
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
Author : Hamz-Code                         #
FileType : Python  (.py)                   #
Requirements : - Linux or MacOS            #
               - playsound module          #
               - python3                   #
                                           #
                           [127.0.0.1]     #
                          [192.168.1.1]    #
Copyright(c) 2020 Hamz-Code                #
                                           #
"""                                        #
############################################
'''
Thanks To :

* Michael Gundlach
* Hamz-Code
* Kali.org
* Python.org
* Github.com

Developed Using :

* Mousepad (Kali Linux Code Editor)
* Notepad++
* Python3



'''

import os
import sys
import time
import shutil
import platform
import subprocess


def Install():
    print("Checking Python 3...")
    time.sleep(0.5)
    if os.path.isfile("/bin/python3") == True:
        print("[+] Python Available")
        print(" ")
        pass
    else:
        print("[-] Python ")
        os.system("sudo apt install python3")
    print("Checking Pip...")
    time.sleep(0.5)
    if os.path.isfile("/bin/pip") == True:
        print("[+] Pip Avilable !")
        print(" ")
        pass
    else:
        os.system("sudo apt install python-pip")
    time.sleep(1)
    print("Select the audio player :")
    print("[1] Mpg123")
    print("[2] Playsound")
    APIns = input("[Choose] >>> ")
    if APIns == "1":
        print("[!] Installing Mpeg123")
        os.system("sudo apt-get install mpg123")
    elif APIns == "2":
        print("[!] Installing Playsound")
        os.system("pip install playsound")
    else:
        print("Installation Failed :(")
        exit()
    print(" ")
    print("Installation Succeed")

def Update():
    os.system("git pull")
        
def Uninstall():
    print("Uninstalling...")
    time.sleep(0.5)
    ThisFolderLocation = os.path.dirname(__file__)
    shutil.rmtree(ThisFolderLocation)
    print("Uninstall Succeed")


print("+===================+")
print(" ___   _   _   _   _ ")
print("|_ _| | | | | | | | |")
print(" | |  | | | | | | | |")
print(" | |  | |_| | | |_| |")
print("|___|  \___/   \___/ ")
print("+===================+")
print("| [1] Install ")
print("| [2] Update")
print("| [3] Uninstall")
print("+===================")
UsC = input("[Choose] >>> ")
if UsC == "1":
    Install()
elif UsC == "2":
    Update()
elif UsC == "3":
    Uninstall()
else:
    pass