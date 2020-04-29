import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs():
    global ans

    while q:
        r, c, cnt = q.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0<=nr<n and 0<=nc<m:
                if visited[nr][nc] == 1 or arr[nr][nc] == -1: continue
                visited[nr][nc] = arr[nr][nc] = 1
                q.append((nr,nc,cnt+1))
                ans = cnt + 1
    for i in arr:
        if 0 in i:
            return -1
    else:
        return ans

m,n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans = 0
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j, 0))
            visited[i][j] = 1
print(bfs())