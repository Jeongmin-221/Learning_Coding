followers = {
    "강민수" : True,
    "이철수" : False,
    "오민지" : True,
    "박수민" : False
    }

print("이전 팔로워 : ", end = "")
for i in followers.keys():
    print(i, end = " ")
print()
print("현재 팔로워 : ", end = "")
for i in followers:
    if followers[i]:
        print(i, end = " ")
