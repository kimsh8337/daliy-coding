import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

for tc in range(1,1+int(input())):
    n = int(input())
    miro = [list(map(int,input())) for _ in range(n)]
    Q = deque()
    visit = []
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                Q.append((i,j))
                visited[i][j] = 1

                while Q:
                    q = Q.popleft()
                    visit.append((q[0],q[1]))

                    for k in range(4):
                        nr = q[0] + dr[k]
                        nc = q[1] + dc[k]
                        if 0<=nr<n and 0<=nc<n:
                            if visited[nr][nc] == 0:
                                if miro[nr][nc] == 0:
                                    visited[nr][nc] = visited[q[0]][q[1]] + 1
                                    Q.append((nr,nc))
                                if miro[nr][nc] == 3:
                                    visited[nr][nc] = visited[q[0]][q[1]] + 1
                                    Q.append((nr, nc))

    print('#{}'.format(tc), end = ' ')
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 3:
                if visited[i][j] == 0:
                    print(visited[i][j])
                else:
                    print(visited[i][j]-2)

