import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i=0):
    if i == n:
        if len(num) == m:
            for a in range(len(num)):
                print(num[a], end = ' ')
            print()
        return

    num.append(i + 1)
    backtrack(i+1)
    num.pop()
    backtrack(i+1)

n,m = map(int, input().split())
num = []
backtrack()

# 방법 2 - for문 활용
# def backtrack(i=0, cnt =0):
#     if cnt == m:
#         for a in range(len(num)):
#             print(num[a], end = ' ')
#         print()
#         return
#
#     for j in range(i, n):
#         if visit[j] == 0:
#             visit[j] = 1
#             num.append(j+1)
#             backtrack(j + 1,cnt+1)
#             num.pop()
#             visit[j] = 0
#
#
# n, m = map(int, input().split())
# visit = [0] * n
# num = []
# backtrack()