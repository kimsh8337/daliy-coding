import sys
sys.stdin = open('input2178.txt')
from _collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs():
    Q = deque()
    Q.append((0,0))
    visit[0][0] = 1

    while Q:
        r,c = Q.popleft()

        if r==n-1 and c==m-1:
            return visit[r][c]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m and arr[nr][nc] and not visit[nr][nc]:
                # visit[nr][nc] = 1
                visit[nr][nc] = visit[r][c] + 1
                Q.append((nr,nc))


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
print(bfs())