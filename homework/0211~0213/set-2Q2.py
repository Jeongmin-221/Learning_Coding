set1 = {1, 3, 2, 5, 7}
set2 = {3, 8, 4, 5}

print("집합1은 집합2에", end = " ")
if set1.issuperset(set2):
    print("포함됨")
else:
    print("포함되지 않음")

print("집합2는 집합1에", end = " ")
if set2.issuperset(set1):
    print("포함됨")
else:
    print("포함되지 않음")

print("대칭차집합", set2.difference(set1).union(set1.difference(set2)))
