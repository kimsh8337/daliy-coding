import sys
sys.stdin = open('input.txt', 'r')

def search_func(i, j):
    global count_i, count_j
    for x in range(i, N):
        if li[x][j] == 0:
            break
        count_i += 1
    for y in range(j, N):
        if li[i][y] == 0:
            break
        count_j += 1
    for x in range(i, i + count_i):
        for y in range(j, j + count_j):
            li[x][y] = 0


def sort_func():
    for i in range(len(result) - 1):
        for j in range(len(result) - 1 - i):
            if result[j][0] * result[j][1] == result[j + 1][0] * result[j + 1][1]:
                if result[j][0] > result[j + 1][0]:
                    result[j], result[j + 1] = result[j + 1], result[j]
            elif result[j][0] * result[j][1] > result[j + 1][0] * result[j + 1][1]:
                result[j], result[j + 1] = result[j + 1], result[j]


TC = int(input())
for TC_count in range(TC):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    result = []
    result_count = 0
    for i in range(N):
        for j in range(N):
            if li[i][j] != 0:
                count_i = count_j = 0
                search_func(i, j)
                result.append([count_i, count_j])
                result_count += 1
    sort_func()
    print('#{} {} '.format(TC_count + 1, result_count), end='')
    for i in range(len(result)):
        print(' '.join(map(str, result[i])), end=' ')
    print()