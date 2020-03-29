import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    k = int(input())
    n = int(input())
    apt = [[0]*n for _ in range(k+1)]

    for i in range(k+1):
        for j in range(n):
            if i == 0:
                apt[i][j] = j+1
            else:
                for z in range(j+1):
                    apt[i][j] += apt[i-1][j-z]
    print(apt[k][n-1])