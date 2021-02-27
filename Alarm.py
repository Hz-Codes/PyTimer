############################################
"""                                        #
                                           #
  __     _    _      [==< v1.14 >==]  __   #
 / /    / \  | | __ _ _ __ _ __ ___   \ \  #
/ /    / _ \ | |/ _` | '__| '_ ` _ \   \ \ #
\ \   / ___ \| | (_| | |  | | | | | |  / / #
 \_\ /_/   \_\_|\__,_|_|  |_| |_| |_| /_/  #
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
Author : Hamz-Code (Region : NYC)          #
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

Developed Using :

* Mousepad (Kali Linux Code Editor)
* Notepad++
* Python3



'''
##############################################################################################
# This is copied from playsound module "/usr/local/lib/python3.8/dist-packages/playsound.py" #
############################################################################################################################
class PlaysoundException(Exception):
    pass

def _playsoundWin(sound, block = True):
    '''
    Utilizes windll.winmm. Tested and known to work with MP3 and WAVE on
    Windows 7 with Python 2.7. Probably works with more file formats.
    Probably works on Windows XP thru Windows 10. Probably works with all
    versions of Python.

    Inspired by (but not copied from) Michael Gundlach <gundlach@gmail.com>'s mp3play:
    https://github.com/michaelgundlach/mp3play

    I never would have tried using windll.winmm without seeing his code.
    '''
    from ctypes import c_buffer, windll
    from random import random
    from time   import sleep
    from sys    import getfilesystemencoding

    def winCommand(*command):
        buf = c_buffer(255)
        command = ' '.join(command).encode(getfilesystemencoding())
        errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))
        if errorCode:
            errorBuffer = c_buffer(255)
            windll.winmm.mciGetErrorStringA(errorCode, errorBuffer, 254)
            exceptionMessage = ('\n    Error ' + str(errorCode) + ' for command:'
                                '\n        ' + command.decode() +
                                '\n    ' + errorBuffer.value.decode())
            raise PlaysoundException(exceptionMessage)
        return buf.value

    alias = 'playsound_' + str(random())
    winCommand('open "' + sound + '" alias', alias)
    winCommand('set', alias, 'time format milliseconds')
    durationInMS = winCommand('status', alias, 'length')
    winCommand('play', alias, 'from 0 to', durationInMS.decode())

    if block:
        sleep(float(durationInMS) / 1000.0)

def _playsoundOSX(sound, block = True):
    '''
    Utilizes AppKit.NSSound. Tested and known to work with MP3 and WAVE on
    OS X 10.11 with Python 2.7. Probably works with anything QuickTime supports.
    Probably works on OS X 10.5 and newer. Probably works with all versions of
    Python.

    Inspired by (but not copied from) Aaron's Stack Overflow answer here:
    http://stackoverflow.com/a/34568298/901641

    I never would have tried using AppKit.NSSound without seeing his code.
    '''
    from AppKit     import NSSound
    from Foundation import NSURL
    from time       import sleep

    if '://' not in sound:
        if not sound.startswith('/'):
            from os import getcwd
            sound = getcwd() + '/' + sound
        sound = 'file://' + sound
    url   = NSURL.URLWithString_(sound)
    nssound = NSSound.alloc().initWithContentsOfURL_byReference_(url, True)
    if not nssound:
        raise IOError('Unable to load sound named: ' + sound)
    nssound.play()

    if block:
        sleep(nssound.duration())

def _playsoundNix(sound, block=True):
    """Play a sound using GStreamer.

    Inspired by this:
    https://gstreamer.freedesktop.org/documentation/tutorials/playback/playbin-usage.html
    """
    if not block:
        raise NotImplementedError(
            "block=False cannot be used on this platform yet")

    # pathname2url escapes non-URL-safe characters
    import os
    try:
        from urllib.request import pathname2url
    except ImportError:
        # python 2
        from urllib import pathname2url

    import gi
    gi.require_version('Gst', '1.0')
    from gi.repository import Gst

    Gst.init(None)

    playbin = Gst.ElementFactory.make('playbin', 'playbin')
    if sound.startswith(('http://', 'https://')):
        playbin.props.uri = sound
    else:
        playbin.props.uri = 'file://' + pathname2url(os.path.abspath(sound))

    set_result = playbin.set_state(Gst.State.PLAYING)
    if set_result != Gst.StateChangeReturn.ASYNC:
        raise PlaysoundException(
            "playbin.set_state returned " + repr(set_result))

    # FIXME: use some other bus method than poll() with block=False
    # https://lazka.github.io/pgi-docs/#Gst-1.0/classes/Bus.html
    bus = playbin.get_bus()
    bus.poll(Gst.MessageType.EOS, Gst.CLOCK_TIME_NONE)
    playbin.set_state(Gst.State.NULL)


from platform import system
system = system()

if system == 'Windows':
    playsound = _playsoundWin
elif system == 'Darwin':
    playsound = _playsoundOSX
else:
    playsound = _playsoundNix

del system

###########################
# End of playsound module #
#############################################################################################################################
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
	print("if you don't understand, insert 'Help' command ")
	time.sleep(1)
	print("")
	next = input("Press Enter To Continue...")
	os.system('clear')
	start()



def ffx():
		playsound('/mnt/c/Users/WilZamComp/Music/Favourite/ Payphone - Maroon 5.mp3')
		playsound('/mnt/c/Users/WilZamComp/Music/Favourite/ Payphone - Maroon 5.mp3')
		playsound('/mnt/c/Users/WilZamComp/Music/Favourite/ Payphone - Maroon 5.mp3')


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
	hows = input("How much (Seconds) : ")
	print("")
	print(Yellow + "Alarm set for : " + hows + " Seconds")
	print("Press [CTRL + Z] To Exit" + Reset)
	os.system('sleep ' + hows + scs)
	ffx()
	
def minutes():
	print("")
	howm = input("How much (Minutes) : ")
	print("")
	print(Yellow + "Alarm set for : " + howm + " Minutes")
	print("Press [CTRL + Z] To Exit" + Reset)
	os.system('sleep ' + howm + mns)
	ffx()
	
def hours():
	print("")
	howh = input("How much (Hours) : ")
	print("")
	print(Yellow + "Alarm set for : " + howh + " Hours")
	print("Press [CTRL + Z] To Exit" + Reset)
	os.system('sleep ' + howh + hrs)
	ffx()
	
	
def days():
	print("")
	howd = input("How much (Days) : ")
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
