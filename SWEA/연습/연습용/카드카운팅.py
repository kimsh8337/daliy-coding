import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T+1):
    card = input()
    s_cnt, d_cnt, h_cnt, c_cnt = 13,13,13,13
    s = [0]*(len(card)//3)
    idx = 0
    flag = True
    for i in range(0,len(card),3):
        s[idx] = card[i] + card[i+1] + card[i+2]
        idx += 1
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                print('#{} ERROR'.format(tc))
                flag = False
                break

    for i in range(0,len(card),3):
        if card[i] == 'S':
            s_cnt -= 1
        elif card[i] == 'D':
            d_cnt -= 1
        elif card[i] == 'H':
            h_cnt -= 1
        elif card[i] == 'C':
            c_cnt -= 1
    print('#{} {} {} {} {}'.format(tc, s_cnt, d_cnt, h_cnt, c_cnt))