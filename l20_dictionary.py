#딕셔너리 key=value
user={
    "name":"경민",
    "age":40,
    "isMari" :True
    } 
print(type(user)) #<class 'dict'>
print(user) #{'name': '경민', 'age': 40, 'isMari': True}
print(user["age"],user["name"])
#print(user["skills"]) # KeyError: 'skills'
user["city"]="고양시" #없는 것을 호출하는 것은 오류, 대입은 가능
print(user)
print(user.get("name")) #user["name"]
print(user.get("names")) #없는 키를 호출해도 오류 발생 X
print(user.get("names","없음")) #없는 키를 호출해도 오류 발생 X



