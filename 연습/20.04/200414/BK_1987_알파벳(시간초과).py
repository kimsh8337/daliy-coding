import sys
sys.stdin = open('input.txt','r')

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def dfs(r=0,c=0,cnt=0):
    global ans
    if arr[r][c] in li:
        ans = max(ans,cnt)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<a and 0<=nc<b and visited[nr][nc]==0:
            visited[r][c] = 1
            li.append(arr[r][c])
            dfs(nr,nc,cnt+1)
            visited[nr][nc] = 0
            li.pop()

a, b = map(int, input().split())
arr = [list(input()) for _ in range(a)]
visited = [[0]*b for _ in range(a)]
li = []
ans = 0
dfs()
print(ans)