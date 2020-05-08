import sys
sys.stdin = open('input.txt','r')

for tc in range(1,1+int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        m, n = map(int, input().split())
        arr.append((m, n))
    arr = sorted(arr, key=lambda x: x[1])

    _list = [0] * 25
    cnt = 0
    for i, j in arr:
        for x in range(i, j):
            if _list[x] == 1:
                cnt += 1
                break
            else:
                _list[x] = 1

    print('#{} {}'.format(tc, len(arr) - cnt))