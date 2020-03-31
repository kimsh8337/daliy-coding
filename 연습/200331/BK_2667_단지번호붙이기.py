import sys
sys.stdin = open('input.txt', 'r')

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def dfs(r,c):
    global cnt

    cnt += 1
    arr[r][c] = 2

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<n and 0<=nc<n:
            if arr[nr][nc] == 1:
                dfs(nr,nc)

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
li_cnt = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i,j)
            li_cnt.append(cnt)

li_cnt.sort()
print(len(li_cnt))
for i in range(len(li_cnt)):
    print(li_cnt[i])

