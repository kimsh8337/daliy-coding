import sys
sys.stdin = open('input.txt','r')

a,b,c, = map(int, input().split())

if b < c:
    x = a // (c - b)
    print(x+1)
else:
    print(-1)

