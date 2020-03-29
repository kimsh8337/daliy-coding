import sys

sys.stdin = open('input.txt', 'r')


def game(x, y):
    if (num[x] == 1 and num[y] == 3) or (num[x] == 2 and num[y] == 1) or (num[x] == 3 and num[y] == 2):
        return x
    elif (num[x] == 2 and num[y] == 3) or (num[x] == 1 and num[y] == 2) or (num[x] == 3 and num[y] == 1):
        return y
    elif (num[x] == 1 and num[y] == 1) or (num[x] == 2 and num[y] == 2) or (num[x] == 3 and num[y] == 3):
        return x


def getMin(x, y):
    if x == y:
        return x
    mid = (x + y) >> 1
    l = getMin(x, mid)
    r = getMin(mid + 1, y)
    return game(l, r)


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    num = list(map(int, input().split()))
    N = len(num)
    ans = getMin(0, N - 1)
    print('#{} {}'.format(tc, ans + 1))