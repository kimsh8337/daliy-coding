import sys
sys.stdin = open('input.txt', 'r')

def rotation(nums):
    tmp = [['']*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[j][n-1-i] = nums[i][j]
    return tmp

def result(tmp, col):
    for i in range(n):
        for j in range(n):
            ans[i][col] += tmp[i][j]


T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [input().split() for _ in range(n)]

    ans = [['']*3 for _ in range(n)]

    for i in range(3):
        arr = rotation(arr)
        result(arr,i)

    print('#{}'.format(tc))
    for i in range(n):
        for j in range(3):
            print(ans[i][j], end =' ')
        print()