import sys
sys.stdin = open('input.txt', 'r')


def check(idx, value):
    global min_ans

    if idx >= 12:
        if min_ans > value:
            min_ans = value
        return

    check(idx+1, value+(month[idx]*price[0]))
    check(idx+1, value+price[1])
    check(idx+3, value+price[2])
    check(idx+12, value+price[3])
    return


for tc in range(1, int(input())+1):
    price = list(map(int, input().split()))
    month = list(map(int, input().split()))
    min_ans = float('inf')

    check(0,0)

    print('#{} {}'.format(tc, min_ans))