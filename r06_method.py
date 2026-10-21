#함수
print("안녕") #파이썬으로 실행 => 프로그램 (어플)
print(1+1*2/4) #정수 
print(1.3+1.1*2.3/4.2) #실수
#데이터를 재사용 하는 방법 변수
a=10
b="안녕하세요~"
  #분기 청소년(15살이상), 초등학생(8살이상) 미취학아동(나머지) elif
def age_test (param_age) :
    result="미취학 아동"
    if param_age>=19 :
        result="성인"
    elif param_age>=15 :
        result="청소녕"
    elif param_age >=8 :
        result="초등학생"
    return result

while True :
    age=input("나이를 입력 :")
    age=int(age)
    result=age_test(age)
    print(f"당신은 {result} ({age}) 입니다")
    msg=input("exit를 입력하면 종료  :")
    if msg=="exit" : break
    #exit를 입력하면 반복문을 종료하게 작성!
