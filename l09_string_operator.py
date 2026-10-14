a="안녕"
b="하세요!"
result=a+b
print(result)
#concat : 열의 더하기 연산
#print(a-b)
print(a*10) #파이썬의 특별한 기능!
#이스케이프 문자 (문자가 아닌 문자, 키보드의 키(라안개행,탭))
a="안녕 \n하세요~ \n경민코딩\t입니다!" 
print(a)
# \백(역)슬러시  
# /슬러시  
# | or

age=40
#f-문자열, 포맷티드 문자열
say="안녕하세요 최경민입니다. 나이는 "+str(age)+"입니다!"
print(say)

say=f"안녕하세요 최경민입니다. 나이는 {age}입니다!"
# [대괄호] {중괄호} (소괄화 )
print(say)

#rf"" : \n 탈출문자를 사용하지 않는 문자열 => 경로사용시 
path=rf"c:\nsers\Dong\Downloads"
print(path)
