#class data의 형태(type)
#같은 종류의 데이터는 같은 속성과 함수(기능)을 갖는다.
a="안녕!"
b="잘가!"
print(type(a)) #<class 'str'>
print(a.split("녕"))
print(b.split("가")) #a b 는 다른 데이터지만 형이 같아서 같은 기능 갖는다!

#형은 파스칼 규칙 (대문자로 시작, 문자간의 결함은 대문자로)
class User :
    #__init__ : 생성자는 객체의 속성을 초기화 
    def __init__(self, name, age) :
        self.name=name  #속성
        self.age=age
    # 함수 : 객체의 기능! 
    def say(self) :
        print("안녕~ 나는 "+self.name)
#User 객체를 만들면 이름과 나이를 속성으로 갖는다!

u1=User("경민",40)
u2=User("고길동",50)
print(u1.name, u1.age) 
print(u2.name, u2.age)
print(u1.__dict__) #{'name': '경민', 'age': 40}
print(u2.__dict__) #{'name': '고길동', 'age': 50}
#객체와 딕셔너리는 유사하다!! (함수는 딕셔너리[data]서 제외 )
u1.say()
u2.say()


