import sys
sys.stdin = open('input.txt','r')

for tc in range(1, 11):
    n = int(input())

    table = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    for j in range(n):
        for i in range(n):
            if table[i][j] == 1:
                for x in range(i+1,n):
                    if table[x][j] == 2:
                        cnt += 1
                        break
                    elif table[x][j] == 1:
                        break

    print('#{} {}'.format(tc,cnt))