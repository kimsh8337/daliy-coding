# 풀이 1
dr = [0, 0, -1]
dc = [-1, 1, 0]


def dfs(r, c):
    global ans

    if ans != -1:
        return  # global로 ans값을 바꾸기만하고 리턴 값은 주지않음
    if r == 0:
        ans = c
        return
    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        if ladder[nr][nc] == 1:
            ladder[nr][nc] = 2
            dfs(nr, nc)


for tc in range(10):
    tc_num = int(input())
    n = 100
    ladder = [list(map(int, input().split())) for _ in range(n)]
    ans = -1

    for i in range(n):
        if ladder[n - 1][i] == 2:
            sc = i
            break

    dfs(n - 1, sc)
    print('#{} {}'.format(tc_num, ans))

# stack 풀이2
dr = [0, 0, 1]
dc = [-1, 1, 0]


def dfs():
    for i in range(100):
        if ladder[0][i] == 1:  # 출발
            visited = [[0] * 100 for _ in range(100)]
            visited[0][i] = 1
            stack = list()
            stack.append((0, i))
            while len(stack) > 0:
                r, c = stack.pop()
                visited[r][c] = 1
                for k in range(3):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < len(ladder) and 0 <= nc < len(ladder) and visited[nr][nc] == 0:
                        if ladder[nr][nc] == 1:
                            stack.append((nr, nc))
                            break
                        elif ladder[nr][nc] == 2:
                            return i
    return -1


for tc in range(10):
    tc_num = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    ans = dfs()
    print('#{} {}'.format(tc_num, ans))
