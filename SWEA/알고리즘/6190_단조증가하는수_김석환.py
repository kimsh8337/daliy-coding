import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     a_list = list(map(int, input().split()))
#
#     x = []
#     for i in range(N):
#         for j in range(i+1,N):
#             x.append(a_list[i]*a_list[j])
#
#
#     for i in range(len(x)):
#         n = x[i] // 10
#         m = x[i] % 10
#         if
#
#     print(x)

# 앞부터 검사
# def check(num):
#     tmp = str(num)
#     for i in range(1, len(tmp)):
#         if tmp[i-1] > tmp[i]:
#             return -1
#     return  num
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#
#     max_value = -1
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             tmp = check(nums[i] * nums[j])
#             if max_value < tmp:
#                 max_value = tmp
#
#     print('#{} {}'.format(tc, max_value))

# 뒤부터 검사
T = int(input())

    for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_value = -1

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            num = nums[i] * nums[j]
            tmp_num = num
            prev = 10
            isOk = True

            while num > 0:
                target = num % 10
                if prev < target:
                    isOk = False
                    break
                num = num // 10
                prev = target

            if isOk:
                if max_value < tmp_num:
                    max_value = tmp_num
    print('#{} {}'.format(tc, max_value))