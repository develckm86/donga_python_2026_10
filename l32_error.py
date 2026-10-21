#에러의 종류와 예외 

#문법오류 SyntaxError 가 존재하면 프로그램이 실행되지 않음 ! => 작성을 다시!
#print(
# print("안녕")
#a="안녕'

#예외 : 실행도중에 발생하는 예상 못한 오류 => try except로 예외 처리가능 (try catch)

arr=[7,8,9,10]
print(arr[0],arr[1],arr[2],arr[3])
try:
    print(arr[4]) #IndexError: list index out of range
except IndexError as e:
    print("범위를 벗어났습니다.", e)


a="13"
b=15
#print("a+b=",a+b) #TypeError: can only concatenate str (not "int") to str
print("a+b=",int(a)+b) #예외가 발생하지 않도록 코드작성

a="십삼" #ai는 13인걸 알수 있지만 일반적인 프로그램은 13인 것을 알수가 없다!
try :
    print(int(a)) #ValueError: invalid literal for int() with base 10: '십삼'
except Exception as e :
    print("형변환 시 오류발생",e)