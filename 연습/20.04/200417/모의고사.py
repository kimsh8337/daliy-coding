import sys
sys.stdin = open('input.txt','r')

dc = [-1, 0, 1, -1, 1, -1, 0, 1]
dr = [-1, -1, -1, 0, 0, 1, 1, 1]

def dfs(r, c):
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<10 and 0<=nc<10:
            if arr[nr][nc] == 1:
                arr[nr][nc] = 2
                dfs(nr, nc)

for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(10)]
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print('#{} {}'.format(tc, cnt))