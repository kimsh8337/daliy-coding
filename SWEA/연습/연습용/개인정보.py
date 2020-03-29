num = input()

if len(num)!=11 or num[:3]!='010':
    print('핸드폰번호를 입력하세요')
else:
    print('*'*7+num[7:])