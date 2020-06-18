#!/bin/bash
#变量的运算
#方式1
a=100
b=50
let c=$a+$b
echo "c=$c"

#方式2
#支持c语言的语法
let c++ #让c自身加1 ，c=c+1
echo "c=$c"
let c+=2  #c=c+2
echo "c=$c"

#方式3 把计算结果保存下来或者直接输出(推荐)
d=$(( a+b )) #或者 $(( $a+$b))
echo "d=$d"

#方式4
e=`expr $a + $b` #保存结果
expr $e + 100

#以上的计算仅仅支持整数运算
#如果需要支持浮点数运算或者更多运算符号，可以使用bc命令
echo "scale=5;1/3" |bc
echo "scale=5;2*2.5" |bc



