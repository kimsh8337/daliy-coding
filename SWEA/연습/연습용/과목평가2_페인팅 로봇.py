import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    r,c,n = map(int, input().split())
    arr = [[0]*(c+1) for _ in range(r+1)]

    for x in range(n):
        r1,c1,r2,c2 = map(int, input().split())

        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                arr[i][j] += 1

        max = 0
        for i in range(r+1):
            for j in range(c+1):
                if max < arr[i][j]:
                    max = arr[i][j]
        cnt = 0
        for i in range(r+1):
            for j in range(c+1):
                if max == arr[i][j]:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))
















