#coding=utf-8

#字符串
for i in 'abcde':
    print(i)

#列表
l=[1,2,'o8ma','ladeng']
for a in l:
    print(a)

#函数
#内置函数range()
#range(10)    0-9
#range(1,10)  1-9
    
for i in range(10):
    print(i)

for i in range(1,10):
    #print(i)
    print('*'*i)

for i in range(-5,5):
    #print(i)
    if i<0:
        print(-i)
    else:
        print(i)
