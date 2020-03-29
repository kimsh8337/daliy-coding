import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    price = list(map(int, input().split()))
    earn = 0

    max_price = price[n-1]
    for i in range(n-2,-1,-1):
        if price[i] < max_price:
            earn += (max_price - price[i])
        else:
            max_price = price[i]

    print('#{} {}'.format(tc, earn))