result = []
max_ = 100

for i in range(1,101):
    result.append(i)

result.remove(1)
for i in range(2,int(max_**0.5)+1):
    for a in range(2,100//i+1):
        if a*i in result:
            result.remove(a*i)

print(result)
