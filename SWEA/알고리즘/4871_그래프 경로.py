import sys
sys.stdin = open('input.txt', 'r')

def dfs(visited,s):
    for i in range(1,v+1):
        if arr[s][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited,i)
    if (s and g) in visited:
        return 1
    else:
        return 0

for tc in range(1, 1+int(input())):
    v,e = map(int, input().split())
    arr = [[0]*(v+1) for _ in range(v+1)]

    for i in range(e):
        a,b = map(int, input().split())
        arr[a][b] = 1
    s,g = map(int,input().split())

    ans = dfs([s],s)
    print('#{} {}'.format(tc, ans))