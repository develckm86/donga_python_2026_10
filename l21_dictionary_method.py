user={
    "이름" : "최경민",
    "나이" : 40,
}
print(user["이름"],user.get("이름"))

user_keys=user.keys()
user_values=user.values();
print(user_keys,list(user_keys)) # dict_keys(['이름', '나이', '기술'])  배열과 유사한 타입=>list(배열)
print(user_values)
print(user.items()) #dict_items([('이름', '최경민'), ('나이', '40')])

# del user["나이2"] #keyError 없는 key는 삭제시 오류
del user["나이"]
print(user)
print(user.pop("이름"))
print(user.pop("이름","None")) #없는 것을 지워도 오류발생 x
print(user)


