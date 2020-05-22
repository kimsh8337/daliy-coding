import sys
sys.stdin = open('input2660.txt', 'r')
from _collections import deque

N = int(input())
G = [[0]*(N+1) for _ in range(N+1)]

while 1:
    r,c = map(int, input().split())
    if r == -1: break
    G[r][c] = 1
    G[c][r] = 1

def bfs(V):
    q = deque()
    q.append(V)
    visit = [0]*(N+1)
    D = [0] * (N+1)

    while q:
        r = q.popleft()
        visit[r] = 1

        for c in range(N+1):
            if G[r][c] == 1 and visit[c] == 0:
                visit[c] = 1
                D[c] = D[r] + 1
                q.append(c)
    return D

leader_list = [0]
minV = float('inf')

for i in range(1, N+1):
    ans = bfs(i)
    leader_list.append(max(ans))
    minV = min(minV, max(ans))

print(minV, leader_list.count(minV))
for leader,value in enumerate(leader_list):
    if value == minV:
        print(leader, end=' ')