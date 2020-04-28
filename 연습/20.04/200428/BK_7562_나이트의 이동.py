import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

move = [(1,-2),(1,2),(2,-1),(2,1),(-1,-2),(-1,2),(-2,-1),(-2,1)]

def bfs(arr, r1, c1, r2, c2):
    q = deque()
    q.append((r1, c1))

    while q:
        rr, cc = q.popleft()

        if rr == r2 and cc == c2:
            return arr[rr][cc]

        for i in range(8):
            nr = rr + move[i][0]
            nc = cc + move[i][1]
            if 0<=nr<l and 0<=nc<l and arr[nr][nc]==0:
                arr[nr][nc] = arr[rr][cc] + 1
                q.append((nr,nc))

tc = int(input())
for _ in range(tc):
    l = int(input())
    st_r, st_c = map(int, input().split())
    ed_r, ed_c = map(int, input().split())
    find = [[0]*l for _ in range(l)]
    print(bfs(find, st_r, st_c, ed_r, ed_c))
