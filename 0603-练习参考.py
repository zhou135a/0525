#coding=utf-8
#dic={'username1':'admin','passwd1':'123'}

dic={'admin':'123456','heygor':'654321'}
while 1:
    name=input('请输入用户名')
    if len(name)==0 or name not in dic.keys():
        print('请重新输入')
    else:
        print('ok')
        while 1:
            passwd=input('请输入密码:')
            if dic[name]==passwd:
                print('登录成功')
                break
            else:
                print('您的密码有误，请重新输入')
        break
        
            
            
