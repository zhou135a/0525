#coding=utf-8
import csv

with open('D:\\1.csv','r') as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)
        print(type(i))

with open('D:\\3.csv','w') as f:
    file=csv.writer(f,dialect='excel')
    #写入文件常用方式writerow
    file.writerow([1,2,3,4])
    file.writerow([5,6,7,8])
    
print('ok')
