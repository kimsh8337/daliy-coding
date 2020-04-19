from collections import deque

V,E = map(int, input().split())
G = [[] for _ in range(V+1)]

for i in range(E):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

# 너비 우선 탐색, 시작점 = 1
# 그래프 = 인접리스트 G, 방문정보 표시(정점의 수만큼 1~V),큐
visit = [True]*(V+1)
Q = deque()

# 시작점을 방문하고 큐에 저장


# 빈큐가 아닐 동안 반복
    # 큐에서 정점을 하나 가져온다. --> v
    # v의 방문하지 않은 모든 인접정점을 찾아서 방문하고 큐에 저장