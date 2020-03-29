import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())
#
# for tc in range(1,T+1):
#     N, M, K = map(int, input().split())
#     guest = list(map(int, input().split()))
#
#     # print(guest)
#     # max_g =0
#     # for i in range(len(guest)-1):
#     #     if guest[i] > guest[i+1]:
#     #         max_g = guest[i]
#     length = max(guest)
#
#     b_cnt = 0
#     g_cnt = 0
#     for i in range(length + 1):
#         if i % M == 0 and i != 0:
#             b_cnt += K
#         if i == guest[i]:
#             g_cnt += 1
#             if b_cnt < g_cnt:
#                 break
#     print('#{}'.format(tc) , end =' ')
#     if b_cnt < g_cnt :
#         print('Impossible')
#     else:
#         print('Possible')

# 진기의 최고급 붕어빵
# 테스트 케이스
T = int(input())
for t in range(1,T+1):
    N,M,K = map(int, input().split())
    customers = list(map(int, input().split()))
    # 현재 남아있는 붕어빵이 아니라, 몇개를 팔았느닞
    # 알고 있으면, 손님이 들어온 시점에 붕어빵을 팔 수 있는지
    # 결정할 수 있다.
    customers.sort()
    result = True   # 모든 손님에게 붕어빵을 팔 수 있는지 여부
    sell = 0   # 총 판매량
    for i in range(N):   # 손님의 수만큼 반복
        # 일찍 온 손님부터 물건 팔기 시작
        # 만약에 손님에게 붕어빵을 팔지 못하면, 더이상 검사하지 않고 종료
        time = customers[i]
        # 진기가 time 시간 안에 만들 수 있는 총량
        total = (time // M)*K
        if sell >= total :   # 재고없음
            result = False   # 못팜
            break
        else:
            sell += 1
    if result:
        print ('#{} Possible'.format(t))
    else:
        print ('#{} Impossible'.format(t))
