a = input("문장 입력")
cnt = 0
for i in a:
    if i in "aeiouAEIOU":
        print("*", end = "")
        cnt += 1
    else:
        print(i, end = "")
print()
print("바뀐 모음의 개수 :", cnt)
