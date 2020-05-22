from _collections import deque
from queue import PriorityQueue

# for tc in range(1, int(input())+1):
#     V,E = map(int, input().split())
#     G = [[] for _ in range(V+1)]
#
#     for i in range(E):
#         u, v, w = map(int, input().split())
#         G[u].append((v,w))
#     visit = [False] * (V+1)  # 최단 경로를 찾은 정접들 집합
#     D = [0xfffffff] * (V+1)
#     D[0] = 0
#     # 간선 완화를 brute-force
#     Q = PriorityQueue()
#     Q.put((0,0))  # (거리, 정점)
#     while Q:
#         d, u = Q.get()
#         if visit[u]: continue
#         visit[u] = True
#         for v, weight in G[u]:
#             if not visit[v] and D[v] > d + weight:
#                 D[v] = d + weight
#                 Q.append((D[v],v))
#
#     print('#{} {}'.format(tc,D[V]))

for tc in range(1, int(input())+1):
    V,E = map(int, input().split())
    G = [[] for _ in range(V+1)]

    for i in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v,w))

    D = [0xfffffff] * (V+1)
    D[0] = 0
    # 간선 완화를 brute-force
    Q = deque()
    Q.append(0)
    while Q:
        u = Q.popleft()
        for v, weight in G[u]: # v: 정점, weight: 가중치
            if D[v] > D[u] + weight:
                D[v] = D[u] + weight
                Q.append(v)

    print('#{} {}'.format(tc,D[V]))

# for tc in range(1, int(input())+1):
#     V,E = map(int, input().split())
#     G = [[] for _ in range(V+1)]
#
#     for i in range(E):
#         u, v, w = map(int, input().split())
#         G[u].append((v,w))
#
#     D = [0xfffffff] * (V+1)
#     D[0] = 0
#     # 간선 완화를 brute-force
#
#     while True:
#         flag = True
#         for u in range(V+1):
#             for v, weight in G[u]: # v: 정점, weight: 가중치
#                 if D[v] > D[u] + weight:
#                     D[v] = D[u] + weight
#                     flag = False
#
#         if flag: break
#     print('#{} {}'.format(tc,D[V]))