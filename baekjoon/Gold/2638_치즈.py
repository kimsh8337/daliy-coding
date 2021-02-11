import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def check():
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1:
                return False
    return True

def dfs(r,c):
    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
            if cheese[nr][nc] != 0:
                cheese[nr][nc] += 1
            else:
                visited[nr][nc] = 1
                dfs(nr,nc)

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
res = 0

while 1:
    if check():
        print(res)
        break

    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    dfs(0,0)

    for i in range(N):
        for j in range(M):
            if cheese[i][j] >= 3:
                cheese[i][j]= 0
            elif cheese[i][j] > 0:
                cheese[i][j] = 1
    res += 1