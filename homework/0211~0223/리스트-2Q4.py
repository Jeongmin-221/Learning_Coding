result = []
max = 100

for i in range(1,101):
    result.append(i)

result.remove(1)
for a in range(2,100//2+1):
    if a*2 in result:
        result.remove(a*2)

for a in range(2,100//3+1):
    if a*3 in result:
        result.remove(a*3)

print(result)
