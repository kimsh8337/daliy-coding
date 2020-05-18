import sys
sys.stdin = open('input2468.txt','r')

# dfs
# sys.setrecursionlimit(100000)
# dr = [1,0,-1,0]
# dc = [0,1,0,-1]
#
# def dfs(r,c,h):
#     visit[r][c] = 1
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0<=nr<n and 0<=nc<n:
#             if visit[nr][nc] == 0 and arr[nr][nc] > h:
#                 dfs(nr,nc,h)
#
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# m = 0
# for i in arr:
#     for j in i:
#         if m < j:
#             m = j
# ans = 0
# for k in range(m+1):
#     visit = [[0]*n for _ in range(n)]
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] > k and visit[i][j] == 0:
#                 dfs(i,j,k)
#                 cnt += 1
#     if ans < cnt:
#         ans = cnt
# print(ans)


# bfs
from _collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
def bfs(h):
    visit = [[0] * n for _ in range(n)]
    Q = deque()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and visit[i][j] == 0:
                Q.append((i, j))
                visit[i][j] = 1
                cnt += 1
                while Q:
                    r, c = Q.popleft()
                    visit[r][c]= 1
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if nr < 0 or nr >= n or nc < 0 or nc >= n or arr[nr][nc] <=h: continue
                        if visit[nr][nc] == 1 or (nr, nc) in Q: continue
                        Q.append((nr, nc))
    return cnt

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for h in range(101):
    ans=max(bfs(h),ans)
print(ans)