for tc in range(1, 1+int(input())):
    p,a,b = map(int, input().split())
    st_a, st_b = 1, 1
    ed_a, ed_b = p, p
    cnt=[0,0]

    while 1:
        ca = int((st_a + ed_a) / 2)
        cb = int((st_b + ed_b) / 2)
        if ca > a:
            ed_a = ca
            cnt[0] += 1
        elif ca < a:
            st_a = ca
            cnt[0] += 1
        if cb > b:
            ed_b = cb
            cnt[1] += 1
        elif cb < b:
            st_b = cb
            cnt[1] += 1
        if ca==a and cb==b:
            break

    print('#{}'.format(tc), end = ' ')
    if cnt[0] > cnt[1]:
        print('B')
    elif cnt[0] < cnt[1]:
        print('A')
    else:
        print(0)


# T = int(input())
#
# for tc in range(1, T+1):
#     P,A,B = map(int, input().split())
#     A_l = B_l = 1
#     A_r = B_r = P
#     A_c = B_c = int((B_l+B_r)/2)
#     result = ''
#
#     while 1:
#         if A_c == A and B_c == B:
#             result = '0'
#             break
#         if A_c == A:
#             result = 'A'
#             break
#         if B_c == B:
#             result = 'B'
#             break
#         if A>A_c:
#             A_l = A_c
#         else:
#             A_r = A_c
#
#         if B>B_c:
#             B_l = B_c
#         else:
#             B_r = B_c
#
#         A_c = int((A_l+A_r)//2)
#         B_c = int((B_l+B_r)//2)
#
#     print('#{} {}'.format(tc, result))

# win = ['A','0','B']
#
# def binary(page, search):
#     start = 1
#     end = page
#     cnt = 1
#     while start <= end:
#         mid = (start + end) // 2
#         if mid == search:
#             return cnt
#         if mid < search:
#             start = mid
#         else:
#             end = mid
#
#         cnt+=1
#
# T = int(input())
#
# for tc in range(1,T+1):
#     P,A,B = map(int, input().split())
#
#     cntA = binary(P, A)
#     cntB = binary(P, B)
#     ans = -1
#     if cntA == cntB:
#         ans = 1
#     elif cntA < cntB:
#         ans = 0
#     else:
#         ans = 2
#     print('#{} {}'.format(tc,win[ans]))

# def binarySearch(lo, hi, key):
#     if lo > hi:
#         return 0
#
#     mid = (lo+hi)>>1
#     if mid == key:
#         return 1
#     elif mid>key:
#         return binarySearch(lo,mid,key)+1
#     else:
#         return binarySearch(mid,hi,key)+1
#
# for tc in range(1, int(input())+1):
#     p, pa, pb = map(int, input().split())
#
#     A = binarySearch(1, p, pa)
#     B = binarySearch(1, p, pb)