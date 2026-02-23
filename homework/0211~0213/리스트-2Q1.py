a = input("문자열을 입력해주세요 : ")

for i in range(len(a)):
    print(a[(i+1)*-1], end = "")
