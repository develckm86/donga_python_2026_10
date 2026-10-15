#놀이동산  요금 
# 성인 50000원 (19세이상), 
# (13)청소년는 40000원, 
# (8)초등학생 25000 , 미취학 아동 0
# 나이는 130이하 0이상만 입력 가능
print("놀이동산 요금 계산 어플")

price=0
status="미취학 아동"

age_str=input("나이를 입력하세요 : ") #"30" "12"
age=int(age_str)
if age<0 or age > 130 : 
    print("나이는 0~130 사이 값만 입력 가능합니다!")

elif age>=19 :
    price=50000
    status="성인"

elif age>=13 :
    price=40000
    status="청소년"

elif age>=8 :
    price=25000
    status="초동학생" 

print(f"당신은 {status}이고 가격은 {price}입니다.")


