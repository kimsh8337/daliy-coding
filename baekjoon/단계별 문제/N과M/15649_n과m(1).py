import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i=0):
    if i == m:
        for a in range(len(num)):
            print(num[a], end = ' ')
        print()
        return

    for j in range(n):
        if visit[j] == 0:
            visit[j] = 1
            num.append(j+1)
            backtrack(i + 1)
            num.pop()
            visit[j] = 0


n, m = map(int, input().split())
visit = [0] * n
num = []
backtrack()