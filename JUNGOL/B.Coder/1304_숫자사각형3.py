import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
square = [[0]*n for _ in range(n)]
num = 1

for i in range(n):
    for j in range(n):
        square[j][i] = num
        num +=1
for i in range(n):
    for j in range(n):
        print(square[i][j], end = ' ')
    print()