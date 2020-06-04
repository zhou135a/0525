#coding=utf-8

def func1(p):
    dn=0    #数字个数
    an=0    #字母个数
    en=0    #其他个数
    for i in p:
        if i.isdigit():
            dn+=1
        elif i.isalpha():
            an+=1
        else:
            en+=1
    return (dn,an,en)
r=func1('qwe 123')
print(r)
