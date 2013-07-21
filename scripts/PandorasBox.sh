#!/usr/bin/env bash

gpio -g mode 9 in

# prevent startup if button6 is pushed
if [ $(gpio -g read 9) = 1 ]
then
	sudo python /home/pi/src/Pandora-Pi/scripts/ButtonWatcher.py
fi
