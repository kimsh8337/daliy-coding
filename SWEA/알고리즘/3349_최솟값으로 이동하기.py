import sys
sys.stdin = open('input.txt', 'r')

dr = [1,0,-1,0,1,-1]
dc = [0,1,0,-1,1,-1]
def mincnt(st_x,st_y,cnt,ed_x,ed_y):
    global ans
    if st_x == ed_x and st_y == ed_y:
        if ans > cnt or ans == 0:
            ans = cnt
        return

    for i in range(6):
        nr = st_x + dr[i]
        nc = st_y + dc[i]
        if 0<=nr<(h+1) and 0<=nc<(w+1) and ans <= cnt:
            mincnt(nr,nc,cnt+1,ed_x,ed_y)
            cnt -= 1

for tc in range(1,1+int(input())):
    w,h,n = map(int, input().split())
    road = [[0]*(w+1) for _ in range(h+1)]
    x = []
    y = []
    ans = 0
    for _ in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    for i in range(n-1):
        mincnt(x[i],y[i],ans,x[i+1],y[i+1])
    print('#{} {}'.format(tc, ans))
