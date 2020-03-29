import sys
sys.stdin = open('input.txt', 'r')

def check():
    #가로
    for i in range(9):
        num = [0]*10
        for j in range(9):
            num[puzzle[i][j]] += 1
        if 0 in num[1:]:
            return 0

    #세로
    for j in range(9):
        num = [0]*10
        for i in range(9):
            num[puzzle[i][j]] += 1
        if 0 in num[1:]:
            return 0

    #사각형
    for i in range(0,6,3):
        for j in range(0,6,3):
            num = [0]*10
            for x in range(i,i+3):
                for y in range(j,j+3):
                    num[puzzle[x][y]] += 1
            if 0 in num[1:]:
                return 0

    return 1
T = int(input())

for tc in range(1,T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    # print(puzzle)
    print('#{}'.format(tc),end = ' ')
    print(check())

