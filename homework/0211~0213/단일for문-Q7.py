cnt = 0
for a in range(101):
    if a%3 == 0 and '7' in str(a):
        print(a, end = " ")
        cnt+=1
    if cnt == 5:
        break;
