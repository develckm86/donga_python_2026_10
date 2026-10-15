
scores=[88,78,99,100,50,85,95]
sum=0
#iterator 반복문 (반복자)
for n in scores :
    #print(n)
    sum+=n

print("scores의 전체 합은 ",sum)
print("scores의 평균은 ",sum / len(scores))


say="안녕하세요~~!!"

for c in say :
    print(c)
    if c=="하" : break
