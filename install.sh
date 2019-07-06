python3.7 -V | grep "3.7" &>/dev/null
if [ "$?" -eq "0" ]; then
	python3.7 -m pip install -r requirements.txt
	sudo cp clipcode.py /opt/clipcode
	chmod 755 /opt/clipcode
	sudo cp clipcode.desktop ~/.config/autostart/clipcode.desktop
	/opt/clipcode &
	echo "Clipcode Installed! Clipcode will start from the next reboot"
else
	echo "Clipcode requries python 3.7"
fi
