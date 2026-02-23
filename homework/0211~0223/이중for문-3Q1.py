print("while버전 소수 구하기")

num = 2
while num<20:
    is_prime = True
    i = 2
    while i < int(num**0.5+1):
        if num%i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num, end = " ")

    num+=1
