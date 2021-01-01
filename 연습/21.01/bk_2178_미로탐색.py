import sys, time
sys.stdin = open('input2178.txt', 'r')

from _collections import deque

start = time.time()

dr = [1,0,-1,0]
dc = [0,1,0,-1]

n,m = map(int,input().split())
miro = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
mincnt = float('inf')

Q = deque()
Q.append((0,0,1))

while Q:
    r,c,cnt = Q.popleft()
    visited[r][c] = 1

    if r == n-1 and c == m-1:
        if mincnt > cnt:
            mincnt = cnt

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<n and 0<=nc<m:
            if miro[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                Q.append((nr,nc,cnt+1))

print(mincnt)
print(time.time() - start)