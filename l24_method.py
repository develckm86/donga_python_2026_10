#프로그래밍 -> 자동화 -> 논리적 -> 수학 

def say( name ="경민코딩" ) : #파라미터, 전달인자(전달받는데이터)
    print("안녕하세요~")
    print(f"{name} 입니다~")
    print("#"*30)

say()
say("고양이")
say("호랑이")
say("강아지")

#매개변수의 기본값은 뒤에서 부터 주어야 문제없이 동작 
def add( a, b, c=0) :
    print(f"a+b+c={a+b+c}")

#1. add 를 호출하세요!  33,44,55 합을 구하세요
add(33, 44, 55)
add(77, 88, 99)
add(11, 22) # 기본값을 주고 오류가 뜨지 않게 하세요!


# 수 3개를 받아서 곱한 결과를 출력하는 함수를 만드세요!->호출
def mult (a, b, c) :
    print("a x b x c = "+str(a*b*c))

mult(4,5,6)
mult(14,15,16)
mult(11,12,13)
#mult(1,2) #mult() missing 1 required positional argument: 'c'