#coding=utf-8
class student:
    def __init__(self,name):
        self.name=name
    def info(self):
        print('你的名字是%s'% self.name)

def StudentInfo(s):
    s.info()

heygor=student('heygorgaga')
#heygor是student类的实例化对象
#对象实例化之后可以调用类里面的方法
StudentInfo(heygor)
#StundentInfo括号中传入的heygor是一个已经实例化的对象
#函数传参可以传入常规函数，也可以传入对象
    
