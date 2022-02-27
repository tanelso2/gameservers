#!/bin/bash

if [ ! -p fifo ]; then
	echo "fifo pipe missing, creating"
	mkfifo fifo 
fi

server/TerrariaServer -config /home/terrariaserver/server/serverconfig.txt < fifo &
python3 server_commander.py > fifo
