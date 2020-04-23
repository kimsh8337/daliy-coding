import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
arr = []
stack = []
result = []
for i in range(N):
    num = int(input())
    arr.append(num)

idx = 0
for j in range(1, N + 1):
    stack.append(j)
    result.append('+')
    while idx < N and len(stack) != 0 and stack[-1] == arr[idx]:
        stack.pop()
        idx += 1
        result.append('-')

if len(stack):
    print('NO')
else:
    for i in result:
        print(i)

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# nums = [i for i in range(1,n+1)]
# stack, ans = [], []
# flag = True
#
# for i in range(n):
#     if not flag:
#         break
#     for k in range(n):
#         if len(stack) == 0:
#             stack.append(nums[0])
#             ans.append('+')
#             nums.pop(0)
#         if len(nums) != 0 and arr[i] != stack[-1]:
#             stack.append(nums[0])
#             ans.append('+')
#             nums.pop(0)
#         if arr[i] == stack[-1]:
#             stack.pop()
#             ans.append('-')
#             break
#         elif arr[i] != stack[-1]:
#             if arr[i] in stack:
#                 flag = False
#                 break
#
# if flag:
#     for i in range(len(ans)):
#         print(ans[i])
# else:
#     print('NO')
