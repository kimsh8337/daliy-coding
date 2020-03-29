def dfs(visited, v):
    print(v, end = ' ')
    for i in range(1,n+1):
        if arr[v][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited, i)


n,m = map(int, input().split())

arr = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    st,ed = map(int, input().split())
    arr[st][ed] = arr[ed][st] = 1

dfs([1], 1)