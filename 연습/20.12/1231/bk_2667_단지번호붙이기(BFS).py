import sys
sys.stdin = open('input2667.txt', 'r')

from _collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs(r,c):
    global cnt
    Q = deque()
    Q.append((r,c))
    visited[r][c] = 1
    cnt += 1

    while Q:
        x,y = Q.popleft()

        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]
            if 0<=nr<n and 0<=nc<n:
                if home[nr][nc] == 1 and visited[nr][nc] == 0:
                    cnt += 1
                    visited[nr][nc] = 1
                    Q.append((nr,nc))


n = int(input())
home = [list(map(int, input())) for _ in range(n)]
visited = [[0] *n for _ in range(n)]
group = []

for i in range(n):
    for j in range(n):
        if home[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            bfs(i,j)
            group.append(cnt)

print(len(group))
group.sort()
for i in range(len(group)):
    print(group[i])