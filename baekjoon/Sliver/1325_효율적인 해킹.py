import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(i):
    cnt = 0
    q = deque()
    q.append(i)
    visit = [0] * (n+1)
    visit[i] = 1
    while q:
        a = q.popleft()
        cnt += 1

        for w in com[a]:
            if not visit[w]:
                visit[w] = 1
                q.append(w)

    return cnt


n, m = map(int, sys.stdin.readline().split())
com = [[] for _ in range(n+1)]
mxd = 0
res = []

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    com[v].append(u)

for i in range(1,n+1):
    if com[i]:
        tmp = bfs(i)
        if mxd <= tmp:
            if mxd < tmp:
                res = []
            mxd = tmp
            res.append(i)

print(*res)