import sys
sys.stdin = open('input.txt','r')
from _collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = float('inf')
res = 0
q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            q.append((i,j,0))

            while q:
                r,c,cnt = q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                        if arr[nr][nc] == 1:
                            visited[nr][nc] = 1
                            q.append((nr,nc,0))
                        else:
                            visited[nr][nc] = 1
                            q.append((nr,nc,cnt+1))
                            res = cnt + 1
                            # print(cnt)
            ans = min(ans, res)
print(ans)