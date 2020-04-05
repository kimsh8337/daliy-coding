import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]
for tc in range(1, int(input())):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    Q = deque()
    visit = []
    visited = [[0]*w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                Q.append((i,j))
                visited[i][j] = 1

                while Q:
                    q = Q.popleft()
                    visit.append((q[0],q[1]))

                    for k in range(4):
                        nr = q[0] + dr[k]
                        nc = q[1] + dc[k]
                        if 0<=nr<h and 0<=nc<w:
                            if visited[nr][nc] == 0:
                                if building[nr][nc] == '.':
                                    visited[nr][nc] = visited[q[0]][q[1]] + 1
                                    Q.append((nr,nc))
                            if building[nr][nc] == '*':
                                for p in range(4):
                                    r = nr + dr[p]
                                    c = nc + dc[p]
                                    if building[r][c] != '#':
                                        building[r][c] = '*'

    for i in range(h):
        if i == 0 or i == (h-1):
            for j in range(w):
                if building[i][j] == '.':
                    if visited[i][j] == 0:
                        print('IMPOSSIBLE')
                    else:
                        print(visited[i][j])
        else:
            for j in range(w):
                if j == 0 or j == (w-1):
                    if building[i][j] == '.':
                        if visited[i][j] == 0:
                            print('IMPOSSIBLE')
                        else:
                            print(visited[i][j])
