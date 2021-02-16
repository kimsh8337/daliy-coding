n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

from collections import deque

def bfs(v, visited, nodes):
    cnt = 0
    q = deque()
    q.append((v,cnt))

    while q:
        a, b = q.popleft()
        if visited[a] == -1:
            visited[a] = b
            b += 1
            for e in nodes[a]:
                q.append((e,b))

def solution(n, edge):
    answer = 0
    nodes = [[] for _ in range(n+1)]
    for i in range(len(edge)):
        nodes[edge[i][0]].append(edge[i][1])
        nodes[edge[i][1]].append(edge[i][0])
    visited = [-1] * (n+1)
    bfs(1, visited, nodes)
    for j in visited:
        if j == max(visited):
            answer += 1

    return answer

print(solution(n,vertex))