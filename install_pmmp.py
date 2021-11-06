#!/usr/bin/python3
import os
import time
import sys

os.system ("clear")
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

slowprint("Welcome to PocketMine-MP Installation (64 bit)")
slowprint("-------------------------------------")
slowprint("Created by Keenan Yafiq (keenanyafiqy)")
slowprint("Executed from Python")
slowprint("This installation will install PocketMine-MP v3.25.2")
choice = input("Do you want to start the installation? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")
