import sys
sys.stdin = open('input.txt', 'r')

def check(x,y):
    for i in range(9):
        num = [0]*10
        cnt = 0
        for j in range(9):
            if sudoku[i][j] != 0:
                num[sudoku[i][j]] = 1
        for j in range(9):
            if num[j] == 0:
                cnt += 1
                if cnt >=2:
                    continue
                else:
                    for k in range(9):
                        if sudoku[i][k] == 0:
                            sudoku[i][k] = j

    for j in range(9):
        num = [0] * 10
        cnt = 0
        for i in range(9):
            if sudoku[i][j] != 0:
                num[sudoku[i][j]] = 1
        for i in range(9):
            if num[j] == 0:
                cnt += 1
                if cnt >= 2:
                    continue
                else:
                    for k in range(9):
                        if sudoku[i][k] == 0:
                            sudoku[i][k] = i

    for i in range(9):
        for j in range(9):
            for x in range(0,9,3):
                num = [0] * 10
                cnt = 0
                for y in range(0,9,3):
                    if sudoku[i][j] != 0:
                        num[sudoku[i][j]] = 1
                for y in range(9):
                    if num[j] == 0:
                        cnt += 1
                        if cnt >= 2:
                            continue
                        else:
                            for k in range(9):
                                if sudoku[i][k] == 0:
                                    sudoku[i][k] = y


def backtrack(r=0,c=0):
    if r == 9 or c == 9:
        return
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                check(x,y)

sudoku = [list(map(int, input().split())) for _ in range(9)]
backtrack()
for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end = ' ')
    print()