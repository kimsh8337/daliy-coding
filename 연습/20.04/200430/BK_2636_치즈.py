import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
cnt, time = 0, 0
q = deque()

while 1:
    nxt = []
    q.append((0,0))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<m and 0<=nc<n:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = -1
                    q.append((nr,nc))
                if arr[nr][nc] == 1:
                    arr[nr][nc] = -1
                    nxt.append((nr,nc))

    if not nxt:
        break

    time += 1
    cnt = len(nxt)
    for i in range(m):
        for j in range(n):
            if arr[i][j] == -1:
                arr[i][j] = 0

print(time)
print(cnt)