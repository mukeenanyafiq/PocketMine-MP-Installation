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

slowprint("Starting the setup...")
os.system ("clear")

slowprint("Welcome to PocketMine-MP Installation (64-bit)")
slowprint("-------------------------------------")
slowprint("Created by Keenan Yafiq (keenanyafiqy)")
slowprint("Executed from Python")
slowprint("This installation will install PocketMine-MP v3.25.2")
slowprint("Sometimes packages cannot be downloaded automatically because the packages cannot be located or they're storage is full, so you may needed fast internet connection and many storages")
choice = input("Do you want to start the installation? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")

os.system ("pkg install make")
os.system ("pkg install autoconf")
os.system ("pkg install automake")
os.system ("pkg install libtool")
os.system ("pkg install m4")
os.system ("pkg install wget")
os.system ("pkg install getconf")
os.system ("pkg install gzip")
os.system ("pkg install bzip2")
os.system ("pkg install bison")
os.system ("pkg install g++")
os.system ("pkg install git")
os.system ("pkg install cmake")
os.system ("pkg install pkg-config")
os.system ("pkg install re2c")

choice = input("Some packages has been installed, some packages cannot be installed, do you want to install source PocketMine-MP? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("clear")

slowprint("Starting the downloads....")
slowprint("Getting all files from https://get.pmmp.io...")
os.system ("wget -q -O - https://get.pmmp.io | bash -s -")
slowprint("Successfully completed the setup. Type './start.sh' to start the server")
slowprint("If you want to recompile the PHP, Type './compile.sh' to recompile the PHP")
slowprint("Make sure your devices to 64-bit if you are so sure to install this software. Many peoples cannot install PocketMine-MP because they only have 32-bit systems")
slowprint("Quitting the setup...")
sys.exit()
