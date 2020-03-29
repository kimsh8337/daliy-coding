import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N, M = map(str, input().split())
    lst = list(M)

    n = 0
    while 1:
        for i in range(int(N) - n - 1):
            if lst[i] == lst[i + 1]:
                del lst[i:i + 2]
                n += 2
                break
        else:
            break
    print('#{} {}'.format(tc, ''.join(lst)))