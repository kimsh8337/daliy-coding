import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def combo(com,n,y_cnt,cnt):
    global ans
    if cnt == 7:
        ans += bfs(com)

    for i in range(n,25):
        r,c = i//5, i%5
        if arr[r][c] == 'Y':
            if y_cnt == 3:continue
            combo(com+[(r,c)],i+1,y_cnt+1,cnt+1)
        else:
            combo(com+[(r,c)],i+1,y_cnt,cnt+1)

def bfs(path):
    q = deque()
    visit = [path[0]]
    q.append(path[0])
    while q:
        r,c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr>4 or nc>4 or nr<0 or nc<0: continue
            if (nr,nc) in path:
                if (nr,nc) in visit: continue
                visit.append((nr,nc))
                q.append((nr,nc))

    if len(visit) == 7:
        return 1
    else:
        return 0

arr = [list(input()) for _ in range(5)]
ans = 0
combo([],0,0,0)
print(ans)