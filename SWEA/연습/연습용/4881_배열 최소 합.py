import sys
sys.stdin = open('input.txt','r')

def backtrack(i=0, sum =0):
    global min_sum
    if i == n:
        if min_sum > sum or min_sum == -1:
            min_sum = sum
        return

    for j in range(n):
        if visit[j] == 0:
            visit[j] = 1
            backtrack(i+1, sum + arr[i][j])
            visit[j] = 0

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * n
    min_sum = -1
    backtrack()
    print('#{} {}'.format(tc, min_sum))
