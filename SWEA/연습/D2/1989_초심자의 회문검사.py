import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    s_list = list(map(str, input()))
    n = len(s_list)//2
    flag = True
    for i in range(n):
        for j in range(-i-1,-i-2,-1):
            if s_list[i] == s_list[j]:
                flag = True
            else:
                flag = False
    print('#{}'.format(tc), end = ' ')
    if flag:
        print(1)
    else:
        print(0)