import sys
sys.stdin = open('input.txt','r')
from _collections import deque

v = int(input())
e = int(input())
li = []
for _ in range(e):
    a,b = map(int, input().split())
    li.append((a,b))
Q = deque()
visit = []
visited = [0]*(v+1)
Q.append(1)
visited[1] = 1

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
print(len(visit) - 1)
