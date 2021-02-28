import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

def bfs():
    global cnt, min_time

    q = deque()
    q.append((N,0))
    visited[N] = 1

    while q:
        now, time = q.popleft()

        if min_time >= time:
            if now == K:
                if min_time >= time:
                    min_time = time
                    cnt += 1

            if not visited[now+1] and min_time >= time:
                visited[now+1] = 1
                q.append((now+1,time+1))
            if not visited[now-1] and min_time >= time:
                visited[now - 1] = 1
                q.append((now-1,time+1))
            if now*2 <= 1000000 and min_time >= time:
                if not visited[now*2]:
                    visited[now*2] = 1
                    q.append((now*2,time+1))


N, K = map(int, input().split())
visited = [0]*1000000
cnt = 0
min_time = float('inf')
bfs()
print(min_time)
print(cnt)