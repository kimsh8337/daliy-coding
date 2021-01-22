import sys
sys.stdin = open('input.txt', 'r')

dr = [1,0,-1,0,1,1,-1,-1]
dc = [0,1,0,-1,1,-1,1,-1]

def bfs(r,c):
    arr[i][j] = 0
    Q = [[r,c]]

    while Q:
        y, x = Q[0][0], Q[0][1]
        Q.pop(0)

        for a in range(8):
            ny = y + dr[a]
            nx = x + dc[a]
            if 0<=nx<w and 0<=ny<h and arr[ny][nx] == 1:
                arr[ny][nx] = 0
                Q.append([ny,nx])

while 1:
    w, h = map(int, input().split())

    if w == 0 and h ==0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)