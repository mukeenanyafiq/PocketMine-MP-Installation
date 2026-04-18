#!/usr/bin/python3
import os
import platform
import time
import sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

def clear():

    if os.name == 'nt':
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def architectureresult():

    if platform.architecture()[0] == '64bit':
        _ = slowprint("Your system is compatible for the Setup. You will continue the Setup automatically")
    else:
        _ = slowprint("Your system is not compatible for the Setup. You will be exited automatically")
        _ = sys.exit()

def checkostocontinue():

    if platform.system() == 'Windows':
        _ = os.system("python .setup/setup_pmmp_linux-windows.py")
    else:
        _ = os.system("python .setup/setup_pmmp_android.py")

clear()

slowprint("Getting information about the OS (Operating System) before start the setup...")
print(" ")
slowprint("System OS Name:")
print(platform.system())
slowprint("OS Name:")
print(os.name)
slowprint("Architecture:")
print(platform.architecture())
slowprint("Compatible:")
print(platform.architecture()[0] == "64bit")
print(" ")
architectureresult()
checkostocontinue()
