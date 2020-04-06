import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs():
    Q.append((px,py,0))
    visit[px][py]=1
    while Q:
        x,y,z=Q.popleft()
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if tx<0 or tx>=h or ty<0 or ty>=w:
                if z==1:continue
                return visit[x][y]
            if visit[tx][ty] or building[tx][ty]=='#':continue
            visit[tx][ty]=visit[x][y]+1
            Q.append((tx,ty,z))
    return 'IMPOSSIBLE'
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for T in range(int(input())):
    w,h=map(int,input().split())
    building=[list(input()) for _ in range(h)]
    visit=[[0]*w for _ in range(h)]
    Q=deque()
    px=py=0
    for i in range(h):
        for j in range(w):
            if building[i][j]=='*':
                Q.append((i,j,1))
                visit[i][j]=1
            elif building[i][j]=='@':
                px,py=i,j
                building[i][j]='.'
    print(bfs())