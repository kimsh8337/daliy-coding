import sys
sys.stdin = open('input.txt')
from _collections import deque
nd = [(0,1),(0,-1),(1,0),(-1,0)]
def BFS():
    global ans
    while q:
        r,c,k = q.popleft()
        for d in range(4):
            nr = r + nd[d][0]
            nc = c + nd[d][1]
            if 0<=nr<N and 0<=nc<M and tomato[nr][nc]==0 and not check[nr][nc]:
                tomato[nr][nc] = check[nr][nc] = 1
                q.append((nr,nc,k+1))
                ans = k+1
    for i in tomato:
        if 0 in i:
            return -1
    else:
        return ans
M,N = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]
ans = 0
q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:
            q.append((i,j,0))

print(BFS())