#!/usr/bin/python3
import os
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

clear()

slowprint("Starting the setup...")
clear()

slowprint("Welcome to PocketMine-MP Installation (64-bit) - Linux & Windows")
slowprint("PocketMine-Setup v1.0.2")
print(" ")
slowprint("-------------------------------------")
print(" ")
slowprint("Made by @mukeenanyafiq")
slowprint("Executed with Python")
slowprint("This installation will install the latest PocketMine-MP")
print(" ")
slowprint("NOTE: Sometimes packages cannot be installed automatically either because the package cannot be located or not enough storage. Prepare before continuing")
print(" ")
slowprint("-------------------------------------")
print(" ")
choice = input("Start with the installation? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : clear()

slowprint("You will install:")
slowprint("1. make")
slowprint("2. autoconf")
slowprint("3. automake")
slowprint("4. libtool")
slowprint("5. m4")
slowprint("6. wget")
slowprint("7. getconf")
slowprint("8. gzip")
slowprint("9. bzip2")
slowprint("10. bison")
slowprint("11. g+ or g++")
slowprint("12. cmake")
slowprint("13. pkg-config")
slowprint("14. re2c")
print(" ")

choice = input("Start the setup? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : clear()

slowprint("Starting setup...")
slowprint("Installing 14 packages...")
os.system ("sudo apt install make")
os.system ("sudo apt install autoconf")
os.system ("sudo apt install automake")
os.system ("sudo apt install libtool")
os.system ("sudo apt install m4")
os.system ("sudo apt install wget")
os.system ("sudo apt install getconf")
os.system ("sudo apt install gzip")
os.system ("sudo apt install bzip2")
os.system ("sudo apt install bison")
choice = input("Possibility of package g+ or g++ cannot be found, do you want to try installing it anyway? [y/n]: ")
if choice == 'n' : slowprint("1 package installation cancelled")
if choice == 'y' : os.system ("sudo apt install g++")
os.system ("sudo apt install cmake")
os.system ("sudo apt install pkg-config")
os.system ("sudo apt install re2c")
clear()

choice = input("All required packages are ready. Start with the PocketMine-MP setup? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : clear()
slowprint("Installing PocketMine-MP")
slowprint("Creating folder 'Server'")
os.system("mkdir Server")
os.system("cd Server")
slowprint("Getting all files from https://get.pmmp.io...")
os.system ("wget -q -O - https://get.pmmp.io | bash -s -")
slowprint("Successfully completed the setup. Type './start.sh' to start the server")
slowprint("You cannot start your server/setup with rooted user.")
slowprint("With Ubuntu on Windows, you might need to exit from root user to start the server.")
choice = input("Press any key to exit: ")
sys.exit()
