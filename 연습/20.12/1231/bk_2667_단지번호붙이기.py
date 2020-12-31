import sys
sys.stdin = open('input2667.txt', 'r')

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def dfs(r,c):
    global cnt

    cnt += 1
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<n and 0<=nc<n:
            if home[nr][nc] == 1 and visited[nr][nc] == 0:
                dfs(nr,nc)

n = int(input())
home = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
group = []

for i in range(n):
    for j in range(n):
        if home[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i,j)
            group.append(cnt)

print(len(group))
group.sort()
for i in range(len(group)):
    print(group[i])
