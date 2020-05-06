import sys
sys.stdin = open('input.txt', 'r')

dr = [1,0]
dc = [0,1]

def check(r,c,sum):
    global min_sum
    if min_sum < sum:
        return
    
    if r==n-1 and c==n-1:
        if min_sum > sum:
            min_sum = sum
        return

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<n and 0<=nc<n:
            if visit[nr][nc]: continue
            visit[nr][nc] = 1
            check(nr,nc,sum+arr[nr][nc])
            visit[nr][nc] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    min_sum = float('inf')
    check(0,0,arr[0][0])
    print('#{} {}'.format(tc,min_sum))