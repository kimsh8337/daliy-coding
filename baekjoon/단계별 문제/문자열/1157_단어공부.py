t=str(input())

s=t.upper()
a=s
dicready=list(set(a))
dic={}
for i in dicready:
    dic[i]=0
for i in range(len(a)):
    for x, y in dic.items():
        if x in a[i]:
            dic[x]+=1
value=[]
maxvalue=0
for x in dic.keys():
    if dic[x]>=maxvalue:
        maxvalue=dic[x]
arr=[]
for i in dic.keys():
    if dic[i]==maxvalue:
        arr.append(i)

if len(arr)>=2:
    print('?')
else:
    print(arr[0])



# 풀이 1 시간초과
# a = input().upper()
# b = []
# ans = []
# for i in range(len(a)):
#     cnt = 0
#     for j in range(len(a)):
#         if a[i] == a[j]:
#             if a[i] in b:
#                 break
#             cnt += 1
#     b.append(a[i])
#     ans.append(cnt)
#
# # print(b,ans)
# maxvalue=max(ans)
# arr=[]
# for i in range(len(b)):
#     if ans[i]==maxvalue:
#         arr.append(b[i])
# # print(arr)
#
# if len(arr)==2:
#     print('?')
# else:
#     print(arr[0])


# 풀이2 시간초과
# a = input().upper()
# b = []
# ans = []
# for i in range(len(a)):
#     cnt = 0
#     for j in range(len(a)):
#         if a[i] == a[j]:
#             if a[i] in b:
#                 break
#             cnt += 1
#     b.append(a[i])
#     ans.append(cnt)
#
#     if i >= 1:
#         if ans[0] == ans[1]:
#             print('?')
#             break
#         elif ans[0] < ans[1]:
#             del(ans[0])
#             del(b[0])
#         elif ans[0] > ans[1]:
#             del(ans[1])
#             del(b[1])
# if len(b) == 1:
#     print(b[0])
