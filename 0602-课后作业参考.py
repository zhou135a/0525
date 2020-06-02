#coding=utf-8
'''
for i in range(-3,4):
    #print(i)
    if i<0:
        a=-i
    else:
        a=i
    #print(7-a*2)
    print(a*' '+'*'*(7-a*2))
'''
'''
n=int(input('请输入一个数字'))
c=n//2
for i in  range(-c,c+1):
    a=-i if i<0 else i
    print(' '*a+'*'*(n-a*2))
    
'''
n=7
e=n//2
for i in range(-e,n-e):
    #print(i)
    a=-i if i<0 else i
    print(' '*(e-a)+'*'*(2*a+1))

#99乘法表
#print()函数格式化输出中使用end=""不换行显示
for i in range(1,10):
    for j in range(1,i+1):
        print(' '+str(i)+'*'+str(j)+'='+str(i*j),end="")
    print()













