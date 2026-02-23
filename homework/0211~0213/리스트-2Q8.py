a=0
_list=[]

while a!= 4:
    a = int(input("1.추가 2.삭제 3.확인 4.종료 : "))
    if a == 1:
        inp = input("추가할 문자열을 입력해주세요.")
        _list.append(inp)
        print(_list)
