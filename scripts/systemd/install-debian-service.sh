#!/bin/bash
#
# Installs the one of the klipper services.
#
# Convenience script to simplify switching between different klippyer service configurations
#
# OS Support:
#	debian
#	Ubuntu
#
# Usage:
# 	./install-debian-service.sh SYSTED_SERVICE_CONFIG
#
service_config="$1"

if ${UID} -ne 0; then
	echo "Must be root"
else
	systemctl stop klippy &>/dev/null
	
	cp -f "${service_config}" /etc/systemd/system/klipper.service

	pushd . &>/dev/null
	cd /etc/systemd/system
	unlink klippy &>/dev/null
	ln -s $(pwd)/klipper.service klippy
	popd &>/dev/null
	
	systemctl enable klipper
	systemctl start klipper
	systemctl status klipper
fi
