import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [[0]*101 for _ in range(101)]

for t in range(n):
    r,c,w,h = map(int, input().split())

    for i in range(n):
