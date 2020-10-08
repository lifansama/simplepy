#生成任意位数的随机数：
import random
n=int(input('随机数长度='))
s='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'#这里可以加入你想要的字符
name=''
for _ in range(n):
    i=random.choice(s)
    name=name+i
print(name)
