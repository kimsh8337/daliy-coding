import sys
sys.stdin = open('input.txt', 'r')

def getsum(x):
    if x == n:
        return 1
    if x > n :
        return 0
    return getsum(x+10) + getsum(x+20)*2

for tc in range(1, 1+int(input())):
    n = int(input())
    print('#{} {}'.format(tc, getsum(0)))