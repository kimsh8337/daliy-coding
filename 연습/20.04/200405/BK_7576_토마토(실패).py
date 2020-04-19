import sys
sys.stdin = open('input.txt','r')
from _collections import deque

m,n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
Q = deque()
visit = []
visited = [[0] * m for _ in range(n)]
unriped = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            Q.append((i,j))
            visited[i][j] = 1
days = 1

while Q:
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    q = Q.popleft()
    visit.append((q[0],q[1]))

    for i in range(4):
        nr = q[0] + dr[i]
        nc = q[1] + dc[i]
        if 0<=nr<n and 0<=nc<m:
            continue
        if box[nr][nc] != 0:
            continue

        box[nr][nc] = box[q[0]][q[1]] + 1
        Q.append((nr,nc))
        days = max(box[nr][nc], days)
        unriped -= 1

if unriped == 0:
    print(days - 1)
else:
    print(-1)

            # if box[nr][nc] != -1:
            #     if visited[nr][nc] == 0:
            #         visited[nr][nc] = visited[q[0]][q[1]] + 1
            #         Q.append((nr,nc))
