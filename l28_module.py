import random #모듈 (내장모듈 )
from random import choice
s="안녕하세요!"
print(s, len(s),list(s)) #len(내장함수)

print(random.randint(1, 11))

arr=["짜장","짬뽕","제육","햄버거"]
c=random.randint(0,len(arr)-1)
print(arr[c])
print(choice(arr))
print(random.choice(arr))




