#성적 입력 함수 88점 -> B
def set_grade( score ) :
    #성적은 0~100사이만 입력 가능합니다! ValueError
    if score>100 or score<0 :
        raise ValueError("성적은 0~100사이만 입력 가능합니다!")
        # 오류 발생시 다음코드는 실행되지 않음!!
    grade= "F"
    if score>=90 :
        grade="A"
    elif score >= 80 :
        grade="B"
    print(f"당신의 성적은 {grade}입니다")

set_grade(99)
set_grade(88)
#set_grade(-200)

def set_age(birth) : #birth로 나이를 계산해서 반환하는 함수 <=1986 "40살입니다."
    now=2026 #1.datetime 모듈로 현재 year 받아오기 (x)
    #birth는 2026을 넘을 수 없다.(미래에 태어날수 없다.)
    if birth > now :
        raise ValueError("미래에 태아날 수 없습니다.")
    age=now-birth
    print(f"당신은 {age}살 입니다.")    

set_age(1986)
try :
    set_age(2030)
except ValueError as e :
    print(e)
#파이썬 문법은 여기까지~~~~
#나머지는 응용~ api,pandas,llm연결,영상자동화! 프롬프트엔지니어링고급, 챗봇만들기