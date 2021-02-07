import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs(i,j):
    visit = [[0] * n for _ in range(n)]
    visit[i][j] = 1
    eat = []
    dist = [[0] * n for _ in range(n)]
    q = deque()
    q.append([i,j])

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0<=nr<n and 0<=nc<n and visit[nr][nc] == 0:
                if arr[nr][nc] <= arr[i][j] or arr[nr][nc] == 0:
                    q.append([nr,nc])
                    visit[nr][nc] = 1
                    dist[nr][nc] = dist[r][c] + 1
                if arr[nr][nc] < arr[i][j] and arr[nr][nc] != 0:
                    eat.append([nr, nc, dist[nr][nc]])
    if not eat:
        return -1,-1,-1
    eat.sort(key=lambda x:(x[2],x[0],x[1]))
    return eat[0][0], eat[0][1], eat[0][2]




n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
           arr[i][j] = 2
           start = [i,j]
exp = 0
cnt = 0

while 1:
    i,j = start[0], start[1]
    ex, ey, dist = bfs(i,j)
    if ex == -1:
        break
    arr[ex][ey] = arr[i][j]
    arr[i][j] = 0
    start = [ex,ey]
    exp += 1
    if exp == arr[ex][ey]:
        exp = 0
        arr[ex][ey] += 1
    cnt += dist
print(cnt)