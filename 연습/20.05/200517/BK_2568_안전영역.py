import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input2468.txt','r')

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def dfs(r,c):
    global cnt
    cnt += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<n and 0<=nc<n:
            if visit[nr][nc] or sample[nr][nc] == 0: continue
            visit[nr][nc] = 1
            dfs(nr,nc)
            if cnt != 0:
                res.append(cnt)
            cnt = 0


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = 0
for i in range(n):
    for j in range(n):
        m = max(m, arr[i][j])
max_cnt = -float('inf')
for k in range(1,m):
    visit = [[0]*n for _ in range(n)]
    res = []
    sample = arr
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= k:
                sample[i][j] = 0
    for i in range(n):
        for j in range(n):
            if sample[i][j] != 0:
                visit[i][j] = 1
                dfs(i,j)

    max_cnt = max(max_cnt,len(res))
print(max_cnt)