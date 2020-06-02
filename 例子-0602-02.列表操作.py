#coding=utf-8
'''
#直接访问
l1=['李元芳','李白','钟馗']
print(l1)
print(type(l1))
#遍历访问
for i in l1:
    print(i)
    print(type(i))
#成员访问
if '张小敬' in l1:
    print('长安12时辰')
else:
    print('不在里面')
#列表的索引和切片
l1=['张飞','赵云','黄忠','马超','关羽']
print(l1[0])
print(l1[-2])
#print(l1[5])
print(l1[2:])
print(l1[2:3])
#列表的拼接
l=[1,2,3,4]
m=['a','b']
print(l+m)
#列表的修改
l=[1,2,3]
print(l)
l[2]='柳岩'
print(l)
l[-2]='大鹏'
print(l)
#列表的删除
l=[1,2,3]
print(l)
del l[2]
print(l)
del l
print(l)
'''
#栈的方式访问列表
l=[1,2,3,4]
print(l)
l.append(5)
print(l)
l.append(5)
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)

#获取列表索引
l=['a','b','c','d']
print(l.index('c'))

#枚举
l=['a','b','c']
for index,value in enumerate(l):
    #print(index,value)
    print('索引是'+str(index)+'，值是：'+str(value))
#列表的排序
l=[1,2,3,4]
print(l)
l.reverse()
print(l)
l=[1,3,5,2,4,6]
print(l)
l.reverse()
print(l)
l=[1,3,5,2,4,6]
print(l)
l.sort()
print(l)

l=[1,3,5,2,4,6]
print(l)
l.sort(reverse=True)
print(l)

#补充
#insert()
l=['a','b','c']
l.insert(1,'d')
print(l)
l.insert(-1,'aaa')
print(l)
#extend()
l=[1,2,3,4]
l.extend('a')
print(l)
l.extend([1,2,3])
print(l)










































