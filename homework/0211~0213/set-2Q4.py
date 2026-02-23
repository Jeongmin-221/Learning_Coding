set1 = {1,2,4,8,16}
set2 = {1,2,3,4,5}

print("리스트 3", set2.difference(set1).union(set1.difference(set2)))
