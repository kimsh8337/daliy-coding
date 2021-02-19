import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

from collections import deque

def bfs():
    while q:
        now, cnt = q.popleft()

        if now == K:
            print(cnt)
            return

        if 0<=(now*2)<l and not visited[now*2]:
            q.appendleft((now*2,cnt))
            visited[now*2] = 1
        if 0<=(now+1)<l and not visited[now+1]:
            q.append((now+1,cnt+1))
            visited[now+1] = 1
        if 0<=(now-1)<l and not visited[now-1]:
            q.append((now-1, cnt+1))
            visited[now-1] = 1


N, K = map(int, input().split())
visited = [0]*100001
l = len(visited)
q = deque()
q.append((N,0))
visited[N] = 1
bfs()