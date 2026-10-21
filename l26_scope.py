#sope 수업을 위한 예시를 만들어줘

def sum (a,b) : # a, b는 매개변수이면서 지역변수(해당 영역에서만 유효)
    c="안녕!" #지역변수
    return a+b

print(sum(99,88)) #지역변수 a,b 함수 sum이 호출될때만 존재함
#print(a,b) #NameError: name 'a' is not defined
print(sum(11,22)) #함수는 호출될 때마다 새롭게 생성됨
#print(c)
