a=10
print(type(a)) #<class 'int'>
#class : 타입을 의미 
#int : integer 정수 
a=10.12
print(type(a)) #<class 'float'> 실수

a= 10 == 10.0 # == 동등비교연산 결과 bool
print(a, type(a)) #True <class 'bool'>

a = 10/3 # 어떤언어는 정수끼리의 연산은 정수를 내놓는다(반환).
print(a) # 3.3333333333333335
#모든 프로그램은 데이터의 크기가 존재하기 때문에 무한한 데이터는 없다!
#실수의 크기가 고정이기 때문에 무한소수는 존재할 수 없다!

a="문자열입니다~"
print(len(a),a,type(a)) #7 문자열입니다~ <class 'str'>