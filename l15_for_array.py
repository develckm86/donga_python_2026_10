#l15_for_array.py
#반복문 for로 배열의 데이터를 추출하자!!

name="경민의코딩입무소" # 문자로된 배열
print(name[0],name[1],name[5]) #배열의 인덱스

num_arr=[11,22,33,44,55,66,77,88] #Array 배열, 수로 된 배열

print(num_arr[0],num_arr[3], num_arr[-1])

sum=num_arr[0]+num_arr[1]+num_arr[2]+num_arr[3]+num_arr[4]+num_arr[5]
print(sum)
i=0
sum=0 #더하기 합집합
while i < len(num_arr) :
    print(i,num_arr[i])
    sum+=num_arr[i]
    i+=1
print("반복문으로 더한 sum :",sum)