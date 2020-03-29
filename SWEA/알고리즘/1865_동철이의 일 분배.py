import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i=0, s=1):
    global ans
    if i == n:
        if ans < s or ans == -1:
            ans = s
        return
    if s == 0:
        return
    if ans > s:
        return

    for j in range(n):
        if visit[j] == 0:
            visit[j] = 1
            backtrack(i+1, s * (work[i][j]/100))
            visit[j] = 0

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    work = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * n
    ans = -1
    backtrack()
    print('#{}'.format(tc),end = ' ')
    print(format(ans*100,".6f"))

