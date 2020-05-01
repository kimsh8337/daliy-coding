import sys
sys.stdin = open('../../20.04/200430/input.txt', 'r')

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def backtrack(r=0,c=0,i=0):
    global cnt, y_cnt, s_cnt
    if i == 7:
        cnt += 1
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<5 and 0<=nc<5:
            if visited[nr][nc]: continue
            visited[nr][nc] = 1



arr = [list(input()) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
cnt = 0
s_cnt = 0
y_cnt = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'S':
            s_cnt += 1
        elif arr[i][j] == 'Y':
            y_cnt += 1
backtrack()