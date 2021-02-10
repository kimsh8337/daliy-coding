import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(st, nodes, node):
    for nd, w in nodes[st]:
        if node[nd] == 0:
            node[nd] = node[st] + w
            dfs(nd, nodes, node)

    return


n = int(input())
nodes = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, p = map(int, input().split())
    nodes[v].append((u,p))
    nodes[u].append((v,p))

node1 = [0] * (n+1)
dfs(1, nodes, node1)
node1[1] = 0

st_nd = node1.index(max(node1))
node2 = [0] * (n+1)

dfs(st_nd, nodes, node2)
node2[st_nd] = 0

print(max(node2))