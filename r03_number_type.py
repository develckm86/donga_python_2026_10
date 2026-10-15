a=10  #정수 integer int
b=12.2 #실수 float 
print(a, type(a)) #class == 형 타입
print(b, type(b))

c=True #논리 연산의 결과 bool 
#  == != > < >= <=
#*** 논리 연산은 값을 비교한다.
print(c, type(c))
print(10 == 10.0)

# == != 로 문자열을 비교할 수 있다.
user_name="경민222"
user_name2="경민"
print(user_name==user_name2)
print(user_name>user_name2) #다른 언어에서는 수가 아닌 데이터의 크기 비교시 오류가 발생!!!
#파이썬은 문자열 비교시 길이를 비교!


print(10+3) #13
print(10-3) #7
print(10*3) #30
print(10/3) #3.3333333333335 (실수는 2진수로 변화 후 저장되기 때문에 끝에 5)
print(10%3) #1
print(10//3) #3
print(10**3) #1000
