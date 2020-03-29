import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 98766554123
    for row in range(1,n):
        for col in range(1,n):
            s1 = s2 = s3 = 0
            for i in range(0,row):
                for j in range(0,col):
                    s1 += arr[i][j]
            for i in range(row,n):
                for j in range(0,col):
                    s2 += arr[i][j]
            for i in range(0,n):
                for j in range(col,n):
                    s3 += arr[i][j]
            diff = max(s1,s2,s3) - min(s1,s2,s3)
            if ans > diff:
                ans = diff
    print('#{} {}'.format(tc, ans))