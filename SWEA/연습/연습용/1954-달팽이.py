import sys
sys.stdin = open('input.txt', 'r')

dr = [0,1,0,-1]
dc = [1,0,-1,0]
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    r=0
    c=0
    dir=0
    num=1

    while(num <= n*n):
        arr[r][c] = num
        num += 1

        nr = r+dr[dir]
        nc = c+dc[dir]

        if nr>=0 and nr<n and nc>=0 and nc<n and arr[nr][nc]==0:
            r=nr
            c=nc
        else:
            dir = (dir+1)%4
            r += dr[dir]
            c += dc[dir]

    print('#{}'.format(tc))
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()