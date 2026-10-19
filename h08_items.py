items=[
    {"name":"우유","price":2800,"qty":2},
    {"name":"계란","price":6500,"qty":1},
    {"name":"사과","price":1500,"qty":4}
]
# 2번 문제 정답 (전체조회)
for item in items :
    for key, value in item.items() :
        print(key, value)

# 3번 문제 정답 (아이템의 총액)
total_price=0
for item in items :
    print(item["name"],item["price"]*item["qty"])
    total_price+=item["price"]*item["qty"]
print(f"상품의 총금액은 {total_price:,}원 입니다")

max_price=0
#max_price=items[0]["price"]
for item in items :
    if max_price < item["price"] :
        max_price=item["price"]
print(max_price) 