# T = int(input())
# arr = list(range(1,13))
#
# for tc in range(1, T+1):
#     li = list(map(int, input().split()))
#     n = len(arr)
#     cnt = 0
#
#     for i in range(1<<n):
#         sum = 0
#         A = []
#         for j in range(n):
#             if i & (1<<j):
#                 sum += arr[j]
#                 A.append((arr[j]))
#         if sum == li[1] and len(A)==li[0]:
#             cnt += 1
#
#     print('#{} {}'.format(tc, cnt))

A = list(range(1, 13))
def find():
    ans = 0
    for i in range(1<<len(A)):
        cnt = 0
        sum = 0
        for j in range(len(A)):
            if i & (1<<j):
                sum += A[j]
                cnt += 1
        if cnt == N and sum == K:
            ans += 1
    return ans

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    print('#{} {}'.format(tc, find()))