#놀이동산  요금 
# 성인 50000원 (19세이상), 미성년자는 25000원
ADULT_FRICE=50000
YOUTH_FRICE=25000

print("놀이동산의 요금을 안내해주는 어플입니다!")
#나이를 입력 받아서 비교후 분기
age_str=input("당신의 나이는? :")  #age_str : 문자열인 나이야
age=int(age_str)

if age>=19 :
    print("당신은 성인입니다. ")
    print(f"성인 요금은 {ADULT_FRICE:,}원 입니다.")
else :
    print("당신은 미성년입니다.")
    print(f"미성년의 요금은 {YOUTH_FRICE:,}원 입니다.")