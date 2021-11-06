#!/usr/bin/python3
import os
import time
import sys

print("Welcome to PocketMine-MP Installation")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

slowprint("Created by Keenan Yafiq (keenanyafiqy)")
choice = input("Do you want to start the installation? [y/n]")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")