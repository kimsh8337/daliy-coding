import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())
#
# for tc in range(1, T+1):
#     n = input()
#     # print(n)
#     for i in range(len(n)):
#         a = '0'*len(n)
#         cnt = 0
#         res = 0
#     # print(a)
#         for j in range(j,len(n)):
#             if a[j] != n[j]:
#                 a[j] == 1
#
#
#
#         if n == a:
#             res = cnt
#             break

N=int(input())
for tc in range(N):
    que=list(map(int,input()))
    # print(que)
    cnt=0
    while 1:
        for sp in range(len(que)):
            if que[sp]==1:

                for ch in range(sp,len(que)):
                    if que[ch]==1:
                        que[ch]=0
                    elif que[ch]==0:
                        que[ch]=1
                cnt += 1
                if max(que)==0:
                    break
        break
    print(que,cnt)