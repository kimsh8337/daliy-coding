import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def water():
    wlen = len(wave)
    while wlen:
        rr, cc = wave.popleft()

        for a in range(4):
            nnr = rr + dr[a]
            nnc = cc + dc[a]
            if 0 <= nnr < R and 0 <= nnc < C:
                if forest[nnr][nnc] == '.':
                    wave.append((nnr, nnc))
                    forest[nnr][nnc] = '*'
        wlen -= 1



def bfs():
    while q:
        qlen = len(q)
        while qlen:
            r, c, cnt = q.popleft()

            for a in range(4):
                nr = r + dr[a]
                nc = c + dc[a]
                if 0<=nr<R and 0<=nc<C and not visited[nr][nc]:
                    if forest[nr][nc] == '.':
                        q.append((nr,nc,cnt+1))
                        visited[nr][nc] = 1
                    elif forest[nr][nc] == 'D':
                        print(cnt+1)
                        return
            qlen -= 1
        water()
    print('KAKTUS')
    return

R, C = map(int, input().split())
forest = [list(map(str, input().strip())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
q, wave = deque(), deque()

for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':
            q.append((i,j,0))
            forest[i][j] = '.'
        elif forest[i][j] == '*':
            wave.append((i,j))
water()
bfs()