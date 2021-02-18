import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def div(now, cnt, pos):
    d = now // cnt

    while pos:
        r,c = pos.popleft()
        con[r][c] = d


def check():
    global now, flag, cnt

    while q:
        r,c = q.popleft()

        for a in range(4):
            nr = r + dr[a]
            nc = c + dc[a]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                dis = abs(con[r][c] - con[nr][nc])
                if L <= dis <=R:
                    flag = True
                    now += con[nr][nc]
                    visited[nr][nc] = now
                    cnt += 1
                    q.append((nr,nc))
                    pos.append((nr,nc))

N, L, R = map(int, input().split())
con = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
q, pos = deque(), deque()
ans = 0
keep = True

while keep:
    go = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                flag = False
                cnt = 1
                q.append((i,j))
                pos.append((i,j))
                now = con[i][j]
                visited[i][j] = now
                check()
                if flag:
                    go = 1
                    div(now,cnt,pos)
                else:
                    pos.popleft()
    if go:
        visited = [[0] * N for _ in range(N)]
        ans += 1
    else:
        break
print(ans)