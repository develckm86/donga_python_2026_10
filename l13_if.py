#조건 분기 
age=17 # 입력받은 나이
#성인(19)만 입장 가능한 어플 
#성인이면 입장
#미성년자는 퇴장
# tab == 들여쓰기=> 영역(scope)이 생긴다
print("성인 19세 이상만 입장가능 합니다 : ", age)
if age>=19 :
    print("입장")
else :
    print("퇴장")

print("#"*30)

score=70
print("성적이 60점 보다 작으면 낙제 아니면 통과:",score)
if score < 60 :
    print("낙제")
else :
    print("통과")



