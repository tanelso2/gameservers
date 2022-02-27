#!/bin/bash

USERNAME=${USERNAME:?Hey username is not set}
PWORD=${PWORD:?Hey password is not set}
APP_ID="105600"

echo "Steam guard code for user: "
read code

steamcmd \
	"+force_install_dir ./server" \
	"+login ${USERNAME} ${PWORD} ${code}" \
	"+app_update ${APP_ID} validate" \
	"+quit"


