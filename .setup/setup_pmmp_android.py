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
    if os.name == 'posix':
        _ = os.system("clear")

clear()

slowprint("Starting the setup...")
clear()

slowprint("Welcome to PocketMine-MP Installation (64-bit) - Android")
slowprint("PocketMine-Setup v1.0.1")
print(" ")
slowprint("-------------------------------------")
print(" ")
slowprint("Created by Keenan Yafiq (keenanyafiqy)")
slowprint("Executed from Python")
slowprint("This installation will install the Latest PocketMine-MP")
print(" ")
slowprint("Make sure you have enough space to Install the Latest PocketMine-MP")
print(" ")
slowprint("-------------------------------------")
print(" ")
choice = input("Do you want to Start the Installation? [y/n]: ")
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
slowprint("11. git")
slowprint("12. cmake")
slowprint("13. pkg-config")
slowprint("14. re2c")
print(" ")

choice = input("Start the Setup? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : clear()

slowprint("Starting setup...")
slowprint("Installing 15 packages...")
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
os.system ("pkg install git")
os.system ("pkg install cmake")
os.system ("pkg install pkg-config")
os.system ("pkg install re2c")
clear()

choice = input("All required packages are ready. Do you want to download PocketMine-MP? [y/n]: ")
if choice == 'n' : sys.exit()
if choice == 'y' : clear()

slowprint("Installing PocketMine-MP....")
slowprint("Creating folder 'Server'...")
os.system("mkdir Server")
slowprint("Succesfully created folder 'Server'")
os.system("cd Server")
slowprint("Downloading PocketMine-MP from https://get.pmmp.io...")
os.system ("wget -q -O - https://get.pmmp.io | bash -s -")
slowprint("Setup completed. Type './start.sh' to start the server")
slowprint("Your server setup cannot start with rooted user.")
choice = input("Press Y to exit. ")
if choice == 'y' : sys.exit()
sys.exit()
