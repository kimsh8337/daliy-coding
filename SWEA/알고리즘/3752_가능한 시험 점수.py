import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 1+int(input())):
    n = int(input())
    score = list(map(int, input().split()))
    sum_list = set([0])
    for x in score:
        num = set()
        for y in sum_list:
            num.add(x+y)
        sum_list = set(list(sum_list)+list(num))
    print('#{} {}'.format(tc, len(sum_list)))

# 시간초과
# def func(i=0,sum=0):
#     if i == n:
#         sum_list.add(sum)
#         return
#
#     for j in range(n):
#         if visit[j] == 0:
#             sum_list.add(sum)
#             visit[j] = 1
#             func(i+1,sum + score[j])
#             visit[j] = 0
#
# for tc in range(1,1+int(input())):
#     n = int(input())
#     score = list(map(int,input().split()))
#     visit = [0]*n
#     sum_list = set()
#     func()
#     print('#{} {}'.format(tc, len(sum_list)))

# DP풀이
# for tc in range(1, int(input()) + 1):
#     n = int(input())
#     score = list(map(int, input().split()))
#     D=[0]*10001
#     D[0] = 1
#     sum = ans = 0
#     for i in range(n):
#         sum += score[i]
#     for i in range(n):
#         for j in range(sum, 0, -1):
#             if D[j]:
#                 D[j+score[i]] = 1
#         D[score[i]] = 1
#     for i in range(sum+1):
#         ans += D[i]
#     print('#{} {}'.format(tc,ans))