import sys
sys.stdin = open('input5251.txt', 'r')
from _collections import deque

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





# for tc in range(1,int(input())+1):
#     V, E = map(int, input().split())
#     adj = {i: [] for i in range(V+1)}
#     for i in range(E):
#         s, e, c = map(int, input().split())
#         adj[s].append([e, c])
#
#     INF = float('inf')
#     dist = [INF] * (V +1 )
#     selected = [False] * (V+1)
#
#     dist[0] = 0
#     cnt = 0
#     while cnt < (V+1):
#         min = INF
#         u = -1
#         for i in range(V+1):
#             if not selected[i] and dist[i] < min:
#                 min = dist[i]
#                 u = i
#         selected[u] = True
#         cnt += 1
#         for w, cost in adj[u]:
#             if dist[w] > dist[u] + cost:
#                 dist[w] = dist[u] + cost
#     print('#{} {}'.format(tc, dist[V]))
