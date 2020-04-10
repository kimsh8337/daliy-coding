arr = [69, 10, 30, 2, 16, 8, 31, 22]; N = len(arr)

# 코드는 쉽지만 메모리를 많이 씀
# def mergeSort(lst):
#     # len(lst) == 1
#     if len(lst) == 1: return lst
#
#     mid = len(lst) >> 1 # 중간 위치 설정
#     L = mergeSort(lst[:mid])
#     R = mergeSort(lst[mid:])
#
#     # 병합
#     ret = []
#     while L and R:
#         if L[0] < R[0]:
#             ret.append(L.pop(0))
#         else:
#             ret.append(R.pop(0))
#     ret.extend(L)
#     ret.extend(R)
#     return ret
# sorted = mergeSort(arr)
# print(sorted)

# 문제의 크기를 범위로 표현
tmp = [0] * N
def mergeSort(lo, hi):
    print('[',lo,hi,']')
    if lo == hi: return

    mid = (lo+hi) >> 1
    mergeSort(lo,mid)
    mergeSort(mid+1, hi)

    # # 병합
    # i, j, k = lo, mid + 1, lo
    # while i <= mid and j <= hi:
    #     if arr[i] < arr[j]:
    #         tmp[k] = arr[i]; i, k = i + 1, k + 1
    #     else:
    #         tmp[k] = arr[j]; j, k= j + 1, k + 1
    # while i <= mid:
    #     tmp[k] = arr[i]; i, k = i + 1, k + 1
    # while j <= hi:
    #     tmp[k] = arr[j]; j, k = j + 1, k + 1
    #
    # for i in range(lo, hi+1):
    #     arr[i] = tmp[i]
    # print(arr[lo:hi+1])

mergeSort(0, N-1)
print(arr)