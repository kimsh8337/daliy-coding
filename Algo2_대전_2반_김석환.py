import sys
sys.stdin = open('input2.txt', 'r')

# 상하좌우대각선 델타값
dr = [0,0,1,-1,1,-1,1,-1]
dc = [1,-1,0,0,1,-1,-1,1]

def check(r,c,x):
    global cnt

    # 방문한 곳 1로 바꿔주고, cnt 1씩 증가시켜줌
    visit[r][c] = 1
    cnt += 1

    # 상하좌우대각선 반복문으로 돌리기
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        # 배열 범위 내에서만 돌 수 있음
        if 0<= nr < n and 0<= nc < n:
            # 방문하지 않은 곳과 배열값이 같은 곳만 찾아가기
            if visit[nr][nc] == 0 and arr[nr][nc]==x:
                check(nr,nc,x)


for tc in range(1,1+int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    cnt = 0
    max_cnt = -1
    size = 0
    max_size = -1

    for i in range(n):
        for j in range(n):
            # 주어진 배열값이 0이고 방문한 적있는 곳은 넘어가기
            if arr[i][j] == 0 and visit[i][j]:
                continue
            # 새로운 배열 값을 받을 때 cnt값 0으로 초기화시키기
            cnt = 0
            # (i,j)위치의 값 check함수 돌리기
            check(i,j,arr[i][j])
            # 매장 면적을 구함
            size = arr[i][j]*cnt
            # 최대 매장량과 최대 매장 광맥 면적 구하기
            if max_size == -1 or max_size < size:
                max_size = size
                max_cnt = cnt

    print('#{} {} {}'.format(tc, max_size, max_cnt))
