item={
    "name":"새우깡",
    "price":1500,
    "qty":550
    }
#딕셔너리 반복 탐색
for key in item :
    print(key, item[key])

for key in item.keys() :
    print(key, item[key])

for value in item.values() :
    print( value )


for k,v in item.items() :
    print(k, v)
