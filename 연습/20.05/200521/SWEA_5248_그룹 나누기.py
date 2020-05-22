import sys
sys.stdin = open('input5248.txt', 'r')


def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])


def union(x,y):
    parent[find_set(y)] = find_set(x)


for tc in range(1, 1+int(input())):
    n, m = map(int, input().split())
    parent = [0]*(n+1)

    for i in range(1, n+1):
        parent[i] = i

    data = list(map(int, input().split()))
    for i in range(m):
        st = data[2*i]
        ed = data[2*i+1]
        union(st, ed)

    result = []
    for i in range(len(parent)):
        result.append(find_set(i))

    print('#{} {}'.format(tc, len(set(result))-1))


# bfs
# from collections import deque
#
# def BFS(n):
#     q = deque([n])
#     check[n] = 1
#     while q:
#         n = q.popleft()
#         for v in G[n]:
#             if not check[v]:
#                 check[v] = 1
#                 q.append(v)
#
# for tc in range(1,int(input())+1):
#     N,M = map(int,input().split())
#     G = [[] for _ in range(N+1)]
#     arr = list(map(int,input().split()))
#     for i in range(0,M*2,2):
#         G[arr[i]].append(arr[i+1])
#         G[arr[i+1]].append(arr[i])
#     check = [0] * (N+1);group = 0
#     for j in range(1,N+1):
#         if not check[j]:
#             if not G[j]:
#                 group += 1
#                 check[j] = 1
#             else:
#                 group += 1
#                 BFS(j)
#     print("#{} {}".format(tc,group))