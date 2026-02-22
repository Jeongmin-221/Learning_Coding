import random

rsp_ = {
        0 : "가위",
        1 : "바위",
        2 : "보"
        }

def input_rsp():
    print("0:가위\n1:바위\n2:보")
    p = -2
    while -1 > p or p > 2:
        p = int(input("수 입력>"))
    return p

def rsp(p1, p2):
    if (p1+1)%3 == p2:
        return 2
    elif p1 == p2:
        return 0
    else:
        return 1

def output_rsp(result, p1_score, p2_score):
    if result == 1:
        p1_score+=1
        print("you win!")
    elif result == 2:
        p2_score+=1
        print("com win!")
    elif result == 0:
        print("무승부")
    print("you {} : {} com".format(p1_score, p2_score))
    return p1_score, p2_score

def minus_1(p1_1, p1_2):
    print("{}, {}중 하나를 빼야합니다.".format(rsp_[p1_1], rsp_[p1_2]))
    print("0:가위\n1:바위\n2:보")
    p = -1
    while p != p1_1 and p != p1_2:
        p = int(input("뺄 숫자 입력>"))
    _p = p1_2 if p == p1_1 else p1_1
    return _p

def play():
    
    p1_1, p1_2 = 0, 0
    p1_score, p2_score = 0, 0
    while True:
        p1_1 = input_rsp()
        p1_2 = input_rsp()
        
        
        p2_ = [random.randrange(0,3), random.randrange(0,3)]
        p2 = p2_[random.randrange(0,2)]
        print("컴퓨터:{}, {}".format(rsp_[p2_[0]], rsp_[p2_[1]]))
        p1 = minus_1(p1_1, p1_2)
        
        print("사용자:{}\n컴퓨터:{}".format(rsp_[p1], rsp_[p2]))
        p1_score, p2_score = output_rsp(rsp(p1, p2), p1_score, p2_score)
        if p1_score >= 3 or p2_score >= 3:
            break

    if(p1_score >=3):
        print("사용자 승리!")
    elif(p2_score >=3):
        print("컴퓨터 승리!")
play()
