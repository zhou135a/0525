#coding=utf-8
import os
import sys
os.system('tasklist')      #运行系统中的命令tasklist
#os.remove('D:\\txl.txt')   #删除系统中的文件
print(os.getcwd())         #当前文件夹的绝对路径
print(os.listdir('D:\\'))  #当前文件夹下所有文件名字
print(os.path.isfile('D:\\1.csv')) #判断是否是文件
#os.path.isdir() 判断是否是目录
#os.path.exists()判断是否存在

print(sys.version)
print(sys.path)
