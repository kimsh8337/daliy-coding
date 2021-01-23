import sys
sys.stdin = open('input.txt' ,'r')
sys.setrecursionlimit(10**5)

def DFS(idx):
    visited[idx] = 1
    for node in nodes[idx]:
        if not visited[node]:
            DFS(node)

    return

n, m = map(int,sys.stdin.readline().split())
nodes = [[] for _ in range(n+1)]
visited = [0]*m
cnt = 0

for _ in range(m):
    u, v = map(int,sys.stdin.readline().split())
    nodes[u].append(v)
    nodes[v].append(u)

for i in range(1,n+1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)