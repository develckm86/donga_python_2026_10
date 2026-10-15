
user_name="경민"
user_name=user_name+" 안녕" #문자열은 더하기 연산이 가능
print(user_name)
print(user_name*10)

#문자열 사용시 주의
#1. 문자열은 수가 아니다!
#2. 문자열과 다은 타입은 연산이 불가능하다!

user_age="40"
#print(user_age+1) #can only concatenate str (not "int") to str

#문자열을 다른 타입과 연산하려면 형 변환이 필요하다!!!
print(user_age+str(1)) # "401"
print(int(user_age)+1) # 41

#대입 연산자 
# = : 대입 연산자
# +=, -=, *=, /= : 할당연산자, 복합 할당 연산자

a=10
a=a+1
a=a+1
a+=1
a+=1
print("a=",a)

say="경민"
say=say+"안녕"
say+="안녕!"
print(say)

name="경민"
age=40
say=name+"님은 " + str(age) +"입니다"
print(say)
say=f"{name}은 나이가 {age} 입니다!"
print(say)


user_birth=input("당신의 태어난 해는?") # 1986=> "1986" : 입력받거나 출력하는 것은 모두 문자열이다!
user_birth=int(user_birth)

now_birth=2026
print(f"당신의 나이는 {now_birth-user_birth}")



