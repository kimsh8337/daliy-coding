import sys
sys.setrecursionlimit(10**5)

from collections import deque
import copy

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs():
    global lab2

    while Q:
        r,c = Q.popleft()

        for e in range(4):
            nr = r + dr[e]
            nc = c + dc[e]
            if 0<=nr<n and 0<=nc<m and lab2[nr][nc] == 0:
                lab2[nr][nc] = 2
                Q.append((nr,nc))
                bfs()
    return

def dfs(r,c):
    global wall, lab2, rooms

    lab[r][c] = 3
    wall -= 1

    if wall == 0:
        lab2 = copy.deepcopy(lab)
        for q in range(n):
            for p in range(m):
                if lab2[q][p] == 2:
                    Q.append((q,p))
                    bfs()

        cnt = 0
        for x in range(n):
            for y in range(m):
                if lab2[x][y] == 0:
                    cnt += 1
        if rooms < cnt:
            rooms = cnt
            return
        return

    for a in range(n):
        for b in range(m):
            if lab[a][b] == 0:
                dfs(a,b)
                lab[a][b] = 0
                wall += 1


n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lab2 = []
rooms = 0
Q = deque()
wall = 3

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            dfs(i,j)
            lab[i][j] = 0
            wall += 1

print(rooms)