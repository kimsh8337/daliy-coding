import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    h = n//2
    sum = 0
    
    for i in range(n):
        sum += farm[h][i]
    for i in range(h):
        for j in range(h-i,h+i+1):
            sum += farm[i][j]
            sum += farm[n-i-1][j]
    print('#{} {}'.format(tc, sum))