import sys
sys.stdin = open('input.txt','r')

def backtrack(r,c):
    global sum_arr
    visit[c] = 1
    sum_arr += arr[r][c]
    if sum_arr > min(result):
        return
    if r == (n-1):
        result.append(sum_arr)
        return
    else:
        for i in range(n):
            if visit[i]:
                continue
            backtrack(r+1,i)
            visit[i] = 0
            sum_arr -= arr[r+1][i]

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = [987654321987654321]
    for i in range(n):
        visit = [0]*n
        sum_arr = 0
        backtrack(0,i)
    print('#{} {}'.format(tc, min(result)))