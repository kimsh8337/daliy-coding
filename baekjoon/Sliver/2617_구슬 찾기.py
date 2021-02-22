import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(find, now):
    global cnt

    visited[now] = 1
    for nxt in find[now]:
        if not visited[nxt]:
            cnt += 1
            dfs(find, nxt)


N, M = map(int, input().split())
more = [[] for _ in range(N+1)]
less = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    less[a].append(b)
    more[b].append(a)
mid = (N+1)//2
ans,cnt = 0, 0

for i in range(1,N+1):
    visited = [0] * (N + 1)
    cnt = 0
    dfs(more,i)
    if cnt >= mid:
        ans += 1
    cnt = 0
    dfs(less,i)
    if cnt >= mid:
        ans += 1
print(ans)