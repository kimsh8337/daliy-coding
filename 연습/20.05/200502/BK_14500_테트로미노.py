import sys
sys.stdin = open('input.txt', 'r')

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(r,c,k,n_sum):
    global MAX,MAX_n
    if n_sum+MAX_n*(3-k)<=MAX:
        return
    if k==3:
        if MAX<n_sum:
            MAX = n_sum
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if arr[nr][nc] == 0 or visit[nr][nc]:continue
        if k==1:
            visit[nr][nc] = 1
            n_sum += arr[nr][nc]
            dfs(r,c,k+1,n_sum)
            n_sum -= arr[nr][nc]
            visit[nr][nc] = 0
        visit[nr][nc] = 1
        n_sum += arr[nr][nc]
        dfs(nr, nc, k+1, n_sum)
        n_sum -= arr[nr][nc]
        visit[nr][nc] = 0



N, M = map(int, input().split())
arr = [[0]*(M+2)]
for i in range(N):
    arr.append([0]+list(map(int, input().split()))+[0])
arr.append([0]*(M+2))
visit = [[0]*(M+2) for _ in range(N+2)]
MAX = 0
MAX_n = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j]>MAX_n:
            MAX_n = arr[i][j]
        visit[i][j] = 1
        dfs(i,j,0,arr[i][j])
        visit[i][j] = 0
print(MAX)

# drc = [(1,0),(0,1),(0,-1),(-1,0)]
# fuck = [[(0,1),(0,2),(1,1)],[(1,0),(2,0),(1,-1)],[(1,0),(1,1),(2,0)]]
#
# def dfs(r,c,cnt,sum_cnt):
#     global ans,num
#     if sum_cnt+num*(4-cnt)<=ans:
#         return
#     if cnt == 4:
#         if ans < sum_cnt:
#             ans = sum_cnt
#         return
#
#     for d in range(4):
#         nr = r + drc[d][0]
#         nc = c + drc[d][1]
#         if 0<=nr<n and 0<=nc<m:
#             if visited[nr][nc] == 1: continue
#             visited[nr][nc] = 1
#             dfs(nr,nc,cnt+1,sum_cnt + arr[nr][nc])
#             visited[nr][nc] = 0
#
# def fucking(r,c):
#     global ans
#     for i in range(3):
#         s = arr[r][c]
#         for j in range(3):
#             try:
#                 nr = r + fuck[i][j][0]
#                 nc = c + fuck[i][j][1]
#                 s += arr[nr][nc]
#             except IndexError:continue
#         ans = max(ans, s)
#
# def solve():
#     for i in range(n):
#         for j in range(m):
#             fucking(i,j)
#             dfs(i,j,0,0)
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# num = 0
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] > num:
#             num = arr[i][j]
# visited = [[0]*m for _ in range(n)]
# ans = 0
# solve()
# print(ans)
