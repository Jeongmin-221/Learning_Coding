set1 = {1, 3, 2, 5, 7}
set2 = {3, 8, 4, 5}

print("합집합", set1.union(set2))
print("교집합", set1.intersection(set2))

print("집합1 - 집합2 차집합", set1.difference(set2))
print("집합2 - 집합1 차집합", set2.difference(set1))
