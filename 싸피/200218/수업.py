# arr = 'ABC'
# N = len(arr)
#
# for i in range(N):
#     for j in range(N):
#         if j == i:
#             continue
#         for k in range(N):
#             if k == i or k == j:
#                 continue
#             print(arr[i],arr[j],arr[k])


# arr = 'ABC'
# N = len(arr)
# visit = [0] * N   # 이전에 선택한 요소들에 대한 정보
# order = []
#
# def backtrack(k):        # k: 함수 호출트리에서 높이, 선택한 요소의 수
#     if k == N:           # 단말노드의 도착
#         print(order)     # order에 하나의 순열이 저장된 상태
#     else:                # 아직 해야할 선택이 남은 상태\
#         for i in range(N):
#             if visit[i]:
#                 continue
#             visit[i] = 1
#             order.append(arr[i])     # i번 요소를 선택
#             backtrack(k+1)
#             order.pop()
#             visit[i] = 0
# backtrack(0)


# arr = 'ABC'
# N = len(arr)
# # visit = [0] * N   # 이전에 선택한 요소들에 대한 정보
# order = []
#
# def backtrack(k,visit):        # k: 함수 호출트리에서 높이, 선택한 요소의 수
#     if k == N:           # 단말노드의 도착
#         print(order)     # order에 하나의 순열이 저장된 상태
#     else:                # 아직 해야할 선택이 남은 상태\
#         for i in range(N):
#             if visit & (1 << i):
#                 continue
#             order.append(arr[i])     # i번 요소를 선택
#             backtrack(k+1, visit | (1 << i))
#             order.pop()
# backtrack(0, 0)
#
# arr = [i for i in range(1,11)]
# N = len(arr)
#
# cnt = 0
# def backtrack(k, cur,n):
#     if cur > 10:
#         return
#     if k == N:
#         global cnt
#         if cur == 10:
#             cnt +=1
#     else:
#         backtrack(k+1, cur + arr[k], n+1)   # k번 요소를 포함
#         backtrack(k+1, cur, n)   # k번 요소를 포함하지 않는 경우
#
# backtrack(0,0,0)
# print(cnt)
#
# def exp(C,n):
#     if n ==0:
#         return 1
#     if n == 1:
#         return C
#     if n&1:    # 홀수=n%2랑 같은 의미
#         ret = exp(C,(n-1)//2)
#         return ret*ret*C
#     else:
#         ret = exp(C,n//2)
#         return ret*ret
#
# print(exp(2,10))
# print(exp(2,100))

# A = [64, 7, 4, 25, 10, 22, 11, 8]
# N = len(A)
#
# def getMin(A, lo,hi):   # A[lo"hi + 1]에서 최소값을 반환하는 함수
#     print(lo,hi)
#     if lo == hi:
#         return A[lo]
#     mid = (lo +hi) >> 1    # mid = (lo +hi) // 2
#     l = getMin(A,lo,mid)
#     r = getMin(A, mid+1,hi)
#     return min(l,r)
#
# print(getMin(A,0,N-1))