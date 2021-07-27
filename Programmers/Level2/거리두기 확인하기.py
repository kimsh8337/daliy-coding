from collections import deque

dr = [-1,0,1,0]
dc = [0,-1,0,1]

def bfs(i,j,room):
    visited = [[0 for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append((i,j,0))

    while q:
        r,c, man_len = q.popleft()
        visited[r][c] = 1

        if man_len == 2:
            return 1

        for a in range(4):
            nr = r + dr[a]
            nc = c + dc[a]
            if 0<=nr<5 and 0<=nc<5:
                if visited[nr][nc] == 0:
                    if room[nr][nc] == 'P':
                        return 0
                    elif room[nr][nc] == 'O':
                        q.append((nr,nc,man_len+1))

    return 1

def solution(places):
    answer = []
    for room in places:
        stop = False
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    if bfs(i,j,room) == 0:
                        stop = True
                        break
            if stop == True:
                break
        if stop == True:
            answer.append(0)
        else:
            answer.append(1)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))