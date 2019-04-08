#! /bin/bash

#IP=$(dig +short myip.opendns.com @resolver1.opendns.com)
IP=$(curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//')


if pgrep -x openvpn > /dev/null; then
    	echo $IP '(VPN)'
    else
        echo $IP
fi
