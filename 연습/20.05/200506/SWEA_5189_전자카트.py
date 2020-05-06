import sys
sys.stdin = open('input.txt', 'r')

def check(i):
    global min_sum, sum

    if sum < min_sum:
        visit[i] = 1
        if 0 not in visit:
            sum += arr[i][0]
            if sum < min_sum:
                min_sum = sum
            sum -= arr[i][0]
        else:
            for j in range(n):
                if not visit[j]:
                    sum += arr[i][j]
                    check(j)
                    sum -= arr[i][j]
        visit[i] = 0

for tc in range(1,1+int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [0]*n
    min_sum = float('inf')
    sum = 0
    check(0)
    print('#{} {}'.format(tc, min_sum))