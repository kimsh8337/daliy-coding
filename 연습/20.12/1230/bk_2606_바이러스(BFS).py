import sys
sys.stdin = open('input2606.txt', 'r')

from _collections import deque

n = int(input())
k = int(input())
network = []

for i in range(k):
    a,b = map(int, input().split())
    network.append((a,b))

Q = deque()
visit = []
visited = [0] * (n+1)
Q.append(1)
visited[1] = 1

while Q:
    q = Q.popleft()
    visit.append(q)

    for i in range(k):
        if network[i][0] == q:
            if visited[network[i][1]] == 0:
                Q.append(network[i][1])
                visited[network[i][1]] = visited[q] + 1
        elif network[i][1] == q:
            if visited[network[i][0]] == 0:
                Q.append(network[i][0])
                visited[network[i][0]] = visited[q] + 1

print(len(visit)-1)