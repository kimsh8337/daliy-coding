import sys
sys.stdin = open('input.txt', 'r')

def attack(r,c):
    sum = 0
    for i in range(r,m+r):
        for j in range(c, m+c):
            sum += arr[i][j]
    return sum

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            tmp = attack(i,j)
            if ans < tmp:
                ans = tmp
    print('#{} {}'.format(tc, ans))