#coding=utf-8
#单继承
'''
class dog:
    def __init__(self,name,color='black'):
        self.name=name
        self.color=color
    def run(self):
        print('狗富贵，互相旺')

class taidi(dog):
    def set_name(self,name):
        self.name=name
    def eat(self):
        print('im eating!!!')

gou=taidi('taitan')
print('名字是%s'% gou.name)
gou.eat()
gou.set_name('2ha')
print('旺财的新名字是%s'% gou.name)
gou.run()
'''
'''
#多继承
class a:
    def PrintA(self):
        print('---a---')
class b:
    def PrintB(self):
        print('---b---')
class c(a,b):
    def PrintC(self):
        print('---c---')
c1=c()
c1.PrintA()
c1.PrintB()
c1.PrintC()
'''
class dog:
    def sayhi(self):
        print('wang！！！！')

class keji(dog):
    def sayhi(self):
        print('aowu~~~~')

dog1=keji()
dog1.sayhi()












