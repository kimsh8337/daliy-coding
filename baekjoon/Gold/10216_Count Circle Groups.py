import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 내 코드 - 메모리 초과...
dr = [1,0,-1,0]
dc = [0,1,0,-1]

def dfs(a,b,dis,cnt,now):
    if dis < cnt:
        return

    visited[now].append((a,b))

    for k in range(4):
        na = a + dr[k]
        nb = b + dc[k]
        if 0<=na<5000 and 0<=nb<5000 and (na,nb) not in visited[now]:
            dfs(na,nb,dis,cnt+1,now)

def find(st, ed):
    global parents

    if parents[st] == ed:
        return

    for (a,b) in visited[st]:
        if (a,b) in visited[ed]:
            d = parents[ed]
            parents[ed] = parents[st]
            for c in range(n):
                if parents[c] == d:
                    parents[c] = parents[ed]
            return

for tc in range(int(input())):
    n = int(input())
    area = []
    parents = [0] * n
    for i in range(n):
        x, y, r = map(int, input().split())
        area.append((x,y,r))
        parents[i] = i
    visited = [[] for _ in range(n)]
    cnt = n

    for i in range(n):
        dfs(area[i][0], area[i][1], area[i][2], 0, i)

    for i in range(n):
        for j in range(i+1,n):
            if parents[i] == parents[j]:
                continue
            find(i,j)

    print(len(set(parents)))



# 유니온 파인드 - 메모리 초과...
# def find(a):
#     if a == parents[a]:
#         return a
#     else:
#         b = find(parents[a])
#         parents[a] = b
#         return b
#
# def merge(a,b):
#     a = find(a)
#     b = find(b)
#     if a == b:
#         return False
#     parents[b] = a
#     return True
#
# for tc in range(int(input())):
#     n = int(input())
#     area = []
#     parents = [0] * n
#     for i in range(n):
#         x, y, r = map(int, input().split())
#         area.append((x,y,r))
#         parents[i] = i
#
#     for i in range(n):
#         for j in range(i+1,n):
#             x1 = area[i][0]
#             x2 = area[j][0]
#             y1 = area[i][1]
#             y2 = area[j][1]
#             dis = area[i][2] + area[j][2]
#
#             if (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2) <= dis * dis :
#                 merge(i,j)
#
#     for i in range(n):
#         parents[i] = find(i)
#
#     print(len(set(parents)))