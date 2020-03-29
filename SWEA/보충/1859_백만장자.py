# 테스트케이스
# N 이후, N개의 매매가

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    # price 배열을 뒤에서 부터 순회하면서, max 값 잡고
    # max보다 더 큰 숫자가 나올 때까지, 수익 책정
    earn = 0    # 수익을 저장할 배열
    max_price = price[N-1]   # 마지막 원소를 max로 지정
    for i in range(N-2, -1, -1):
        if price[i] < max_price:
            # (최고가 - 현재가격)을 수익으로 더한다
            earn += (max_price - price[i])
        else:
            max_price = price[i]
    print('#{} {}'.format(tc, earn))