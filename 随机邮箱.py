import random
n=int(input('随机邮箱名的长度='))
s='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
name=''
for _ in range(n):
    i=random.choice(s)
    name=name+i
print(name+'@qq.com')
