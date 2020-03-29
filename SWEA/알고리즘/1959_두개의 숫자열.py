import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = []

    if N < M:
        for j in range(M-N+1):
            add = 0
            for i in range(N):
                c = a[i] * b[i+j]
                add += c
            ans.append(add)

    if N > M:
        for i in range(N-M+1):
            add = 0
            for j in range(M):
                c = a[i+j] * b[j]
                add += c
            ans.append(add)
    print('#{} {}'.format(tc, max(ans)))