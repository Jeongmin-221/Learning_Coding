login = {
    'leesam0044' : '1234567',
    'leesam0022' : '11223344'
    }

id = input("아이디:")
pw = input("패스워드:")
if login[id] == pw:
    print("로그인 성공!")
else:
    print("로그인 실패!")
