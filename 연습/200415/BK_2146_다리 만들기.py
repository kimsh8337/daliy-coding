import sys
sys.stdin = open('input.txt','r')
from _collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs1(r,c,cnt):
    q.append((r,c))
    visited[r][c] = cnt
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<n:
                if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = cnt
                    q.append((nr,nc))


def bfs2(num):
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<n:
                if arr[nr][nc] == 1 and visited[nr][nc] != num:
                    return visited2[r][c] - 1
                if arr[nr][nc] == 0 and visited2[nr][nc] == 0:
                    visited2[nr][nc] = visited2[r][c] + 1
                    q.append((nr,nc))

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = float('inf')
q = deque()
cnt = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            bfs1(i,j,cnt)
            cnt += 1

for k in range(1,cnt):
    q = deque()
    visited2 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and visited[i][j] == k:
                q.append((i,j))
                visited2[i][j] = 1
    res = bfs2(k)
    ans = min(ans,res)
print(ans)
