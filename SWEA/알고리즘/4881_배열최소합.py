import sys
sys.stdin = open('input.txt','r')

# 시간초과...
# def backtrack(i=0, sum=0):
#     global min_sum
#     if i == n:
#         if sum < min_sum or min_sum == -1:
#             min_sum = sum
#         return
#
#     for j in range(n):
#         if visit[j]:
#             continue
#         visit[j] = 1
#         backtrack(i+1, sum + arr[i][j])
#         visit[j] =0
#
# for tc in range(1,1+int(input())):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visit = [0]*n
#     min_sum = -1
#     backtrack()
#     print('#{} {}'.format(tc, min_sum))


def backtrack(r,c):
    global sum_arr
    visit[c] = 1
    sum_arr += arr[r][c]
    if sum_arr > min(result):
        return
    if r == (n-1):
        result.append(sum_arr)
        return
    else:
        for i in range(n):
            if visit[i]==0:
                backtrack(r+1,i)
                visit[i]=0
                sum_arr -= arr[r+1][i]

for tc in range(1, 1+int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = [987654321]
    for i in range(n):
        visit = [0]*n
        sum_arr = 0
        backtrack(0,i)
    print('#{} {}'.format(tc, min(result)))