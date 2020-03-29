for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # arr.sort()
    # for i in range(5):
    #     print(arr[N-1-i], end = ' ')
    #     print(arr[i], end = ' ')
    # print()

    # 선택 정렬
    for i in range(10):  # 최소값을 찾을 범위의 시작
        if i % 2 == 0:  # 짝수일때는 큰 값순서로
            idx = i
            for j in range(i + 1, N):
                if arr[idx] < arr[j]:
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]
        else:
            idx = i
            for j in range(i+1,N):
                if arr[idx] > arr[j]:
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]
    for i in range(10):
        print(arr[i],end = ' ')
    print()



# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#
#     result = []
#     for i in range(len(nums)):
#         result[0] = max(nums)
#         result[1] = min(nums)

# def sort(tmp):
#     for i in range(len(tmp)-1):
#         min_idx = i
#         for j in range(i+1, len(tmp)):
#             if tmp[min_idx] > tmp[j]:
#                 min_idx = j
#
#         tmp[min_idx], tmp[i] = tmp[i], tmp[min_idx]
#
#     return tmp
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#
#     nums = sort(nums)
#
#     ans = [0]*10
#
#     idx = 0
#     for i in range(0, 10, 2):
#         ans[i] = nums[N-1-idx]
#         ans[i+1] = nums[idx]
#         idx += 1
#
#     print('#{}'.format(tc), end=' ')
#     for i in range(len(ans)):
#         print(ans[i], end=' ')
#     print()