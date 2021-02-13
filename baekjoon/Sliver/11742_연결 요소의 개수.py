import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(st, cy):
    visited[st] = 1

    for a in nodes[st]:
        if not visited[a]:
            dfs(a, cy)
    return

n, m = map(int, input().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)
visited = [0] * (n+1)
cnt = 0

for i in range(1,n+1):
    if not visited[i]:
        dfs(i,i)
        cnt += 1
print(cnt)