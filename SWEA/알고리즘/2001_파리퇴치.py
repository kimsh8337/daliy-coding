import sys
sys.stdin = open('input.txt', 'r')
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     arr = [[int(x) for x in input().split()] for _ in range(N)]
#     # print(arr)
#
#     r = 0
#     c = 0
#     sum = 0
#     for r in range(r,M+r):
#         for c in range(c,M+c):
#             sum += arr[r][c]
#         print(sum)
#     # arr2 = [[0]*M for _ in range(M)]
#     # for i in range(M):
#     #     for j in range(M):
#     #         arr2[i][j] = arr[i][j]
#
#
#     print(arr2)

def attack(r, c):
    sum = 0
    for i in range(r,r+M):
        for j in range(c,c+M):
            sum += fly[i][j]
    return sum

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    fly = [list(map(int, input().split()))for _ in range(N)]

    ans = 0

    # 시작위치를 위한 2중 for문
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 파리퇴치를 위한 2중 for문
            tmp = attack(i,j)
            if ans < tmp:
                ans = tmp
    print("#{} {}".format(tc, ans))