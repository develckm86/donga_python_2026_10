#리스트와 딕셔너리의 중첩구조를 만들보자 (표)
customers=[
    {"name":"홍길동","age":50},
    {"name":"최경민","age":40},
    {"name":"김철수","age":20}
]
print(customers[0])
print(customers[0]["age"])
cus2=customers[2]
print(cus2)
print(cus2["name"])

age_sum=0

for c in customers :
    print(c["age"]) #고객의 나이만 보이게 하세요
    age_sum+=c["age"]

print(age_sum , age_sum/len(customers))
#고객의 나이의 합과 평균을 구하세요!
