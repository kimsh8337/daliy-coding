def 한줄검사(n):
    check = [[0] * 10 for _ in range(2)]
    for i in range(len(sudoku)):
        row = sudoku[n][i]
        col = sudoku[i][n]
        if check[0][row] == 1:
            return False
        if check[1][col] == 1:
            return False
        check[0][row] = check[1][col] = 1
    return True


def 삼삼검사(r, c):
    check = [0] * 10
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if check[sudoku[i][j]] == 1:
                return False
            check[sudoku[i][j]] = 1
    return True


T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    ans = 1
    for i in range(9):
        tmp = 한줄검사(i)
        if not tmp:
            ans = 0
            break

    if ans == 1:
        for i in range(0, len(sudoku), 3):
            for j in range(0, len(sudoku), 3):
                tmp = 삼삼검사(i, j)
                if not tmp:
                    ans = 0
                    break
            if ans == 0:
                break

    print("#{} {}".format(tc, ans))