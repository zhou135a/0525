#coding=utf-8
#1.实参位置
def info(name,age):
    print('名字是%s,年龄是%d'% (name,age))
info('o8ma',200)
#info(300,'5kong')

#2.关键字参数
def animal(pet1,pet2):
    print(pet1+'wang!!!!'+pet2+'miao!!!!')

#animal(pet2='cat','2ha')
animal('2ha',pet2='jiafei')
animal(pet2='bosi',pet1='taitan')
#3.参数默认值
def userinfo(name,age,minzu='汉'):
    print('您的名字%s,年龄%d,民族%s'%(name,age,minzu))

userinfo('o8ma',90)
userinfo('ladeng',80,'v5er')
#4.不定长参数
def test(x,y,*args):
    print(x,y,args)
test(1,2,'o8ma','ladeng')
def test1(x,y,**args):
    print(x,y,args)
test1(1,2,a=10,b='gaga')







