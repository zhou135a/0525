#coding=utf-8
class student:                   #创建一个类
    def study(self):             #方法列表
        print('im study!!!')
    def play(self):
        print('im playing ball')

boy=student()
#实例化对象，产生了一个student对象，通过boy实例对象来访问属性和方法
boy.age=20
#给对象添加属性
boy.favor='baseball'
boy.study()
boy.play()
#通过实例化对象访问类里面的方法
print(boy.age)
print(boy.favor)
