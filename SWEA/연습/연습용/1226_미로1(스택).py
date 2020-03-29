import sys

sys.stdin = open('input.txt', 'r')


def dfs(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    stack_x = []
    stack_y = []
    while 1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < 16 and ny >= 0 and ny < 16 and arr[nx][ny] == 3:
                return 1
            if nx >= 0 and nx < 16 and ny >= 0 and ny < 16 and arr[nx][ny] == 0:
                stack_x.append(x)
                stack_y.append(y)
                arr[nx][ny] = 2
                x = nx
                y = ny
                break
        else:
            if len(stack_x) == 0 and len(stack_y) == 0:
                return 0
            else:
                x = stack_x.pop()
                y = stack_y.pop()


for tc in range(10):
    tc_num = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    print('#{} {}'.format(tc_num, dfs(1, 1)))
