#coding=utf-8
#通过input函数对键盘输入进行处理
#input括号中可以填写提示信息
#name=input()
#print('your name is %s'% name)

name=input('请输入您的法号：')
print(type(name))
print('%s 大师，久仰久仰！！！'% name)

sal=int(input('请输入您的薪资'))
sal2=int(input('请输入您的奖金'))
print(sal+sal2)
