#!/bin/bash
str1="hello world"
str2=

if [ -n "$str1" ];then
	echo "OK"
else
	echo "failed"
fi

if [ -z "$str2" ];then
	echo "string  size is zero"
else
	echo "failed"
fi
echo
if [ -z "$str1" ];then
	echo "string  size is zero"
else
	echo "failed"
fi

num1=123
num2="123 "
if [ "$num1" = "$num2" ];then
	echo "num1 = num2 "
else
	echo "num1 !=num2"
fi












