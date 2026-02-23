set1 = set()
while len(set1) < 5:
    num = int(input("1~30의 숫자 하나를 입력해주세요 : "))
    if num < 1 or num > 30:
        print("다시 입력해주세요.")
        continue
    set1.add(num)
print(set1)
