
# 성적내는 프로그램 
# 점수(88)를 입력하면 성적(B)을 반환하는 함수(grade_test)를 만드세요
# 점수를 터미널에서 입력 받아서 grade_test 호출해 성적을 알려주세요!
# 무한 반복문을 작성해서 프로그램이 종료되지 않게 작성하세요!

def grade_test(score) :
    grade="F"
    if score>=90 :
        grade="A"
    elif score>=80 :
        grade="B"
    elif score>=70 :
        grade="C"
    else :
        grade="F"
    return grade

while True :
    score_str=input("성적입력 :")
    score=int(score_str)
    grade=grade_test(score)
    print(f"당신의 등급은 {grade} 입니다.")
