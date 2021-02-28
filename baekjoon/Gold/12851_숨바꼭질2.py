import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

def bfs():
    global cnt

    q = deque()
    q.append((N,0))

    while q:
        now, time = q.popleft()
        if now == K:
            if not visited[now]:
                visited[now] = time
                cnt += 1
            else:
                if time == visited[now]:
                    cnt += 1

        for nxt in [now*2, now+1, now-1]:
            if 0 <= nxt <= 1000000:
                if not visited[nxt] or visited[nxt] >= time+1:
                    if visited[K] and time+1 > visited[nxt]:
                        continue
                    visited[nxt] = time + 1
                    q.append((nxt,time+1))


N, K = map(int, input().split())
visited = [0]*1000001
cnt = 0
if N >= K:
    print(N-K)
    print(1)
else:
    bfs()
    print(visited[K])
    print(cnt)