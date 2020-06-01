#coding=utf-8
#设置字符集为utf-8
#字符集相当于翻译官，解析不同语言用于显示
#中文字符集 GBK2312
#1.直接输出
#通过print()函数进行打印，把括号中内容显示在屏幕上
print('翻滚吧,牛宝宝')
print(1000000)
#2.变量输出
#变量可以理解为容器，容器的值是不固定的，设置什么就保存什么
name='python'
print(name)
name='gaga'
print(name)
#变量操作后输出
a=100
b=20
print(a+b)
a='heygor is '
b='250'
print(a+b)
#3.函数输出
#输出函数处理过的值
#abs()   绝对值
#len()  字符串的长度(元素的个数)
print(abs(-20))
name='heygor gaga'
print(len(name))
#4.格式化输出
# %s  输出字符串
# %d  输出整型
#如果语句中只传入一个变量，不需要加括号，如果多个变量，需要加括号
name='python'
no=1
print('%s is no.%d'%(name,no))

name='heyga'
print('%s is so cool'% name)


















