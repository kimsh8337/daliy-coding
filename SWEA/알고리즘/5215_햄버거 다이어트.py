import sys
sys.stdin = open('input.txt', 'r')


def f(i, N, Cal, D, full):
    global L, satisfied
    if i == N:
        if Cal <= L:
            if D > satisfied:
                satisfied = D
    elif Cal == L:
        if D > satisfied:
            satisfied = D
    elif Cal > L:
        return
    elif D + full < satisfied:
        return
    else:
        # 재료를 선택하거나
        f(i + 1, N, Cal + ingredient[i][1], D + ingredient[i][0], full - ingredient[i][0])
        # 재료를 선택하지 않거나
        f(i + 1, N, Cal, D, full - ingredient[i][0])


T = int(input()) + 1
for tc in range(1, T):
    N, L = map(int, input().split())

    ingredient = [list(map(int, input().split())) for _ in range(N)]
    full = 0
    for i in range(N):
        full += ingredient[i][0]
    satisfied = 0
    f(0, N, 0, 0, full)
    print('#{0} {1}'.format(tc, satisfied))