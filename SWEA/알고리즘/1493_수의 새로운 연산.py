import sys
sys.stdin = open('input.txt', 'r')
# v1
T = int(input())

for tc in range(1, T+1):
    board = [[0]*300 for _ in range(300)]
    value = 1

    for i in range(1, 300):
        r = i
        c = 1
        for j in range(1, i+1):
            board[r][c] = value
            value += 1
            r -= 1
            c += 1

    p ,q = map(int, input().split())

    posP = (0,0)
    posQ = (0,0)

    for i in range(1,300):
        for j in range(1, 300):
            if board[i][j] == p:
                posP = (i,j)
            if board[i][j] == q:
                posQ = (i,j)

    point = (posP[0] + posQ[0], posP[1] + posQ[1])
    result = board[point[0]][point[1]]

    print('#{} {}'.format(tc, result))