import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**5)

dr = [1,0,-1,0]
dc = [0,1,0,-1]


def DFS(r,c):
    if memo[r][c]:
        return memo[r][c]
    memo[r][c] = 1

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0<=nr<n and 0<=nc<n:
            if forest[nr][nc] > forest[r][c]:
                memo[r][c] = max(memo[r][c], DFS(nr,nc)+1)
    return memo[r][c]


n = int(input())
forest = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
memo = [[0]*n for _ in range(n)]
day = 0

for i in range(n):
    for j in range(n):
        day = max(day,DFS(i,j))
print(day)

