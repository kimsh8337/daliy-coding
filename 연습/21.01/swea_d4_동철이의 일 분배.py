import sys
sys.stdin = open('input.txt', 'r')


def check(idx, value):
    global ans

    if 0 not in visited:
        if ans < value:
            ans = value
        return
    if value == 0:
        return
    if ans > value:
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            check(idx+1, value*(persons[idx][i]/100))
            visited[i] = 0
    return

for tc in range(1, int(input())+1):
    n = int(input())
    persons = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = -float('inf')

    check(0, 1)

    print('#{} {}'.format(tc, format(round(ans*100, 6), ".6f")))