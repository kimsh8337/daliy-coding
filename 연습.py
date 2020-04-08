import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

rc = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs():
    global ans
    while q:
        r,c,k = q.popleft()
        for i in range(4):
            nr = r + rc[i][0]
            nc = c + rc[i][1]
            if 0<=nr<n and 0<=nc<m:
                if tomato[nr][nc] == 0 and check[nr][nc] == 0:
                    tomato[nr][nc] = check[nr][nc] = 1
                    q.append((nr,nc,k+1))
                    ans = k+1
    if 0 in tomato:
        return -1
    else:
        return ans

m,n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]
ans = 0
q = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i,j,0))
print(bfs())