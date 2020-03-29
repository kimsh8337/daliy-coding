import sys
sys.stdin = open('input.txt', 'r')

n,m = map(int, input().split())
square = [[0]*n for _ in range(n)]
num = 1

if m == 1:
    for i in range(n):
        for j in range(n):
            square[i][j] = num
        num += 1
elif m == 2:
    for i in range(n):
        for j in range(n):
            if i %2 == 0:
                square[i][j] = num
                num += 1
            else:
                num -= 1
                square[i][j] = num
elif m == 3:
    for i in range(n):
        num = i+1
        for j in range(n):
            if j == 0:
                square[i][j] = num
            else:
                square[i][j] = square[i][j-1]+i+1


for i in range(n):
    for j in range(n):
        print(square[i][j], end = ' ')
    print()