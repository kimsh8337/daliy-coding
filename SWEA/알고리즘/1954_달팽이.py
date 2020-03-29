# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
#     arr = [[0]*N for _ in range(N)]
#
#     r = 0
#     c = -1
#     num = 1
#     dir = 1
#     K = N
#
#     while 1:
#         # 수평이동
#         for k in range(K):
#             c += dir
#             arr[r][c] = num
#             num += 1
#         K -= 1
#         if K == 0:
#             break
#
#         # 수직이동
#         for k in range(K):
#             r += dir
#             arr[r][c] = num
#             num += 1
#
#         dir *= -1
#
#     print('#{}'.format(tc,))
#     for i in range(N):
#         for j in range(N):
#             print(arr[i][j] ,end =' ')
#         print()
#

# 우하좌상 풀이
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dir = 0
    r = 0
    c = 0
    num = 1

    while num <= N*N:
        arr[r][c] = num
        num += 1

        nr = r+dr[dir]
        nc = c+dc[dir]
        if nr >= 0 and nr < N and nc>=0 and nc < N and arr[nr][nc] == 0:
            r = nr
            c = nc
        else:
            dir = (dir+1)%4
            r += dr[dir]
            c += dc[dir]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()