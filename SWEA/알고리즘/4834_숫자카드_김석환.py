for tc in range(1,1+int(input())):
    n = int(input())
    a = list(map(int, input()))
    num =[0]*10

    for i in range(n):
        num[a[i]] += 1

    tmp = 0
    card = -1
    for i in range(10):
        if tmp <= num[i]:
            tmp = num[i]
            card = i
    print('#{} {} {}'.format(tc, card, tmp))

# T=int(input())
# for tc in range(1, T+1):
#     N = input()
#     num_list = list(map(int, input()))
#
#     answer = 0
#     count=0
#
#     for i in range(10):
#         if num_list.count(i) >= count:
#             count = num_list.count(i)
#             answer = i
#     print("#{} {} {}".format(tc, answer, count))

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     line = input()
#
#     nums = [0]*10
#     for i in range(len(line)):
#         nums[int(line[i])] += 1
#
#     max_idx = 0
#     max_val = 0
#     # 지금은 뒤에서 검사를 하기 때문에 조건 < 만 검사
#     # 앞에서부터 검사한다고 하면 <= 으로 검사
#     # 문제에서 같은 장수를 가지면 큰 수를 출력한다고 했기 때문에.
#     for i in range(len(nums)-1,-1,-1):
#         if max_val < nums[i]:
#             max_val = nums[i]
#             max_idx = i
#
#     print('#{} {} {}'.format(tc, max_idx, max_val))