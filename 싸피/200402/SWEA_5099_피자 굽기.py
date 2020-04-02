import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 1+int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = []
    r = -1

    while 1:  # 피자 행렬만들기
        if r == n - 1: break
        r += 1
        ans.append((r, arr[r]))

    while 1:  # 요기부터 중요
        if len(ans) == 1: break
        i, j = ans.pop(0)
        j = j // 2
        if j == 0:
            if r < m - 1:
                r += 1
                ans.append((r, arr[r]))
        if j != 0:
            ans.append((i, j))
    print('#{} {}'.format(tc, ans[0][0] + 1))

# for tc in range(1, 1+int(input())):
#     n,m = map(int, input().split())
#     c = list(map(int, input().split()))
#     pizza = []
#
#     for i in range(n):
#         pizza.append([c[i],i])
#
#     i = 0
#     while len(pizza) != 1:
#         pizza[0][0] //= 2
#         if pizza[0][0] == 0:
#             if n+i <m:
#                 pizza.pop(0)
#                 pizza.append([c[n+i], n+i])
#                 i += 1
#             elif n+i >= m:
#                 pizza.pop(0)
#         else:
#             pizza.append(pizza.pop(0))
#
#     print('#{} {}'.format(tc, pizza[0][1]+1))