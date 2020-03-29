import sys

sys.stdin = open('input.txt', 'r')


def dfs(x, y):
    global ans
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < 16 and ny >= 0 and ny < 16:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                dfs(nx, ny)
            if arr[nx][ny] == 3:
                arr[x][y] = 2
                ans = 1
                return
    return


for tc in range(10):
    tc_num = int(input())
    ans = 0
    arr = [list(map(int, input())) for _ in range(16)]
    dfs(1, 1)
    print('#{} {}'.format(tc_num, ans))