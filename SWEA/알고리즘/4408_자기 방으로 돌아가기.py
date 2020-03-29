import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,1+int(input())):
    N = int(input())

    cnt = [0]*201   # 1 ~ 200

    for _ in range(N):
        a, b = map(int, input().split())    # a --> b

        a = (a+1)//2
        b = (b+1)//2

        if a>b :
            a,b = b,a
        for i in range(a,b+1):
            cnt[i] += 1

    print("#{} {}".format(tc, max(cnt)))


# for tc in range(1, 1 + int(input())):
#     n = int(input())
#     st = []
#     ed = []
#     ans = 1
#
#     for i in range(n):
#         a, b = map(int, input().split())
#         st.append(a)
#         ed.append(b)
#
#     for i in range(len(st) - 1):
#         x = []
#         y = []
#         if st[i] <= ed[i]:
#             for j in range(st[i],ed[i]+1):
#                 x.append(j)
#             if st[i+1] <= ed[i+1]:
#                 for j in range(st[i+1],ed[i+1]+1):
#                     y.append(j)
#             else:
#                 for j in range(ed[i+1],st[i+1]+1):
#                     y.append(j)
#         else:
#             for j in range(ed[i],st[i]+1):
#                 x.append(j)
#             if st[i + 1] <= ed[i + 1]:
#                 for j in range(st[i + 1], ed[i + 1] + 1):
#                     y.append(j)
#             else:
#                 for j in range(ed[i + 1], st[i + 1] + 1):
#                     y.append(j)
#
#         for k in range(len(x)):
#             if x[k] in y:
#                 ans += 1
#                 break
#
#     print('#{} {}'.format(tc, ans))
