import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def BFS():
    while Q:
        u, v = Q.popleft()

        for i in range(m):
            if not visited[i]:
                if u == nodes[i][0] or u == nodes[i][1]:
                    visited[i] = 1
                    Q.append((nodes[i][0], nodes[i][1]))
                elif v == nodes[i][0] or v == nodes[i][1]:
                    visited[i] = 1
                    Q.append((nodes[i][0], nodes[i][1]))


n, m = map(int,sys.stdin.readline().split())
nodes = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
visited = [0] * m
cnt = 0
Q = deque()

for i in range(m):
    if not visited[i]:
        Q.append((nodes[i][0], nodes[i][1]))
        visited[i] = 1
        BFS()
        cnt += 1
print(cnt)
