import sys
sys.stdin = open('input.txt', 'r')

dr = [1,0,-1,0]
dc = [0,1,0,-1]
# 재귀
def func(r,c,cnt = 0):
    global num
    if cnt == 7:
        result.add(num)
        return

    num = num + arr[r][c]

    for i in range(4):
        if 0<=r+dr[i]<4 and 0<=c+dc[i]<4:
            func(r+dr[i], c+dc[i],cnt+1)
    num = num[:-1]

for tc in range(1,1+int(input())):
    arr = [list(input().split()) for _ in range(4)]
    num = ''
    result = set()
    for i in range(4):
        for j in range(4):
            func(i,j)
    print('#{} {}'.format(tc, len(result)))


# while
# for tc in range(1, 1+int(input())):
#     a = [list(input().split()) for _ in range(4)]
#     q = []
#     ans = set()
#     for i in range(4):
#         for j in range(4):
#             q.append([i,j,1,a[i][j]])
#     while q:
#         tmp = q.pop()
#         if tmp[2] == 7:
#             ans.add(tmp[3])
#         else:
#             for i in range(4):
#                 x = tmp[0] + dr[i]
#                 y = tmp[1] + dc[i]
#                 if 0<=x<4 and 0<=y<4:
#                     q.append([x,y,tmp[2]+1,tmp[3]+a[x][y]])
#     print('#{} {}'.format(tc, len(ans)))