import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input.txt', 'r')

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def dfs(r,c):
    farm[r][c] = 2

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<n and 0<=nc<m:
            if farm[nr][nc] == 1:
                dfs(nr,nc)
            else:
                continue

for tc in range(1, 1+int(input())):
    m,n,k = map(int, input().split())
    farm = [[0]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int, input().split())
        farm[b][a] = 1
    cnt = 0

    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                dfs(i,j)
                cnt += 1

    print(cnt)
