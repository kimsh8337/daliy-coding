import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

def bfs():
    global cnt

    q = deque()
    for i in friends[1]:
        q.append((1,i))
    visited[1] = 1

    while q:
        x, y = q.popleft()
        if not visited[y]:
            visited[y] = 1
            cnt += 1
        else:
            continue

        if x == 1:
            for j in friends[y]:
                if not visited[j]:
                    q.append((y,j))

    return

n = int(input())
m = int(input())
friends = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
visited = [0] * (n+1)
cnt = 0


bfs()

print(cnt)