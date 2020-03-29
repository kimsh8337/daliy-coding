import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
square = [[0]*n for _ in range(n)]
num = 65
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        square[j][i] = chr(num)
        if num == 90:
            num = 65
        else:
            num += 1

for i in range(n):
    for j in range(n):
        print(square[i][j], end = ' ')
    print()
