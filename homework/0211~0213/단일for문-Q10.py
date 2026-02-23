for a in range(97,123):
    if a%2 == 1:
        print("{}({})".format(a, chr(a)), end = " ")
    else:
        print("{}({})".format(chr(a), a), end = " ")
