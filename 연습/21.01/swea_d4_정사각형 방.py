import sys
sys.stdin = open('input.txt', 'r')

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def find(r,c):
    global cnt

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<n and 0<=nc<n and rooms[nr][nc] == rooms[r][c]+1:
            cnt += 1
            find(nr,nc)

    return cnt


for tc in range(1, int(input())+1):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]
    ans = -float('inf')
    room_num = 0

    for i in range(n):
        for j in range(n):
            cnt = 1
            find(i,j)
            if ans < cnt:
                ans = cnt
                room_num = rooms[i][j]
            elif ans == cnt:
                if room_num > rooms[i][j]:
                    room_num = rooms[i][j]


    print('#{} {} {}'.format(tc, room_num, ans))