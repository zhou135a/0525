#coding=utf-8
'''
class student:
    def __init__(self):
        self.boy=20
        self.girl=30
    def study(self):
        print('good good study!!')

java=student()#实例化对象
print(java.boy)
print(java.girl)
'''
class student:
    def __init__(self,boy,girl):
        self.badboy=boy
        self.cutegirl=girl
    def study(self):
        print('study!!!!')
z=student(300,20)
print('班级有男生%d个'% z.badboy)
print('班级有女生%d个'% z.cutegirl)
    
