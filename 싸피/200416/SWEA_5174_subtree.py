import sys
sys.stdin = open('input.txt','r')

for tc in range(1,int(input())+1):
    E,N = map(int,input().split())
    arr = list(map(int,input().split()))
    L=[0]*(E+2)
    R=[0]*(E+2)
    for i in range(0,len(arr),2):
        p,c=arr[i],arr[i+1]
        if L[p]:R[p]=c
        else: L[p]=c

    def subTree(v):

        if v==0: return 0

        l=subTree(L[v])
        r=subTree(R[v])
        return l+r+1

    print(subTree(N))


# def dfs(t):
#     global max_cnt,cnt
#     cnt += 1
#     if ed[t] in st:
#         for i in range(len(st)):
#             if st[i] == ed[t]:
#                 dfs(i)
#     else:
#         if max_cnt < cnt:
#             max_cnt = cnt
#             return
#
#
# for tc in range(1, int(input())+1):
#     e, n = map(int,input().split())
#     li = list(map(int, input().split()))
#     st = []
#     ed = []
#     cnt = 1
#     max_cnt = -float('inf')
#     for i in range(len(li)):
#         if i % 2 ==0:
#             st.append(li[i])
#         else:
#             ed.append(li[i])
#     for i in range(len(st)):
#         if n in st:
#             if st[i] == n:
#                 dfs(i)
#         else:
#             if n in ed:
#                 max_cnt = 1
#             else:
#                 max_cnt = 0
#     print('#{} {}'.format(tc,max_cnt))