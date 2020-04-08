import sys
sys.stdin = open('input.txt','r')
from _collections import deque

rc = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs():
    global ans
    while q:
        r,c,k = q.popleft()
        for i in range(4):
            nr = r + rc[i][0]
            nc = c + rc[i][1]
            if 0<=nr<h and 0<=nc<w:
                if arr[nr][nc] == 'L' and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr,nc,k+1))
                    ans = k+1
    return ans

h,w = map(int, input().split())
arr = [list(input()) for _ in range(h)]
visited = [[0]*w for _ in range(h)]
q = deque()
ans = 0

for i in range(h):
    for j in range(w):
        if arr[i][j] == 'L':
            q.append((i,j,0))
print(bfs())