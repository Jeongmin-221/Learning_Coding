a = input("문자열 입력>")
aa = set()

for i in a:
    if 'A' <= i <= 'z':
        aa.add(i)

print(aa)
