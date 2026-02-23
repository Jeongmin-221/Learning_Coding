words = {
    'coding' : '코딩',
    'soccer' : '축구',
    'loop' : '반복문',
    'condition' : '조건',
    }

print("영어 단어 맞추기!")

for i in words:
    a = input(f'{i}: ')
    if words[i] == a:
        print("정답입니다!!")
    else:
        print("틀렸습니다.")
        break
