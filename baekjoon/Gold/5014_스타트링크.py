import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

def bfs():
    while q:
        st, cnt = q.popleft()

        if st == G:
            print(cnt)
            return

        if U != 0 and (st + U) <= F:
            if not visited[st+U]:
                q.append((st+U, cnt+1))
                visited[st+U] = 1
        if D != 0 and (st - D) >= 1:
            if not visited[st-D]:
                q.append((st-D, cnt+1))
                visited[st-D] = 1

    print('use the stairs')

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)
q = deque()
q.append((S,0))
visited[S] = 1
bfs()