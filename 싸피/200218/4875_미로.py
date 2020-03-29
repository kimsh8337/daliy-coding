import sys
sys.stdin = open('input.txt','r')

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c):
    global ans
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr>=N or nc < 0 or nc >= N:
            continue
        if maze[nr][nc] == 0 or maze[nr][nc] ==3:
            if maze[nr][nc] == 3:
                ans = 1
                return
            maze[nr][nc] = 1
            dfs(nr, nc)

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i
                sC = j
                break

    dfs(sR, sC)
    print("#{} {}".format(tc, ans))
