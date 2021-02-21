import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs():
    global flag, sheep, wolf

    while q:
        r, c = q.popleft()

        if sheep > wolf:
            flag = True
        else:
            flag = False

        for a in range(4):
            nr = r + dr[a]
            nc = c + dc[a]
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc]:
                if arr[nr][nc] == 'v':
                    q.append((nr,nc))
                    wolf += 1
                    visited[nr][nc] = 1
                elif arr[nr][nc] == 'o':
                    q.append((nr,nc))
                    sheep += 1
                    visited[nr][nc] = 1
                elif arr[nr][nc] == '.':
                    q.append((nr,nc))
                    visited[nr][nc] = 1



R, C = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
q = deque()
flag = True
sheep = 0
wolf = 0
s_cnt = 0
w_cnt = 0

for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            if arr[i][j] == '.':
                continue
            elif arr[i][j] == '#':
                continue
            elif arr[i][j] == 'v':
                q.append((i,j))
                visited[i][j] = 1
                wolf += 1
                bfs()
            elif arr[i][j] == 'o':
                q.append((i,j))
                visited[i][j] = 1
                sheep += 1
                bfs()
            if flag:
                s_cnt += sheep
                sheep,wolf = 0,0
            else:
                w_cnt += wolf
                sheep, wolf = 0, 0
print(s_cnt, w_cnt)

