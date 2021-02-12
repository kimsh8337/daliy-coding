import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def dfs(r,c):
    global cnt,now

    now += 1
    visited[r][c] = 1

    if arr[r][c] > cnt:
        cnt = arr[r][c]

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0<=nr<n and 0<=nc<m and arr[nr][nc] == 1 and not visited[nr][nc]:
            arr[nr][nc] += now
            dfs(nr,nc)
    return arr[r][c]

n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
visited = [[0]*m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            now = 0
            dfs(i,j)
print(cnt)
