while True :

    print("총금액과 인원을 알려주면 더치페이 금액을 계산하는 프로그램")
    #예외 처리로 수가 아닌 문자열을 입력할시 "수만 입력하세요"로 안내하고 다시 입력 받으세요!
    try :
        total_price=input("총금액은? :")
        total_price=int(total_price)
        total_cnt=int(input("총인원은? :"))
        #print("입력하신 금액과 인원을 확인하세요",total_price,total_cnt)
        #print(total_price/total_cnt) #"10"/"3"
        quot=(total_price//total_cnt) #"10"/"3"
        mod=(total_price%total_cnt) #"10"/"3"
        #print("1인당 내야할 금액은"+str(quot)+"원 입니다.")
        print(f"1인당 내야할 금액은 {quot:,}원 입니다.")
        print(f"남은 금액은 {mod}원 입니다. 가위바위보로 정하세요!")
        status=input("어플을 종료하고 싶으면 exit 입력하시고 아니면 enter! : ")
        if status == "exit" : break
    except Exception as e :
        print("총 금액과 인원은 정수만 입력 가능합니다.",e)

