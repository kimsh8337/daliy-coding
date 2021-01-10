n = 3
computers = [[1,1,0], [1,1,0], [0,0,1]]

from _collections import deque

def solution(n, computers):
    answer = 0
    Q = deque()
    visited = [0] * n

    while 0 in visited:
        x = visited.index(0)
        Q.append(x)
        visited[x] = 1

        while Q:
            q = Q.popleft()
            for i in range(n):
                if visited[i] == 0 and computers[q][i] == 1:
                    Q.append(i)
                    visited[i] = 1
        answer += 1

    return answer

print(solution(n, computers))