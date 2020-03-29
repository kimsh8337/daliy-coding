import sys
sys.stdin = open('input.txt', 'r')
# 당근 수확1
# 배열의 순회를 연습할 수 있는 문제
# 영준이의 당근밭은 농사가 잘되어서

# T = int(input())
#
# for tc in range(1, T+1):
#     n = int(input())
#     carrot = list(map(int, input().split()))
#     carrot_sum = [0] * n
#     sum1 = 0
#     sum2 = 0
#     total = []
#     for i in range(len(carrot)):
#         carrot_sum = carrot[i]
#         sum1 = sum1 + carrot[i]
#         sum2 = sum(carrot) - sum1
#         total.append(abs(sum1-sum2))
#     for i in range(len(total)):
#         if total[i] == min(total):
#             print('#{} {} {}'.format(tc, i+1, total[i]))

T = int(input())

for tc in range(1, T+1):
    N = int(input())   # 농장의 길이
    carrots = list(map(int, input().split()))
    # 당근 밭을 두 구역으로 나누었을 때, 두 구역의
    # 당근 개수의 합이 차가 최소가 되는 구역은 구하라
    # 두 영역으로 나눌 수 있는 모든 경우의 수를 계산
    # 1번 구역 나누기 > 계산
    # 2번 구역 나누기 > 계산
    # 3번 구역 나누기 > 계산...N-1번까지 반복
    # 구역나누고
    # 나누어진 구역을 각각 순회하며 총합 구하기
    min_diff = 2000
    min_position = 0
    for i in range(N-1):   # i는 1번 일꾼의 마지막 일하는 칸
        # 나누어진 두 구역에 대한 총합구하기
        sum1 = 0   # 1번 일꾼의 총 수확량
        sum2 = 0   # 2번 일꾼의 총 수확량
        for j in range(i+1):
            # 합구하기
            sum1 += carrots[j]
        for j in range(i+1,N):
            sum2 += carrots[j]

        diff = abs(sum1 - sum2)   # 차이 구하기

        if min_diff > diff:
            min_diff = diff
            min_position = i
    print('#{} {} {}'.format(tc, min_position+1, min_diff))