import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def dfs(i, j, pa, cnt):
    global ma
    ma = max(ma, cnt)

    for a in range(4):
        nr = i + dr[a]
        nc = j + dc[a]
        if 0 <= nr < r and 0 <= nc < c and not visited[change_num(nr, nc)]:
            visited[change_num(nr,nc)] = 1
            dfs(nr,nc,pa,cnt+1)
            visited[change_num(nr,nc)] = 0
    return

def change_num(x,y):
    return ord(arr[x][y]) - ord('A')

r, c = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(r)]
visited = [0] * 26
ma = 0
visited[change_num(0,0)] = 1
dfs(0,0,[],1)

print(ma)