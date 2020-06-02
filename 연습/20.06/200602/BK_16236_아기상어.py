import sys
sys.stdin = open('input16236.txt', 'r')
from _collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]


def bfs(r,c):
    Q = deque()
    Q.append((r,c,2,0))
    visit[r][c] = 1
    cnt = 0

    while Q:
        rr, cc, size, time = Q.popleft()

        for i in range(4):
            nr = rr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<n and 0<=nc<n and not visit[nr][nc]:
                if arr[nr][nc] < size and arr[nr][nc] != 0:
                    visit[nr][nc] = 1
                    cnt += 1
                    if cnt == size:
                        size += 1
                        cnt = 0
                    Q.append((nr,nc,size,time + 1))
                elif not arr[nr][nc]:
                    Q.append((nr,nc,size, time + 1))
                else:
                    return time


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            print(bfs(i,j))