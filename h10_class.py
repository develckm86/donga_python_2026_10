#쇼핑몰에서 item을 객체로 관리하고 싶다.
#1. Item 클래스를 만들어서 name, price, qty 을 갖도록 합니다.
#2. Item 을 객체(Item())로 만들때 이름, 가격, 수량을 초기화 하세요!
#3. add_qty 함수를 만들어서 수량을 증가시켜보세요!

#쇼핑몰 개발자가 상품을 dict으로 관리해왔다..-> 불편 class => 객체

# milk={'name':'우유','price':3000,'qty':50, 'sale':True}
# egg={'name':'계란','price':6000,'qty':5, 'sale':False}
# apple={'name':'사과','price':1200,'qty':20, 'sele':True} 
# # 500개의 상품이 있다...
# items=[]
# items.append(milk)
# items.append(egg)
# items.append(apple)
# print(items)

from ast import Return
class Item :
    def __init__( self, name, price, qty, is_sale=True ) :
        self.name=name
        self.price=price
        self.qty=qty
        self.is_sale=is_sale
    #모든 클래스는 이미 정의된 함수가 있는데 __(init,str)__ 새롭게 정의(재정의,override)
    def __str__(self) : #<__main__.Item object at 0x000001E2BB078530>
        return (f'상품정보입니다. 이름 : {self.name}, 가격 : {self.price}')

    def add_qty(self, qty) :
        self.qty+=qty

    def cost(self) :
        return self.price*self.qty


i=Item("계란", 6000, 10 )  #객체를 만들기 위해서는 생성자를 호출해야함!!
# . 객체의 속성 접근자
#i.name="우유"
#i.price=2000
print(i) #<__main__.Item object at 0x000001296048A3F0>
i.add_qty(3) #객체는 기능(함수) 추가가 가능!
print(i.__dict__) #객체.__dict__ : 객체의 속성을 dict의 key-value로 변환!(객체와 dict은 유사)
print("계란의 총가격",i.cost())


i2=Item("우유",3000,200)
print("우유의 총가격 :",i2.cost())
i3=Item("멜론",10000,0,False)
i4=Item("수박",20000,5,True)
item_arr=[i, i2, i3, i4] 
#print(item_arr)


#장바구니를 만들어서 상품을 관리, 상품의 총액 및, 관리(추가(o),삭제(x),수정(o))

#상품을 배열로 관리하는 장바구니
class Cart :
    def __init__(self) :
        self.cart=[] #[ Item(사탕,1),Item(새우깡,2)]

    def add(self, item) :
        #self.cart.append(item)
        #동일한 상품이 들어오면 수량만 증가 => 반복탐색으로 같은 상품이 있는지 검색
        is_find=False
        for i in self.cart :
            if i.name == item.name :
                i.add_qty(item.qty)
                is_find=True
        if is_find == False :
            self.cart.append(item)
    #cost 함수로 장바구니의 전체가격을 반환하세요! (CartDict도 cost 구현)

    #삭제구현!(ai로 해도 ok)

c=Cart()
c.add(Item("사탕",500,1))
c.add(Item("새우깡",1500,2))
c.add(Item("새우깡",1500,1))
print(c.cart[0].__dict__)
print(c.cart[1].__dict__)
#print(c.cart[2].__dict__)

d={"a":10,"b":20,"우유":Item("우유",2000,2)}
print("딕에 우유가 있니? ","우유" in d) #해당 키가 있니?

class CartDict :
    def __init__(self) :
        self.cart={}
        #상품이름의 상품의id {"사탕":Item("사탕",500,1),}
    def add(self, item) :
        if(item.name  in self.cart) :
            self.cart[item.name].add_qty(item.qty) #기존상품에 수량만 추가!!
        else :
            self.cart[item.name]=item #상품추가

card_dict=CartDict() #장바구니 생성
card_dict.add(Item("사탕",500,2))
card_dict.add(Item("사탕",500,5))
card_dict.add(Item("새우깡",1500,3))
card_dict.add(Item("새우깡",1500,1))
card_dict.add(Item("새우깡",1500,2))
print(card_dict.cart)
print(card_dict.cart["사탕"].qty)



