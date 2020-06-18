#!/bin/bash
read -p "input a path>> " path

if [ -L "$path" -a -e "$path" ];then
	echo "its a link"
elif [ -d "$path" ];then
	echo "its s directory"
elif [ -f "$path" ];then
	echo "its a file"
else
	echo "some others"
fi
