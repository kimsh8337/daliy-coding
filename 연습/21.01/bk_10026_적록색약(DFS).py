import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**5)

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def DFS(r,c, color):
    visited[r][c] = 1

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
            if sector[nr][nc] == color:
                DFS(nr, nc, color)
    return

def DFS2(r,c,color):
    visited2[r][c] = 1

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0 <= nr < n and 0 <= nc < n and not visited2[nr][nc]:
            if color == 'B' and sector[nr][nc] == 'B':
                DFS2(nr, nc, color)
            elif color != 'B' and sector[nr][nc] != 'B':
                DFS2(nr, nc, color)
    return

n = int(input())
sector = [list(map(str,input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
visited2 = [[0]*n for _ in range(n)]
cnt, non = 0,0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            DFS(i,j, sector[i][j])
            cnt += 1
        if not visited2[i][j]:
            DFS2(i,j, sector[i][j])
            non += 1

print(cnt, non)