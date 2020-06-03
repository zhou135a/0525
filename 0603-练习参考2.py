#coding=utf-8
dic={'admin':'12345'}
name=input('your name!')
passwd=input('your password')

#定义写入文件的方式，filename文件路径，text文件内容，正确和错误都要写入文件所以需要追加
def WriteFile(filename,text):
    file=open(filename,'a')
    file.write(text)
    file.close()
    print('写入成功')

def LogIn(name,passwd):
    if name in dic.keys():
        #print('写入文件')
        if dic[name]==passwd:
            WriteFile('yes.log',name+','+passwd)
            return "success"
        else:
             WriteFile('no.log',name+','+passwd)
             return "failed"
    else:
        return "username is wrong!"
#变量接受函数处理后的结果
p=LogIn(name,passwd)
print(p)
    
