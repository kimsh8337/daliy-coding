import sys
sys.stdin = open('input.txt', 'r')

def check():
    global ans
    for i in range(9):
        nums = [0] * 10
        for j in range(9):
            nums[sudoku[i][j]] += 1
            if max(nums) > 1:
                ans = 0
                return

    for i in range(9):
        nums = [0] * 10
        for j in range(9):
            nums[sudoku[j][i]] += 1
            if max(nums) > 1:
                ans = 0
                return

    for i in range(0,7,3):
        for j in range(0,7,3):
            nums = [0] * 10
            for k in range(i,i+3):
                for p in range(j,j+3):
                    nums[sudoku[k][p]] += 1
                    if max(nums) > 1:
                        ans = 0
                        return
    return


for tc in range(1,1+int(input())):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    nums = [0]*10
    ans = 1
    check()

    print('#{} {}'.format(tc, ans))