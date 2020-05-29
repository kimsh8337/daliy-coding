import sys
sys.stdin = open('input1600.txt', 'r')
from _collections import deque

h_move = [(1, -2), (1, 2), (2, -1), (2, 1), (-1, -2), (-1, 2), (-2, -1), (-2, 1)]
m_move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    Q = deque()
    Q.append((0, 0, 0))
    visit[0][0][0] = 1

    while Q:
        r, c, cnt = Q.popleft()

        if r == h - 1 and c == w - 1:
            return visit[cnt][r][c] - 1

        if cnt < k:
            for j in range(8):
                nr = r + h_move[j][0]
                nc = c + h_move[j][1]
                if 0 <= nr < h and 0 <= nc < w and not arr[nr][nc] and not visit[cnt+1][nr][nc]:
                    visit[cnt+1][nr][nc] = visit[cnt][r][c] + 1
                    Q.append((nr, nc, cnt + 1))

        for j in range(4):
            nr = r + m_move[j][0]
            nc = c + m_move[j][1]
            if 0 <= nr < h and 0 <= nc < w and not arr[nr][nc] and not visit[cnt][nr][nc]:
                visit[cnt][nr][nc] = visit[cnt][r][c] + 1
                Q.append((nr, nc, cnt))
    return -1


k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
visit = [[[0] * w for _ in range(h)] for _ in range(k+1)]
print(bfs())

# visit = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]
# print(visit)
