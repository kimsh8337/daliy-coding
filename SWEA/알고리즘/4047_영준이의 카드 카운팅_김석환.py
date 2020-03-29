# 내가 짠 코드
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,1+int(input())):
    card = list(input())
    cnt_list=[13]*4
    flag = True
    print('#{}'.format(tc), end = ' ')
    for i in range(0,len(card),3):
        for j in range(i+3,len(card),3):
            a = card[i]+card[i+1]+card[i+2]
            b = card[j]+card[j+1]+card[j+2]
            if a == b:
                flag = False
                break
        if card[i] == 'S':
            cnt_list[0] -= 1
        elif card[i] == 'D':
            cnt_list[1] -= 1
        elif card[i] == 'H':
            cnt_list[2] -= 1
        elif card[i] == 'C':
            cnt_list[3] -= 1

    if flag:
        for i in range(4):
            print(cnt_list[i], end = ' ')
        print()
    else:
        print('ERROR')

# T = int(input())
#
# for tc in range(1, T+1):
#     card = list(input())
#     s=[0]*(len(card)//3)
#
#     s_cnt = 13
#     d_cnt = 13
#     h_cnt = 13
#     c_cnt = 13
#     flag = False
#     idx = 0
#     for i in range(0, len(card), 3):
#         s[idx] = card[i] + card[i + 1] + card[i + 2]
#         idx += 1
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             if s[i] == s[j]:
#                 print('#{} ERROR'.format(tc))
#                 flag = True
#                 break
#     for j in range(0,len(card),3):
#         if card[j] == 'S':
#             s_cnt -= 1
#     for j in range(0, len(card), 3):
#         if card[j] == 'D':
#             d_cnt -= 1
#     for j in range(0,len(card),3):
#         if card[j] == 'H':
#             h_cnt -= 1
#     for j in range(0,len(card),3):
#         if card[j] == 'C':
#             c_cnt -= 1
#     if flag == False:
#         print('#{} {} {} {} {}'.format(tc, s_cnt, d_cnt, h_cnt, c_cnt))

    # res = ''
    # if s[0] == s[1] or s[0] == s[2] or s[0] == s[3]:
    #      res = 'ERROR'
    #     print('#{} {}'.format(tc, res))
    # # print(s)
    # # print(s_cnt, d_cnt, h_cnt, c_cnt)

# 해설
# T = int(input())
# pattern = {'S':0, 'D':1, 'H':2, 'C':3}
#
# for tc in range(1,T+1):
#     line =input()
#
#     card = [[0]*14 for _ in range(4)]
#
#     flag = True
#     for i in range(0, len(line), 3):
#         card_pattern = pattern[line[i]]
#         card_num = int(line[i+1:i+3])
#         if card[card_pattern][card_num] == 1:
#             flag = False
#             break
#         card[card_pattern][card_num] = 1
#         card[card_pattern][0] += 1
#
#     print('#{}'.format(tc), end = ' ')
#     if flag:
#         for i in range(4):
#             print('{}'.format(13 - card[i][0]), end = ' ')
#         print()
#     else:
#         print('ERROR')