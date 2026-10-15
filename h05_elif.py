#성적을 만드는 프로그램 score 입력 받으면 grade 이 나오는 프로그램 
# 예 88 -> B , 95-> A, 55 -> F
score_str=input("당신의 성적은?")
score=int(score_str)
grade="F" # else 를 대신할 수 있다.(기본값 default)

if score>100 or score<0 :
    print("점수는 100점 이하 0점 이상만 입력하세요!")
else :
    if score >= 90 :
        grade = "A"
    elif score >= 80 :
        grade = "B"
    elif score >= 70 :
        grade = "C"
    elif score >= 60 :
        grade = "D"
    else :
        grade = "F"
        
    print(f"당신의 등급은 {grade} 입니다.")
