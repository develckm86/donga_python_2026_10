#as 가명 (동일한 이름의 모듈이나 변수 함수를 피하기 위해)
import random as rd
from datetime import date #시분초를 제외
from datetime import datetime
import pandas

print(date.today()) #2026-10-19
print(date.today().year) #2026
print(date.today().month) #10 (1월 == 0월)
now=date.today()
print(now.day)
print(now.weekday()) #0월요일~ 6일요일
weeks=["월","화","수","목","금","토","일"]
print(weeks[now.weekday()])
date_format="%Y년 %m월 %d일 %H시 %M분 %S초 %p"
print(date.today().strftime(date_format))
print(datetime.now().strftime(date_format))


#특정 날짜 만들기
birth= date(1986,5,25)
#print(birth)




#print(rd.choice(["아메리카노","라떼","아이스티","수박주스"]))