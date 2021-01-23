import sys
import copy
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**5)

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def findcnt(r,c):
    visited[r][c] = 1

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and iceberg[nr][nc]:
            findcnt(nr, nc)
    return

def melt(r,c):
    global sea
    visited[r][c] = 1

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and not iceberg[nr][nc]:
            sea += 1
    return


n, m = map(int, sys.stdin.readline().split())
iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
year = 0

# clone = [[0]*m for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         clone[i][j] = iceberg[i][j]
clone = copy.deepcopy(iceberg)

while cnt <= 2:
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    # 최초 2개일 때
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and iceberg[i][j]:
                findcnt(i,j)
                cnt += 1
    if cnt >= 2:
        print(year)
        break

    flag = 1
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:
                flag = 0
                break
        if flag == 0:
            break

    if flag:
        print(0)
        break

    visited = [[0] * m for _ in range(n)]
    # 녹이기
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and iceberg[i][j]:
                sea = 0
                melt(i,j)
                clone[i][j] -= sea
                if clone[i][j] < 0:
                    clone[i][j] = 0

    # 녹인 거 적용
    for i in range(n):
        for j in range(m):
            iceberg[i][j] = clone[i][j]
    year += 1