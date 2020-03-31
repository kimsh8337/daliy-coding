import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input.txt', 'r')

dr=[1,0,-1,0]
dc=[0,1,0,-1]

def dfs(r,c):
    global cnt
    arr[r][c] = 1
    cnt += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<m and 0<=nc<n:
            if arr[nr][nc] == 0:
                dfs(nr,nc)

m,n,k = map(int, input().split())
arr = [[0]*n for _ in range(m)]
for _ in range(k):
    a,b,c,d = map(int,input().split())
    if (m-b)< (m-d):
        for i in range(m-b,m-d):
            for j in range(a,c):
                arr[i][j] = 1
    else:
        for i in range(m-d,m-b):
            for j in range(a,c):
                arr[i][j] = 1
# print(arr)
li_cnt =[]
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            cnt = 0
            dfs(i,j)
            li_cnt.append(cnt)

print(len(li_cnt))
li_cnt.sort()
for i in range(len(li_cnt)):
    print(li_cnt[i],end = ' ')