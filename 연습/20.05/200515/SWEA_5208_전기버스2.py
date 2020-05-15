import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,1+int(input())):
    arr = list(map(int, input().split()))
    N = arr[0]
    ans = 0xfffffff
    def backtrack(pos, remain, cnt):
        global ans
        if ans <= cnt: return
        if pos >= N:
            ans = min(ans, cnt)
        else:
            backtrack(pos + 1, arr[pos] - 1, cnt + 1)
            if remain:
                backtrack(pos + 1, remain - 1, cnt)

    backtrack(2, arr[1] - 1, 0)
    print('#{} {}'.format(tc, ans))

# dp풀이법
# for tc in range(1, 1+int(input())):
#     arr = list(map(int, input().split()))
#     N = arr[0]
#
#     dp = [0xfffff] * (N+1)
#     for i in range(1, 1+arr[1]+1):
#         dp[i] = 0
#
#     for i in range(2,N): # 2번 정류소 ~ N - 1번까지
#         for j in range(i+1, i+arr[i]+1):
#             # i번 정류소에서 교체, i --> j
#             if j > N :  break
#             if dp[j] > dp[i] + 1:
#                 dp[j] = dp[i]+1
#
#     print('#{} {}'.format(tc, dp[N]))