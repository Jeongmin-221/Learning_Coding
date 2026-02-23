a = int(input("수 입력>"))

for i in range(1,a//2+1):
    if a%i == 0:
        print(i, end = " ")

print(a)
