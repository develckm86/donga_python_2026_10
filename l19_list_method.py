
#method,function : 함수,기능 소괄호를 포함
print("안녕") #터미널 출력 기능 
#age_str=input() #터미널에 입력 
#list.append() : 리스트에 값을 추가하는 기능 
names=[]
print(type(names)) #<class 'list'>
names.append("a")
names.append("b")
names.append("c")
names.insert(1,"안녕!") #리스트의 특정 인덱스에 값을 추가하는 함수 
print(names)
names.pop() # 맨뒤에 값을 삭제
names.pop(1) # 특정 인덱스의 값을 삭제
names.remove("a") #특정 값을 삭제 
print(names)

nums=[]
#append로 -50 -70 10 100 -3 23 을 추가하고 전체 출력을 하세요!
nums.append(-50)
nums.append(70)
nums.append(10)
nums.append(10)
nums.append(10)
nums.append(100)
nums.append(-3)
nums.append(-23)
print(nums)
#특정 값 찾기
print(70 in nums)
# print(nums.index(-30)) # 없는 것을 찾으면 오류 ValueError: -30 is not in list 
print(nums.index(-3))
nums.sort() #오름차순 asc
print(nums)
nums.reverse() #내림차순 desc
print(nums)
#count 몇개 있나?
print(nums.count(10))
print(nums.count(10000))

#배열의 더하기 concat
nums2=[1,2,3]
nums3=[4,5,6]
print(nums2+nums3) # 배열 더하기는 더해진 새로운 배열 생성
print(nums2,nums3)
nums2.extend(nums3) # 기존 배열에 더하기 
print(nums2)

