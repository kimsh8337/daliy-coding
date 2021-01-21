import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**5)

dr = [1,0,-1,0,1,1,-1,-1]
dc = [0,1,0,-1,1,-1,1,-1]

def find(r,c):
    for a in range(8):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0<=nr<h and 0<=nc<w and visited[nr][nc] == 0 and arr[nr][nc] == 1:
            visited[nr][nc] = 1
            find(nr,nc)
    return

while 1:
    w,h = map(int,input().split())

    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                find(i,j)
                cnt += 1
    print(cnt)

