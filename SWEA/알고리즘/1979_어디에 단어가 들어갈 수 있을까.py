import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    # arr = [[int(x) for x in input().split()] for _ in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 가로 확인
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if k == cnt:
                    ans += 1
                cnt = 0
        if k == cnt:
            ans += 1


    # 세로 확인
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if k == cnt:
                    ans += 1
                cnt = 0
        if k == cnt:
            ans += 1


    print('#{} {}'.format(tc, ans))