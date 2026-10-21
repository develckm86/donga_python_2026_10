#object dict 유사
#i=Item("우유",3000) => i.price
#i={"price":3000} => i["price"]

import math as m
cart_arr=[
    {'name':'사발면','price':1000,'qty':3},
    {'name':'왕뚜꺼','price':1500,'qty':5}
]
#cart의 전체 가격 => 반복탐색
total_price=0
for cart in cart_arr :
    #print(cart)
    total_price += cart["price"]*cart["qty"]
print("카트의 전체 가격",total_price)

class Item :
    def __init__(self, n, p, q) :
        self.name=n
        self.price=p
        self.qty=q

cart_arr2=[ Item("우유",3500,3), Item("사탕",500,10)]

total=0
for cart in cart_arr2 :
    total+=cart.price*cart.qty
print("카트2의 전체 가격 ",total)


