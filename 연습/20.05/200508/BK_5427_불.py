import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs():
    global ans
    while q:
        r,c,cnt = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<h and 0<=nc<w:
                if building[nr][nc] == '.':
                    building[r][c] = '.'
                    building[nr][nc] = '@'
                    cnt += 1
            else:
                ans = cnt
                return
        ans = cnt
    return ans


for tc in range(int(input())):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    ans = 0
    q = deque()
    flag = True
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                q.append((i,j,0))
                bfs()
            elif building[i][j] == '*':
                for d in range(4):
                    nr = i + dr[d]
                    nc = j + dc[d]
                    if 0<=nr<h and 0<=nc<w:
                        if building[nr][nc]=='.':
                            building[nr][nc]='*'
                        if building[nr][nc]=='@':
                            flag = False
                            break
    if flag:
        print(ans+1)
    else:
        print('IMPOOSIBE')
