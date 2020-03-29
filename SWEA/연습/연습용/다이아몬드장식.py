import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    word = input()

    board = [['.']*(4*len(word)+1) for _ in range(5)]

    for i in range(len(word)):
        col = 2 + (4*i)
        row = 2
        board[row][col] = word[i]

        for k in range(8):
            nr = row + dr[k]
            nc = col + dc[k]
            board[nr][nc] = "#"

        for i in range(len(board)):
            for j in range(len(board[i])):
                print("{}".format(board[i][j]), end="")
            print()