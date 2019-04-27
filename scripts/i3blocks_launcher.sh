#!/bin/bash

DESKTOP=dauntless
LAPTOP=vanguard

if [ $HOSTNAME == $DESKTOP ] 
then
	i3blocks -c $CONFIG/i3blocks/i3blocks_desktop.conf
elif [ $HOSTNAME == $LAPTOP ]
then
	i3blocks -c $CONFIG/i3blocks/i3blocks_laptop.conf
fi
