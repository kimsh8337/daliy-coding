import sys
sys.stdin = open('input.txt','r')

N, M = map(int, input().split())
card = list(map(int, input().split()))
answer = 0
for i in range(0, N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if (card[i]+card[j]+card[k]) <= M and M - (card[i]+card[j]+card[k]) < M - answer:
                answer = card[i]+card[j]+card[k]
print(answer)














# n,m = map(int,input().split())
# num = list(map(int, input().split()))
# sum = 0
# sum_result = []
# diff_result = [987654321]
# ans = [987654321]
# for i in range(0,n-2):
#     for j in range(i+1,n-1):
#         # if j == i:
#         #     continue
#         for k in range(j+1,n):
#             # if k == i or k == j:
#             #     continue
#             sum = num[i] + num[j] + num[k]
#             if sum not in sum_result or sum <= m:
#                 sum_result.append(sum)
# for i in range(len(sum_result)):
#     a = abs(m-sum_result[i])
#     if a < min(diff_result):
#         diff_result.pop()
#         ans.pop()
#         diff_result.append(a)
#         ans.append(i)
# print(sum_result[ans[-1]])
