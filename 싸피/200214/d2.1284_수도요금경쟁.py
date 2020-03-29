import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    p,q,r,s,w = map(int, input().split())

    a_res = p*w
    if (w-r) > 0:
        b_res = q + (w-r)*s
    else:
        b_res = q

    if a_res < b_res:
        ans = a_res
    else:
        ans = b_res
    print('#{} {}'.format(tc, ans))