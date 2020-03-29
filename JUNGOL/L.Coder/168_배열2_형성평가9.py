import sys
sys.stdin = open('input.txt','r')

n = int(input())
pascal = [[1]*(i+1) for i in range(n)]

for i in range(2,n):
    for j in range(1,i):
        pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]

for i in range(n-1,-1,-1):
    for j in range(i+1):
        print(pascal[i][j], end= ' ')
    print()