# T=int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     lst = []
#     for i in range(N-M+1):
#         lst.append((sum(arr[i:i+M])))
#     print("#{} {}".format(tc, max(lst)-min(lst)))

def slice(nums):
    maxvalue = 0
    minvalue = 987654321

    for i in range(N-M+1):
        sum = 0
        for j in range(i, i+M):
            sum += nums[j]
        # s = sum(nums[i:i+M] 내장함수로 위 과정 쓰는법 아직 비추천 ㅎ
        if maxvalue < sum:
            maxvalue = sum
        if minvalue > sum:
            minvalue = sum
    return  maxvalue - minvalue

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())

    nums = list(map(int, input().split()))

    print('#{} {}'.format(tc, slice(nums)))
