import sys
sys.stdin = open('input1260.txt', 'r')
from _collections import deque


def dfs(V):
    if not visit_d[V]:
        visit_d[V] = 1
        for i in range(1,n+1):
            if D[V][i] and not visit_d[i]:
                res_d.append(i)
                dfs(i)
        return


def bfs():
    Q = deque()
    Q.append(v)
    visit_b[v] = 1

    while Q:
        q = Q.popleft()
        res_b.append(q)

        for i in range(1,n+1):
            if D[q][i] == 1 and not visit_b[i]:
                visit_b[i] = 1
                Q.append(i)

n, m, v = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
D = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    D[arr[i][0]][arr[i][1]] = 1
    D[arr[i][1]][arr[i][0]] = 1
visit_d = [0]*(n+1)
res_d = [v]
dfs(v)
for i in range(len(res_d)):
    print(res_d[i],end=' ')
print()

visit_b = [0]*(n+1)
res_b = []
bfs()
for i in range(len(res_b)):
    print(res_b[i],end=' ')