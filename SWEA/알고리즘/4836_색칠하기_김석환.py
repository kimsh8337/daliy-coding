def paint(r1, c1, r2, c2, color):
    cnt = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            arr[i][j] += color
            if arr[i][j] == 3:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*10 for _ in range(10)]
    ans = 0

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        ans += paint(r1, c1, r2, c2, color)

    print('#{} {}'.format(tc, ans))
