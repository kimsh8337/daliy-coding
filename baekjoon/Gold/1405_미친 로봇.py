import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def dfs(r, c, nxt, p):
    global ans

    if nxt == move[0]:
        if visited[r][c] == move[0]+1:
            ans += p
        return

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if visited[nr][nc] == 0:
            visited[nr][nc] += visited[r][c] + 1
            dfs(nr,nc,nxt+1, p*move[a+1])
            visited[nr][nc] = 0

    return


move = list(map(int, input().split()))
for i in range(1,5):
    move[i] *= 0.01
visited = [[0]*29 for _ in range(29)]
visited[14][14] = 1
ans = 0

dfs(14,14,0,1)
print(ans)