#!/bin/bash

#变量的赋值

kernel1=`uname -s`
echo "$kernel1"
echo '$kernel1'


kernel2=$(uname -s)
echo $kernel2

#交互形式赋值

read -p "input your name" username
echo "your name is $username"

read -s -p "insert your passwd " passwd
echo
echo "your passwd is $passwd"
