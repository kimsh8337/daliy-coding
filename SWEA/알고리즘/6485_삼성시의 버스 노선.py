import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    bus = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    bus_stop = []
    for i in range(p):
        stop = int(input())
        bus_stop.append(stop)
    print('#{}'.format(tc), end =' ')
    for i in range(len(bus_stop)):
        cnt = 0
        for j in range(n):
            if bus[j][0]<=bus_stop[i]<=bus[j][1]:
                cnt += 1
        if i < len(bus_stop)-1:
            print('{}'.format(cnt), end = ' ')
        elif i == len(bus_stop)-1:
            print('{}'.format(cnt))

# 다솜이 코드
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     result = [0] * 5000
#     for i in lst:
#         for j in range(i[0] - 1, i[1]):
#             result[j] += 1
#     P = int(input())
#     stop=[]
#     for i in range(P):
#         c=int(input())
#         stop.append(result[c-1])
#
#     print('#{} {}'.format(tc, ' '.join(map(str, stop))))