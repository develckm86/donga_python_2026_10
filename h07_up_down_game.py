import random #도구 라이브러리
#컴퓨터 1~100까지 수 중에 랜덤하게 뽑은 수를 10번안에 맞추는 게임 
print("컴퓨터 1~100까지 수 중에 랜덤하게 뽑은 수를 10번안에 맞추는 게임 ")
random_num=random.randint(1,100)
print("컴퓨터가 뽑은 수 :", random_num)
#게임의 규칙
#1. 수를 입력 받아서 맞을때 까지 무한 반복
#2. 입력 받은 수가 정답보다 작으면 up
#3. 입력 받은 수가 정답보다 크면 down 으로 힌트 제공
#4. 정답을 몇번 째에 맞추었는지 공지함
cnt=0
REST=10
while True :
    num_str=input("1~100수 중 하나를 입력 : ")
    num=int(num_str)
    cnt+=1
    #print(num,random_num, num==random_num)
    if num == random_num :
        print(f"정답!!! 남은기회 {REST-cnt}")
        break
    elif num > random_num :
        print(f"오답 Down! 남은기회 {REST-cnt}")
    else :
        print(f"오답 Up! 남은기회 {REST-cnt}")

#1.예외가 발생할 수 있는 상황을 찾으세요!
#2.예외를 처리하세요!
