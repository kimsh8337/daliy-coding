import sys
sys.stdin = open('input.txt', 'r')

x,y,w,h = map(int, input().split())
dr = [1,0,-1,0]
dc = [0,1,0,-1]
cnt = 1
ans = 987665
square = [[0]*w for _ in range(h)]
square[y-1][x-1] = 1
for i in range(w):
    square[0][i], square[h-1][i] = 2, 2
for i in range(h):
    square[i][0], square[i][w-1] = 2, 2
for i in range(4):
    nr = (y-1) + dr[i]
    nc = (x-1) + dc[i]
    if 0<=nr<h and 0<=nc<w:
        if square[nr][nc]==0:
            square[nr][nc] = 1
            cnt += 1
        elif square[nr][nc] == 2:
            if ans > cnt:
                ans = cnt
print(ans)