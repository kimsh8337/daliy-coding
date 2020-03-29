import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]

    row = n//2
    sum = 0
    for i in range(n):
        sum += farm[row][i]

    for i in range(1,n//2+1):
        st = 0+i
        ed = n-1-i
        for j in range(st,ed+1):
            sum += farm[row+i][j] + farm[row-i][j]

    print('#{} {}'.format(tc, sum))