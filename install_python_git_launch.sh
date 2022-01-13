pkg install python
pkg install python2
pkg install git
pkg install getconf

if [ `getconf LONG_BIT` == "32" ]; then
	echo "This setup is needed 32-bit operating system!"
        exit 1
fi

clear

echo Done! Launching the setup wizard now

wget -q -o - https://raw.githubusercontent.com/keenanyafiqy/PocketMine-MP-Installation/Setup/install_pmmp.py | bash -s -

rm install_pmmp.py

exit
