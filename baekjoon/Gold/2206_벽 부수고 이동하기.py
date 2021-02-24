import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1

    while q:
        r, c, bk = q.popleft()

        if r == N-1 and c == M-1:
            cnt = visited[bk][r][c]
            return cnt

        for a in range(4):
            nr = r + dr[a]
            nc = c + dc[a]
            if 0<=nr<N and 0<=nc<M and not visited[bk][nr][nc]:
                if arr[nr][nc] == 0:
                    q.append((nr,nc,bk))
                    visited[bk][nr][nc] = visited[bk][r][c] + 1
                if arr[nr][nc] == 1 and bk == 0:
                    q.append((nr,nc,1))
                    visited[1][nr][nc] = visited[bk][r][c] + 1

    return -1


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
print(bfs())