#전역변수 global variable
a=10  #전역에 선언된 변수 => 전역변수 (지역에서 호출가능)

def test() :
    a=20 #지역변수를 생성 (전역변수와 같은이름)
    print("지역변수 a 호출",a)
    print("전역변수 globals()['a'] 호출", globals()['a'] )

print("전역변수 a 호출",a) #a=10
test() #a=20
print("전역변수 a 호출",a) #a=10

print("#"*30)

def test2() :
    global a  #전역변수 a 를 지역에서 사용하겠다!
    a=1000
test2()

print("전역변수 a",a)


