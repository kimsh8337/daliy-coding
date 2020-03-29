import sys
sys.stdin = open('input.txt', 'r')

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def dfs(visited, v):
    for i in range(0, n):
        cnt = 0
        if farm[v][i] == 1 and i not in visited:
            r,c =
            for k in range(4):
                nr = x+dr[k]
                nc = y+dc[k]

            if 0 <= nr < m and 0 <= nc < n and farm[nr][nc] == 1:
                visited.append(i)
                dfs(visited, i)

T = int(input())

for tc in range(1, T+1):
    m,n,k = map(int, input().split())
    farm = [[0]*n for _ in range(m)]
    # print(farm)
    for i in range(k):
        x,y = map(int, input().split())
        farm[x][y] = 1

print('{} {}'.format(tc, dfs([x],x)))