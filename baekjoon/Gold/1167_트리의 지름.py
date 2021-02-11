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


v = int(input())
nodes = [[] for _ in range(v+1)]
for _ in range(v):
    line = list(map(int, input().split()))
    num = 1

    while line[num] != -1:
        nodes[line[0]].append((line[num],line[num+1]))
        num += 2

node1 = [0] * (v+1)
dfs(1,nodes, node1)
node1[1] = 0

max_idx = node1.index(max(node1))

node2 = [0] * (v+1)
dfs(max_idx, nodes, node2)
node2[max_idx] = 0
print(max(node2))