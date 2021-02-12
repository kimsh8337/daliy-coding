import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(st, depth):
    global ans
    visited[st] = 1

    if depth == 5:
        ans = 1
        return

    for f in friends[st]:
        if not visited[f]:
            dfs(f, depth+1)
            visited[f] = 0
            if ans:
                return
    return


n, m = map(int, input().split())
friends = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
visited = [0]*n
ans = 0

for i in range(n):
    dfs(i,1)
    visited[i] = 0
    if ans:
        break
print(ans)