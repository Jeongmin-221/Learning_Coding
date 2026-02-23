import random

set1 = set()
set2 = set()
while len(set1) < 5:
    num = int(input("1~30의 숫자 하나를 입력해주세요 : "))
    if num < 1 or num > 30:
        print("다시 입력해주세요.")
        continue
    set1.add(num)

while len(set2) < 5:
    set2.add(random.randrange(1,30))

print(set1)
print(set2)
print(set1.intersection(set2))
