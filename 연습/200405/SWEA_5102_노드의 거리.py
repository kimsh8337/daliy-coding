import sys
sys.stdin = open('input.txt','r')
from _collections import deque

for tc in range(1, 1+int(input())):
    v,e = map(int, input().split())
    li = []
    for i in range(e):
        a,b = map(int,input().split())
        li.append((a,b))
    m,n = map(int, input().split())
    # print(li)
    Q = deque()
    visit = []
    visited = [0] * (v+1)
    Q.append(m)
    visited[m] = 1
    while Q:
        q = Q.popleft()
        visit.append(q)

        for i in range(e):
            if li[i][0] == q:
                if visited[li[i][1]] == 0:
                    Q.append(li[i][1])
                    visited[li[i][1]] = visited[q] + 1
            elif li[i][1] == q:
                if visited[li[i][0]] == 0:
                    Q.append(li[i][0])
                    visited[li[i][0]] = visited[q] + 1

    print('#{}'.format(tc),end = ' ')
    if visited[n] == 0:
        print(0)
    else:
        print('{}'.format(visited[n]-1))