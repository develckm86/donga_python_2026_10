
#순서가 있는 데이터 -> 배열 [] 대괄호
#문자의 순서가 있는 데이터 => 문자열 "",'' ,f"", r""
say="안녕하세요~" #["안","녕","하","세","요","~"]
print(say[0],say[1],say[5],say[-2])
#print(say[6]) #string index out of range
print(say[0:2])
print(say[2:0])
print(len(say))#모든 배열은 길이가 있고 크기를 나타내기 때문에 1부터 시작

#객체 : 복합적인 데이터!(속성과 기능[함수]) (자료형), 문자열은 객체에 해당
# . 참조연산자 : 객체의 자료를 참조할때 사용
phone="010-1234-4435"
phone2=phone.replace("-","*")
phone_arr=phone.split("-")
print(phone_arr)
print(phone2)


