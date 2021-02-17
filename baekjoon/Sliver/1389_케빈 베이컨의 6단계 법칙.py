import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

def bfs(r,c):
    q = deque()
    q.append((r,c))

    while q:
        f, cnt = q.popleft()

        if visited[f] == -1:
            visited[f] = cnt
            for ff in friends[f]:
                q.append((ff,cnt+1))



n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
min_cnt = float('inf')
res = 0

for i in range(1,n+1):
    visited = [-1] * (n + 1)
    bfs(i,0)
    h = sum(visited[1:])
    if min_cnt > h:
        min_cnt = h
        res = i
print(res)