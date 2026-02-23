sta = int(input("몇단부터? : "))
end = int(input("몇단까지? : "))

for i in range(sta, end+1):
    for j in range(1,10):
        print("{} * {} = {}".format(i, j, i*j))
    print()
