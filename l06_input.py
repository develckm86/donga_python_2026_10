#터미널에서 문자열을 입력받는 함수
user_name=input("당신의 이름은 :")

#태어난 해를 받아서 당신의 나이는 ?? 맞습니까를 출력 !
#1986 입력
#2026-1986 =40 계산 
#당신의 나이는 40이 맞습니까? 출력
birth = input("당신이 태어난 해는?") #입력은 문자열
now = 2026
age = now - int(birth)
result = user_name + "님 나이는 " + str(age) + "이 맞습니까?"
print( result )
