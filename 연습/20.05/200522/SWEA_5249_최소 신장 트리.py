import sys
sys.stdin = open('input5249.txt', 'r')

for tc in range(1,int(input())+1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s][e] = c
        adj[e][s] = c

    INF = float('inf')
    key = [INF] * (V + 1)
    p = [-1] * (V + 1)
    mst = [0] * (V + 1)

    key[0] = 0
    cnt = 0
    result = 0
    while cnt < (V + 1):
        min = INF
        u = -1
        for i in range(V + 1):
            if not mst[i] and key[i] < min:
                min = key[i]
                u = i
        mst[u] = 1
        result += min
        cnt += 1
        for w in range(V + 1):
            if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                key[w] = adj[u][w]
                p[w] = u
    print('#{} {}'.format(tc,result))