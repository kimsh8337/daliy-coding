import sys
sys.stdin = open('input.txt', 'r')


dr = [1,0,-1,0,1,1,-1,-1]
dc = [0,1,0,-1,1,-1,1,-1]


def find(r,c):
    global cnt

    for a in range(8):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0<=nr<m and 0<=nc<n:
            if sqaure[nr][nc] == '*':
                cnt += 1
    return

m, n = map(int, input().split())
sqaure = [list(map(str, input())) for _ in range(m)]

for i in range(m):
    for j in range(n):
        if sqaure[i][j] == '.':
            cnt = 0
            find(i,j)
            sqaure[i][j] = cnt
        print(sqaure[i][j],end="")
    print()
