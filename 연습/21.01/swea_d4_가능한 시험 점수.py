import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):
    n = int(input())
    score = list(map(int, input().split()))
    res = set([0])

    for x in score:
        num = set()
        for y in res:
            num.add(x+y)
        res = set(list(res)+list(num))

    print('#{} {}'.format(tc, len(res)))