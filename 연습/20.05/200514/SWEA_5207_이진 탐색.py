import sys
sys.stdin = open('input.txt', 'r')

def binary_search(l, r, n):
    r_flag = False
    l_flag = False
    while l <= r:
        mid = (l + r) // 2
        if a_li[mid] == n:
            return 1
        elif a_li[mid] > n:
            if r_flag:
                return 0
            else:
                r = mid - 1
                l_flag = False
                r_flag = True
        elif a_li[mid] < n:
            if l_flag:
                return 0
            else:
                l = mid + 1
                l_flag = True
                r_flag = False
    return 0


T = int(input())
for TC in range(1, T + 1):
    N, M = map(int, input().split())

    a_li = sorted(list(map(int, input().split())))
    b_li = list(map(int, input().split()))
    b_cnt = 0
    for i in range(M):
        b_cnt += binary_search(0, N - 1, b_li[i])
    print('#{} {}'.format(TC, b_cnt))