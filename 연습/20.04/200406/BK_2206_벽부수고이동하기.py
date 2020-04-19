import sys
sys.stdin=open('input.txt')

N, M = map(int, input().split())
li = [list(map(int, ' '.join(input()).split())) for _ in range(N)]
visited = [0] * (N * M *2)
q = [(0, 0, False)]
visited[0] = 1
idx = 0
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
result = -1
while len(q) > idx:
    p = q[idx]

    if p[0] == N-1 and p[1] == M-1:
        if p[2]:
            result = visited[M * p[0] + p[1] + M * N]
        else:
            result = visited[M * p[0] + p[1]]
        break
    for i in range(4):
        r = p[0] + dr[i]
        c = p[1] + dc[i]
        if 0 <= r < N and 0 <= c < M:
            if li[r][c] == 1:
                if (not p[2]) and visited[M * r + c + M * N] == 0:
                    q.append((r, c, True))
                    visited[M * r + c + M * N] = visited[M * p[0] + p[1]] + 1
            else:
                if p[2]:
                    if visited[M * r + c + M * N] ==0:
                        q.append((r, c, p[2]))
                        visited[M * r + c + M * N] = visited[M * p[0] + p[1] + M * N] + 1
                elif visited[M * r + c] ==0:
                    q.append((r, c, p[2]))
                    visited[M * r + c] = visited[M * p[0] + p[1]] + 1
                    visited[M * r + c + M * N] = visited[M * p[0] + p[1]] + 1
    else:
        idx += 1
        continue
    break
print(result)