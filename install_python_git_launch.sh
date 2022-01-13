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

wget -q -0 https://bit.ly/34O4PaT | bash -s -

exit
