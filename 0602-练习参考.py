#coding=utf-8

a='123abcd'
print(len(a))
'''
for i in range(1,len(a)+1):
    print(a[-i],end="")
'''
l=[]
for i in a:
    l.append(i)
print(l)
l.reverse()
print(l)
for i in l:
    print(i,end="")

