#쇼핑몰에서 item을 객체로 관리하고 싶다.
#1. Item 클래스를 만들어서 name, price, qty 을 갖도록 합니다.
#2. Item 을 객체(Item())로 만들때 이름, 가격, 수량을 초기화 하세요!
#3. add_qty 함수를 만들어서 수량을 증가시켜보세요!

class Item :
    def __init__(self, n, p, q) :
        self.name=n
        self.price=p
        self.qty=q
    def add_qty (self, qty) : #수량 더하기
        self.qty+=qty
    def sub_qty (self, qty) : #수량빼기
        self.qty-=qty

i0=Item("초콜릿",5000,200)
i0.add_qty(50)
i0.sub_qty(100)
print(i0.__dict__)


