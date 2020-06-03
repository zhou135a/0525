#coding=utf-8
#定义一个变量接受open函数打开后文件内容
file=open('D:\\test.txt','r')
print(file)
for i in file:
    print(i)
file.close()

#写文件
str1='oh my dear baby!!!'
file=open('D:\\memeda.txt','w')
file.write(str1)
file.close()
print('已经ok了')

#追加文件
file=open('D:\\test.txt','a')
file.write("\n come on baby!!!")
file.close()
