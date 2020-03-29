import sys

sys.stdin = open('input.txt', 'r')

# def miro(x,y):
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     stack_x = [0, x]
#     stack_y = [0, y]
#     while 1:
#         for i in range(4):
#             if arr[x + dx[i]][y + dy[i]] == 3:
#                 return 1
#         for i in range(4):
#             if arr[x+dx[i]][y+dy[i]] == 0:
#                 x = x + dx[i]
#                 y = y + dy[i]
#                 stack_x.append(x)
#                 stack_y.append(y)
#                 arr[x][y] = 2
#                 break
#         else:
#             stack_x.pop()
#             stack_y.pop()
#             if len(stack_x) != 0:
#                 x = stack_x[-1]
#                 y = stack_y[-1]
#             else:
#                 return 0
#
#
# for TC_count in range(1,11):
#     n = input()
#     arr = [list(map(int, ' '.join(input()).split())) for _ in range(100)]
#     print('#{} {}' .format(TC_count, miro(1,1)))


dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c):
    global ans
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nc < 0 or nc>=N or nr<0 or nc>=N:
            continue
        if maze[nr][nc] == 0 or maze[nr][nc] ==3:
            if maze[nr][nc] == 3:
                ans = 1
                return
            maze[nr][nc] = 1
            dfs(nr, nc)


for tc in range(10):
    tc_num = int(input())
    N = 16
    maze = [list(map(int, input()))  for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i
                sC = j

    dfs(sR, sC)
    print("#{} {}".format(tc_num, ans))