sta = int(input("몇단부터? : "))
end = int(input("몇단까지? : "))

for i in range(1,10):
    for j in range(sta, end+1):
        print("{} * {} = {}".format(j, i, i*j), end = "\t")
    print()
