dic = {}
sum = 0

dic['국어'] = int(input("국어:"))
dic['영어'] = int(input("영어:"))
dic['수학'] = int(input("수학:"))

for i in dic.values():
    sum+=i

print(f"총점 : {sum}\t평균 : {sum/len(dic):.2f}")
