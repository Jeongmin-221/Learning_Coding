multi2 = set()
multi3 = set()
multi5 = set()
temp=0
a=1
while a*2<30:
    temp = a*2
    multi2.add(temp)
    a+=1

a=1
while a*3<30:
    temp = a*3
    multi3.add(temp)
    a+=1

a=1
while a*5<30:
    temp = a*5
    multi5.add(temp)
    a+=1

print(multi2)
print(multi3)
print(multi5)
