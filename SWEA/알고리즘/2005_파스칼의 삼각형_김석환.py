import sys

sys.stdin = open('input.txt', 'r')

# T = int(input())
#
# for tc in range(1, T + 1):
#     n = int(input())
#     print('#{}'.format(tc))
#     a = [[1 for _ in range(i)] for i in range(1, n + 1)]
#     # print(a) --> [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]]
#     for i in range(2, n):
#         for j in range(1, i):
#             a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
#     for i in range(n):
#         print(' '.join(map(str, a[i])))

T = int(input())

for tc in range(1, T+1):
    N =int(input())

    pascal = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if j == 0:
                pascal[i][j] = 1
            elif j == i:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i+1):
            print(pascal[i][j], end=' ')
        print()