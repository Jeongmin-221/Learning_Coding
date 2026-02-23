a=0
_list=[]

while a!= 5:
    a = int(input("1.추가 2.삭제 3.확인 4.선택추가 5.종료 : "))
    if a == 1:
        inp = input("추가할 문자열을 입력해주세요.")
        _list.append(inp)
    elif a == 2:
        _list.pop(-1)
    elif a == 3:
        print("현재 리스트입니다.")
        print(_list)
        continue
    elif a == 4:
        inp = input("추가할 문자열을 입력해주세요.")
        ind = int(input("추가할 위치를 입력해주세요."))
        _list.insert(ind,inp)
    
    
    if a!=5:
        print(_list)
