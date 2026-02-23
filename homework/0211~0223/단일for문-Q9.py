a = input("문장 입력 : ")
cnt = 0
for i in a:
    if i.isdigit():
        cnt+=1

print("숫자의 갯수 :", cnt)
