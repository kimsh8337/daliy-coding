import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(st, nodes, parents):
    for i in nodes[st]:
        if i == 1:
            continue
        elif not parents[i]:
            parents[i] = st
            dfs(i,nodes,parents)
    return

n = int(input())
nodes = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)
parents = [0] * (n+1)

dfs(1,nodes,parents)

for i in range(2,n+1):
    print(parents[i])