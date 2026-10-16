nums=[-99,67,88,0,77,66,55]

print(nums[0],nums[1],nums[6])
print(len(nums))
#print(nums[20]) #list index out of range
#반복자는 마지막에 데이터가 없으면 False 를 반환하면서 종료됨
for n in nums :
    print(n)

names=["최경민","홍길동","고길동","둘리"]
print(names[2:4])
print(names[2:5]) #슬라이싱 없는 인덱스를 참조해도 오류가 뜨지 않도록 설계되었다.
print(names[2:]) 
# 리스트 유용한 함수
names.append("김철수")
names.append("이영희")
#names.append("만득","마이콜")
print(names) #['최경민', '홍길동', '고길동', '둘리', '김철수', '이영희']