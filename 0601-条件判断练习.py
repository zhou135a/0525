#coding=utf-8

a=int(input('请输入第一个边'))
b=int(input('请输入第二个边'))
c=int(input('请输入第三个边'))

#等腰  等边  直角   普通

if a==b and b==c:
    print('等边')
elif a==b or b==c or c==a:
    print('等腰三角形')
elif a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
    print('直角三角形')
else:
    print('普通三角形')
