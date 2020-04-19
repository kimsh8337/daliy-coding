import sys
from _collections import deque
sys.stdin = open('input.txt','r')

def bfs(a):
    Q.append(a)
    visited[a]=1
    while Q:
        q=Q.popleft()
        visit.append(q)
        for i in range(e):
            if arr[i][0]==q:
                if visited[arr[i][1]]==0:
                    Q.append(arr[i][1])
                    visited[arr[i][1]] =visited[q]+ 1
            elif arr[i][1]==q:
                if visited[arr[i][0]]==0:
                    Q.append(arr[i][0])
                    visited[arr[i][0]] =visited[q]+ 1
    if visited[n]!=0:
        print('#{} {}'.format(tc,visited[n]-1))
    else:
        print('#{} {}'.format(tc, 0))

Q=deque()
t=int(input())
for tc in range(1,t+1):
    v,e=map(int,input().split())
    arr=[]

    visited = [0] * (v + 1)
    visit=[]
    for i in range(e):
        a,b=map(int,input().split())
        arr.append((a,b))
    m, n = map(int, input().split())
    bfs(m)
