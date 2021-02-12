import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def dfs(r,c):
    global w

    visited[r][c] = 1
    w += 1

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and arr[nr][nc] == 1:
            dfs(nr,nc)
    return


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
cnt = 0
width = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            w = 0
            dfs(i,j)
            width = max(width, w)
            cnt += 1
print(cnt)
print(width)