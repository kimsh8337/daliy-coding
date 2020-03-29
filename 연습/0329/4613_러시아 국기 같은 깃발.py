import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 1+int(input())):
    n,m = map(int, input().split())
    flag = [list(input()) for _ in range(n)]
    min_cnt = -1

    for i in range(n-2):
        for j in range(i,n-1):
            cnt = 0
            for k in range(0,i+1):
                for p in range(m):
                    if flag[k][p] != 'W':
                        cnt += 1
            for k in range(i+1,j+1):
                for p in range(m):
                    if flag[k][p] != 'B':
                        cnt += 1
            for k in range(j+1,n):
                for p in range(m):
                    if flag[k][p] != 'R':
                        cnt += 1
            if min_cnt > cnt or min_cnt == -1:
                min_cnt = cnt

    print('#{} {}'.format(tc, min_cnt))