#coding=utf-8
#创建元组
tup=(1)
print(type(tup))
print(tup)

tup=(2,)
print(type(tup))

#元组的访问
a=(1,2,3)
print(a)

for i in a:
    print(i)

if 3 in a:
    print('yes')
#删除元组
a=(1,2,3)
del a
#del a[0]
#print(a)

#索引和切片
tup=(1,2,3,4,5)
print(tup)
print(tup[0])
print(tup[-2])
print(tup[2:4])
print(tup[3:])
print(tup[:3])

#补充
tup=(1,2,3,4,5)
print(len(tup))
print(max(tup))
print(min(tup))
print(tup.index(3))
print(tup.count(3))



