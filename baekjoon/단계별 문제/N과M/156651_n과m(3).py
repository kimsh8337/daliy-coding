import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i=0):
    if i == m:
        for a in range(len(num)):
            print(num[a], end = ' ')
        print()
        return

    for j in range(n):
        num.append(j+1)
        backtrack(i+1)
        num.pop()

n, m = map(int, input().split())
num = []
backtrack()