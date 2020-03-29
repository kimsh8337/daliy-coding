import sys
sys.stdin = open('input.txt', 'r')

n,m = map(int, input().split())
square = [[0]*m for _ in range(n)]
num = 1
for i in range(n):
    for j in range(m):
       square[i][j] = num
       num+=1
for i in range(n):
    for j in range(m):
        print(square[i][j], end = ' ')
    print()