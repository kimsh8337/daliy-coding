import sys
sys.stdin=open('input.txt','r')
from _collections import deque

dr=[0,1,0,-1]
dc=[1,0,-1,0]

def bfs():
    while Q:
        q=Q.popleft()
        y=q[0]
        x=q[1]
        visit.append(q)
        for i in range(4):
            ny=y+dr[i]
            nx=x+dc[i]
            if 0<=nx<a and 0<=ny<a:
                if visited[ny][nx] ==0:
                    if arr[ny][nx]==0:
                        Q.append((ny,nx))
                        visited[ny][nx]=visited[y][x]+1
                if arr[ny][nx]==3:
                    Q.append((ny, nx))
                    if visited[ny][nx] == 0:
                        visited[ny][nx] = visited[y][x]
                        value=visited[ny][nx]
                    if visited[ny][nx] != 0:
                        if value>visited[y][x]:
                            visited[ny][nx] = visited[y][x]
                        else:
                            visited[ny][nx]=value




t= int(input())

for tc in range(1,t+1):
    a= int(input())
    arr=[]
    for i in range(a):
        _list=list(map(int,input()))
        arr.append(_list)
    # print(arr)

    visited=[[0]*a for _ in range(a)]
    Q=deque()
    visit=[]
    for i in range(a):
        for j in range(a):
            if arr[i][j]==3:
                ii=i
                jj=j
            if arr[i][j]==2:
                visited[i][j]=1
                Q.append((i,j))
                bfs()


    if (ii,jj) not in visit:
        print('#{} {}'.format(tc,0))
    else:
        print('#{} {}'.format(tc,visited[ii][jj]-1))