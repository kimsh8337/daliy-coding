import sys
sys.stdin = open('input6603.txt', 'r')

from itertools import combinations

while(1):
    S = list(map(int, input().split()))

    if S[0] == 0:
        break

    com = list(combinations(S[1:], 6))

    for i in range(len(com)):
        for j in range(6):
            print(com[i][j], end=" ")
        print()
    print()