import random

pwlist = [i for i in range(0,10)] + [chr(a) for a in range(65,65+24)]
result=[]

for j in range(6):
    print(pwlist[random.randrange(0,len(pwlist))], end = "")
    
