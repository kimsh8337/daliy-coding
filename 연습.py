import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i=0, cnt=0):
    if cnt == m:
        for a in range(len(num)):
            print(num[a],end = ' ')
        print()
        return

    for j in range(i,n):
        num.append(j+1)
        backtrack(j,cnt+1)
        num.pop()

n,m = map(int, input().split())
num = []
backtrack()