#!/bin/bash
#条件判断

if [ -f "/etc/passwd" ];then
	echo "file is exists"
fi


if [ -f "/etc/pass" ];then
	echo "file is exists"
else
	echo "file not exists"
fi

if ls /etc/dasdsadsa &> /dev/null;then
	echo "ok"
else
	echo "failed"
fi
