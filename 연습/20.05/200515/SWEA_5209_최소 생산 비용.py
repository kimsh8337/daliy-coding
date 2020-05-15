import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i=0,sum=0):
    global min_sum
    if min_sum < sum:
        return

    if i == n:
        if min_sum > sum:
            min_sum = sum
        return

    for j in range(n):
        if visit[j]: continue
        visit[j] = 1
        backtrack(i+1,sum+arr[i][j])
        visit[j] = 0

for tc in range(1, 1+int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * n
    min_sum = float('inf')
    backtrack()
    print('#{} {}'.format(tc, min_sum))